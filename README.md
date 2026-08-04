# mxmcao.github.io

A minimal academic homepage built with Hugo and [hugo-theme-terminal](https://github.com/panr/hugo-theme-terminal).

## Requirements

- Hugo Extended 0.90.0 or newer
- Go 1.19 or newer

The repository currently pins Terminal theme `v4.2.3` through Hugo Modules.

## Local development

```bash
hugo server
```

Open <http://localhost:1313/>. To include draft content, run `hugo server -D`.

## Production build

```bash
hugo --gc --minify --cleanDestinationDir
```

The generated site is written to `public/`, which is intentionally ignored by Git.

## Content status

The current pages are minimal placeholders. Information and academic integrations from the previous al-folio site are preserved in `prev-information/` but are not rendered by Hugo yet.

## Deployment

Pushes to `main` trigger `.github/workflows/hugo.yml`, which builds the site and deploys the `public/` artifact to GitHub Pages. The repository's Pages source must be set to **GitHub Actions**.
