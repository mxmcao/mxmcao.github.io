#!/usr/bin/env python3
"""Refresh the Hugo citation snapshot from a public Google Scholar profile."""

from __future__ import annotations

import argparse
import os
import sys
import tempfile
from datetime import date
from pathlib import Path
from typing import Any

import yaml


DEFAULT_CITATIONS = Path("data/citations.yaml")
DEFAULT_PUBLICATIONS = Path("data/publications.yaml")


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def publication_ids(publications: list[dict[str, Any]]) -> set[str]:
    return {
        paper["scholar_id"]
        for year_group in publications
        for paper in year_group.get("papers", [])
        if paper.get("scholar_id")
    }


def validate_snapshot(
    citations: dict[str, Any], publications: list[dict[str, Any]]
) -> None:
    scholar_user_id = citations.get("scholar_user_id")
    if not scholar_user_id:
        raise ValueError("data/citations.yaml is missing scholar_user_id")

    expected = publication_ids(publications)
    available = set(citations.get("papers", {}))
    missing = expected - available
    if missing:
        raise ValueError(
            "citation snapshot is missing publication IDs: " + ", ".join(sorted(missing))
        )

    for scholar_id, paper in citations.get("papers", {}).items():
        count = paper.get("citations")
        if not isinstance(count, int) or count < 0:
            raise ValueError(f"invalid citation count for {scholar_id}: {count!r}")


def normalize_publication_id(publication: dict[str, Any]) -> str | None:
    publication_id = publication.get("pub_id") or publication.get("author_pub_id")
    if not publication_id:
        return None
    return str(publication_id).rsplit(":", maxsplit=1)[-1]


def fetch_citations(scholar_user_id: str, tracked_ids: set[str]) -> dict[str, Any]:
    try:
        from scholarly import scholarly
    except ImportError as error:
        raise RuntimeError(
            "scholarly is not installed; run `python -m pip install -r requirements-scholar.txt`"
        ) from error

    author = scholarly.search_author_id(scholar_user_id)
    author_data = scholarly.fill(author, sections=["publications"])
    fetched: dict[str, Any] = {}

    for publication in author_data.get("publications", []):
        scholar_id = normalize_publication_id(publication)
        if scholar_id not in tracked_ids:
            continue

        bibliography = publication.get("bib", {})
        count = publication.get("num_citations", 0)
        fetched[scholar_id] = {
            "citations": int(count or 0),
            "title": bibliography.get("title", "Unknown title"),
            "year": str(bibliography.get("pub_year", "Unknown")),
        }

    missing = tracked_ids - set(fetched)
    if missing:
        raise RuntimeError(
            "Google Scholar response did not contain tracked IDs: "
            + ", ".join(sorted(missing))
        )

    return fetched


def write_snapshot(path: Path, snapshot: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            yaml.safe_dump(snapshot, stream, sort_keys=False, allow_unicode=True)
        temporary_path.replace(path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--citations", type=Path, default=DEFAULT_CITATIONS)
    parser.add_argument("--publications", type=Path, default=DEFAULT_PUBLICATIONS)
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate the local snapshot without contacting Google Scholar",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    citations = load_yaml(args.citations)
    publications = load_yaml(args.publications)
    validate_snapshot(citations, publications)

    if args.check:
        print(
            f"Citation snapshot is valid for {len(publication_ids(publications))} publications."
        )
        return 0

    tracked_ids = publication_ids(publications)
    print(f"Refreshing {len(tracked_ids)} citation counts from Google Scholar...")
    papers = fetch_citations(citations["scholar_user_id"], tracked_ids)
    snapshot = {
        "scholar_user_id": citations["scholar_user_id"],
        "metadata": {
            "last_updated": date.today().isoformat(),
            "source": "Google Scholar",
        },
        "papers": papers,
    }
    write_snapshot(args.citations, snapshot)
    print(f"Updated {args.citations}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"Citation refresh failed: {error}", file=sys.stderr)
        raise SystemExit(1)
