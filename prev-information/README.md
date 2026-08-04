# 旧站信息归档

本目录保存从 al-folio/Jekyll 旧站提取的个人信息、论文资料，以及旧站学术功能的实现参考。归档时间为 2026-08-04，来源提交为 `1aa6486`。

这些文件不会被新的 Hugo 站点自动发布。后续应先人工审核，再选择性迁移到 `content/`、`data/` 或 `static/`。

## 目录

- `personal/`：主页、联系方式、新闻、头像、CV、域名验证文件，以及旧站完整配置快照。
- `publications/`：论文 BibTeX、引用量快照、venue 配置和论文预览图。
- `academic-reference/`：Google Scholar 更新、论文卡片、banner、badge 等旧实现及说明。
- `SHA256SUMS`：关键原始文件的校验值和来源路径。

## 注意事项

- 此目录位于公开仓库，归档内容也会公开可见。
- `personal/site-config.yml` 是迁移前完整配置快照，既包含个人设置，也包含大量 al-folio 默认设置。
- `_data/cv.yml` 和 `assets/json/resume.json` 仍是模板自带的 Albert Einstein 示例，因此没有归档为个人信息。
- 未发布的示例博客、项目、教学和新闻条目没有归档。
- 新 Hugo 站点当前只使用占位内容，不直接读取本目录。

## 后续迁移建议

1. 从 `personal/about.md` 提取最终首页文案。
2. 从 `personal/socials.yml` 迁移公开社交链接。
3. 将 `publications/papers.bib` 转换为 Hugo 可直接消费的结构化数据。
4. 复用 `academic-reference/README.md` 描述的 Scholar 更新链路。
5. 仅将需要公开的图片和 PDF 复制到 Hugo 的 `static/`。
