# 旧站 Academic 功能实现

本目录保存迁移前实际运行的 academic 相关实现。`source/` 中的代码仍使用 Jekyll Liquid/SCSS/Python，不能直接被 Hugo 执行；它们用于后续重写时核对行为。

## Google Scholar 引用更新

数据流：

```text
_data/socials.yml 中的 scholar_userid
  -> bin/update_scholar_citations.py
  -> scholarly 获取作者论文
  -> _data/citations.yml
  -> bib.liquid 读取 citation count
  -> Shields.io 生成 citations badge
```

- `source/update-citations.yml` 每周一、三、五运行，也支持手动触发。
- `source/update_scholar_citations.py` 使用 `scholarly` 和 `PyYAML`。
- 脚本按 Scholar publication ID 保存标题、年份和引用数。
- 同一天已经更新时跳过请求；数据无变化时不重写文件。
- Action 检查文件哈希，仅在引用数据变化时提交并推送。
- Google Scholar 没有稳定的官方公开 API，`scholarly` 抓取可能受限流或页面变化影响。

精简依赖见 `scholar-requirements.txt`。

## GitHub stars 和 forks

旧站没有 GitHub stars 定时更新脚本。`source/bib.liquid` 根据 BibTeX 的 `github = {owner/repo}` 在浏览器中请求动态图片：

```text
https://img.shields.io/github/stars/owner/repo?style=social&logo=github
https://img.shields.io/github/forks/owner/repo?style=social&logo=github
```

因此 stars/forks 数量由 Shields.io 在页面加载时提供，不写入仓库。forks 仅在 `github_show_forks = {true}` 时显示。

## 论文 banner 与缩略图

- `papers.bib` 的 `preview` 指向 `assets/img/publication_preview/` 中的图片。
- `abbr` 查询 `venues.yml`，取得 venue URL 和 banner 颜色。
- `source/bib.liquid` 将 banner 绝对定位在缩略图左上角，并附带年份。
- `source/figure.liquid` 负责响应式图片渲染。
- `source/publications.scss` 定义阴影、banner、双栏布局和移动端表现。

## 论文 badge

`source/bib.liquid` 支持：

- GitHub stars 和可选 forks：Shields.io 动态 badge。
- Google Scholar citations：定时写入的 YAML 数值加 Shields.io 静态 badge。
- Hugging Face：根据 BibTeX 链接生成 Shields.io badge。
- Altmetric：根据显式 ID、arXiv、DOI、PMID 或 ISBN 创建嵌入。

## 论文卡片其他行为

- 根据站点配置高亮本人姓名。
- 根据 coauthor 数据为作者添加主页链接。
- 作者过多时折叠为 `N more authors`。
- 显示 PDF、Code 和可展开的 BibTeX 按钮。
- `selected_papers.liquid` 用 `selected=true` 筛选首页论文。
- `publications-page.md` 是旧 `/publications/` 页面入口。

## Hugo 重写建议

- 保持论文数据只有一个来源，优先使用 `data/publications.yaml`，或在构建前可靠地将 BibTeX 转换为 YAML/JSON。
- Scholar Action 应改写 Hugo 的 `data/citations.yaml`，并使用专用 requirements 文件。
- stars 可以继续使用 Shields.io；如果需要无第三方依赖，再考虑 GitHub API 定时写入。
- banner、badge、按钮应实现为 Hugo partial，不应复制整个上游 Terminal 布局。
- 图片应放在 `static/img/publications/`，CV 放在 `static/pdf/`。
