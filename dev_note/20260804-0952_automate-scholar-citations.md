# 接入 Google Scholar 引用快照更新

## 改动背景和目标

Research 页面需要显示两篇论文的 Google Scholar 引用数，并自动刷新。Google Scholar 没有稳定的公开 API，抓取可能被限流，因此采用“仓库快照兜底、部署时尽力更新”的容错方案，避免外部服务故障阻塞 GitHub Pages。

## 修改的文件及具体内容

- `data/citations.yaml`：保存 Scholar 用户 ID、更新时间和两篇论文的引用数快照。
- `scripts/update_scholar_citations.py`：校验快照或抓取 Scholar 数据，使用临时文件原子替换。
- `requirements-scholar.txt`：固定 PyYAML 和 scholarly 版本。
- `layouts/partials/publication-buttons.html`：增加 citation 按钮及论文条目链接。
- `layouts/shortcodes/publications.html`：显示引用数据刷新时间。
- `static/style.css`：增加 citation 按钮样式。
- `.github/workflows/hugo.yml`：部署前尝试刷新，并增加每周一定时构建；失败时使用已提交快照继续部署。

## 核心实现说明

脚本只跟踪 `data/publications.yaml` 中声明的 `scholar_id`，防止个人 Scholar 主页中的其他论文意外进入网站数据。输出先写入同目录临时文件，再通过原子替换更新。GitHub Actions 不提交或 push 更新结果，新数据只进入当次 Pages 构建产物。

## 关键代码摘录及对应文件路径

`scripts/update_scholar_citations.py`：

```python
missing = tracked_ids - set(fetched)
if missing:
    raise RuntimeError("Google Scholar response did not contain tracked IDs: ...")
```

`.github/workflows/hugo.yml`：

```yaml
- name: Refresh Google Scholar citation snapshot
  continue-on-error: true
  run: timeout 120s python scripts/update_scholar_citations.py
```

## 实际执行的测试和结果

- `python -m py_compile scripts/update_scholar_citations.py`：通过。
- `python scripts/update_scholar_citations.py --check`：通过，确认快照覆盖两篇配置论文且计数合法。
- 在 `/tmp` 新建隔离 Python 3.12 虚拟环境，按 `requirements-scholar.txt` 安装依赖：通过。
- 在隔离副本执行真实 Google Scholar 刷新：通过；2026-08-04 抓取到 MLP Memory 19 次、Memory Decoder 16 次引用。
- 对刷新后的隔离快照再次执行 `--check`：通过。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-citations-stage`：通过；生成页面包含两个 Scholar 条目链接、引用数按钮和刷新日期。
- 当前环境没有 `actionlint`，workflow 将在最终验证阶段使用可用的 YAML/Actions 静态检查补验。

## 已知风险或未验证内容

- Google Scholar 可能限流或改变页面结构；失败时页面会继续显示最后一次提交的快照。
- workflow 内更新不会回写仓库，因此更新时间只存在于部署产物；仓库快照需在必要时人工刷新提交。
