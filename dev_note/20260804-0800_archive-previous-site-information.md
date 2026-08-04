# 旧站信息归档记录

## 改动背景和目标

站点计划从 Jekyll/al-folio 迁移到 Hugo Terminal。删除旧实现前，将真实个人信息、论文资料和 academic 功能参考集中保存到 `prev-information/`，避免与模板示例混淆或在迁移中丢失。

## 修改的文件及具体内容

- `prev-information/personal/`：归档首页、联系方式、真实新闻、头像、CV、Google Search Console 验证文件和旧配置。
- `prev-information/publications/`：归档 BibTeX、Scholar 引用量、venue 配置和论文图片。
- `prev-information/academic-reference/`：归档 Scholar 更新 Action/Python 脚本，以及论文模板、样式和页面入口。
- `prev-information/README.md`、子目录 README 和 `SHA256SUMS`：记录来源、边界、工作原理和校验值。

## 核心实现说明

个人与论文原始文件保持原格式，不在归档阶段转换成 Hugo 内容。Academic 说明明确区分了两种更新方式：Google Scholar 由定时脚本写入 YAML，GitHub stars/forks 由 Shields.io 在浏览器端动态提供。

## 关键代码摘录及对应文件路径

Google Scholar 数据流记录在 `prev-information/academic-reference/README.md`：

```text
scholar_userid -> scholarly -> citations.yml -> Liquid -> Shields badge
```

GitHub stars 的旧实现保存在 `prev-information/academic-reference/source/bib.liquid`：

```text
https://img.shields.io/github/stars/owner/repo
```

## 实际执行的测试和结果

- 对关键源文件和归档副本执行 `cmp`：全部逐字节一致；Google Search Console 验证文件也通过 SHA-256 对比。
- 对个人资料、论文数据、图片、CV 和 academic 核心实现执行 `sha256sum`：全部与 `prev-information/SHA256SUMS` 中记录一致。
- 执行归档目录完整性检查：共 25 个文件，大小约 1.4 MB。
- 搜索 Einstein、示例 GitHub 用户等模板内容：除 README 的排除说明和完整旧配置中的上游文档链接外，没有归档模板示例。
- `npx prettier . --write`：未执行成功，当前环境没有 Node.js/npm/npx，且没有 Docker 可用；归档原件已加入 `.prettierignore`，新增 Markdown 由 `git diff --check` 检查。
- `git diff --cached --check`：归档原件 `personal/about.md` 和 `personal/site-config.yml` 报告 5 处旧有尾随空格；为保持 SHA-256 和逐字节一致未修改。排除这两份原件后，其余变更通过 whitespace 检查。

## 已知风险或未验证内容

- `prev-information/` 位于公开仓库，其中的邮箱、微信、CV 等仍然公开。
- Scholar 抓取脚本依赖非官方的 `scholarly`，后续运行可能受 Google 限流影响。
- 归档的 Liquid 和 SCSS 仅作参考，不能直接在 Hugo 中运行。
