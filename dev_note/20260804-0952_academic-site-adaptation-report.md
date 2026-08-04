# Hugo Terminal 学术主页适配验收报告

## 目标

在保留 Hugo Terminal v4.2.3 上游模块与 GitHub Pages 路径契约的前提下，恢复旧站真实个人信息，并吸收 Hugo Theme Console 的静态控制台排版和 John Math 学术页面的论文资源按钮。页面不得加入交互式终端。

## 主流程与受保护契约

- 内容入口：`content/_index.md`、`content/research.md`、`content/cv.md`。
- 对外路径：`/`、`/research/`、`/cv/`，并保留 `/publications/` alias。
- 构建入口：`hugo --gc --minify --cleanDestinationDir`。
- 部署入口：push `main`、手动 workflow 或每周定时任务触发 `.github/workflows/hugo.yml`。
- 归档契约：`prev-information/` 保持原始个人信息和学术资料，不被新的展示数据覆盖。

## 已实现改动

### 首页

- 恢复 Jiaqi Cao 的个人介绍、导师、实习经历、研究兴趣、头像和联系信息。
- 使用 `mxmcao:~#`、`$ cat ...` 等纯静态 Console 表现，不含输入框或命令执行。
- 在 Recent News 上方加入求职 banner，并恢复三条真实学术动态。
- 保留并适配已有的明暗主题按钮及用户偏好持久化。

### Research

- 以 `data/publications.yaml` 为单一数据源展示 MLP Memory 和 Memory Decoder。
- 按年份倒序分组，保留论文图片及 ICLR/NeurIPS venue banner。
- 增加 arXiv、Code、Hugging Face 和 Google Scholar citation 按钮。
- 桌面端采用图片/信息双栏，移动端自动切换为单列。

### 引用数据与部署

- `data/citations.yaml` 保存稳定兜底快照。
- `scripts/update_scholar_citations.py` 只更新配置中的两篇论文，校验 ID 完整性并原子写入。
- 部署时尝试刷新 Scholar；外部请求失败不会阻塞 Pages 构建，也不会自动 commit/push。
- 2026-08-04 实际抓取结果：MLP Memory 19 次、Memory Decoder 16 次。

## 验证结果

- `git diff --check`：通过。
- `git fsck --no-progress`：无损坏对象；仅存在 3 个不可达 blob。
- `hugo mod verify`：通过。
- citation 脚本 `py_compile` 与 `--check`：通过。
- 在隔离 Python 3.12 环境按锁定依赖执行真实 Scholar 刷新：通过。
- `actionlint v1.7.7 .github/workflows/hugo.yml`：通过。
- Hugo 生产构建：通过，生成 10 个页面、11 个静态文件和 2 个 aliases。
- HTTP 爬取：检查 28 个站内页面及资源，全部返回 200。
- Playwright Chromium：桌面 1440px、移动 390px 均无横向溢出；图片加载、移动菜单、主题切换及刷新后持久化均通过。
- 页面检查：不存在 `<input>`、`<textarea>`、`terminal-input`、鼠标字符 canvas 或 WebGL liquid-glass。
- 人工截图复核：修复了头像 HTML 高度属性引起的纵向拉伸，最终桌面和移动端均保持方形构图。

## 有意保留与未实现内容

- CV 页面继续保持占位状态，因为本轮没有选择恢复 A7。
- 不迁移旧 al-folio 的 Blog、Projects、Repositories、Books、Teaching 和论文搜索。
- 不加入作者主页数据库、折叠摘要、交互终端、鼠标字符动画或 WebGL 效果。
- 不复制 John Math 的整套 layouts/assets fork，继续通过 Hugo Module 跟随 Terminal 上游。

## 已知风险

- Google Scholar 是非稳定外部来源，可能限流或改变页面结构；失败时自动使用提交的快照。
- Scholar workflow 的更新只影响当次部署产物，不回写仓库；如需更新仓库中的兜底值，需要人工运行并提交。
- 求职文案和毕业时间属于时效信息，状态变化后需更新 `data/profile.yaml`。
- `weixin://` 链接仅在安装微信的设备上可用。
