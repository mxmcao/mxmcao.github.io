# Hugo Terminal 迁移记录

## 改动背景和目标

旧站基于 Jekyll/al-folio，包含大量未使用的模板内容、Ruby/Python/Node 依赖和示例资源。个人资料和 academic 实现完成归档后，将站点替换为可独立构建的最小 Hugo Terminal 骨架。

## 修改的文件及具体内容

- 删除原 al-folio 的 Jekyll 配置、Liquid 模板、Ruby/Python 依赖、示例内容、资源和旧 workflows。
- `hugo.toml`：配置个人主页 URL、三项导航和 Terminal Hugo Module。
- `go.mod`、`go.sum`：固定 `hugo-theme-terminal/v4` 版本。
- `content/`：添加 About、Research、CV 占位页面，暂不导入旧个人信息。
- `static/style.css`、`assets/js/`、`layouts/partials/`：添加轻量配色、主题切换和主题扩展入口。
- `.github/workflows/hugo.yml`：使用 GitHub Pages artifact 部署 Hugo 构建结果。
- `README.md`、`.gitignore`：记录本地使用和构建产物规则。

## 核心实现说明

主题通过 Hugo Module 引入，不复制到 `themes/`。配色使用 Terminal 原生支持的 `static/style.css` 覆盖入口，JavaScript 使用 `extended_head.html` 和 `extended_footer.html` 扩展点加载，不覆盖上游布局模板。

## 关键代码摘录及对应文件路径

`hugo.toml`：

```toml
[[module.imports]]
path = "github.com/panr/hugo-theme-terminal/v4"
```

`.github/workflows/hugo.yml`：

```text
hugo --gc --minify --cleanDestinationDir --baseURL <GitHub Pages base URL>
```

## 实际执行的测试和结果

- `hugo mod tidy`、`hugo mod verify`：通过，Terminal 固定为 `v4.2.3`。
- `hugo --gc --minify --cleanDestinationDir --panicOnWarning`：通过；生成 10 个页面、2 个 alias 和 8 个静态文件。
- `actionlint .github/workflows/hugo.yml`：通过，GitHub Pages workflow 无诊断。
- 本地 `hugo server` HTTP 检查：`/`、`/research/`、`/cv/`、`/publications/`、`/404.html`、favicon、CSS 和 robots 均返回 200。
- 生成物检查：`prev-information/` 和 `dev_note/` 均未进入 `public/`；`/publications/` 正确跳转到 `/research/`。
- Playwright Chromium 桌面 `1440x900` 与移动 `390x844`：浅色/深色截图均非空，无横向溢出，无 console、page 或 network error。
- 交互检查：主题切换更新颜色、ARIA 状态和 `localStorage`；桌面 Research 导航、移动菜单和 CV 导航正常。
- 旧技术栈检查：仓库活动路径中不再存在 `Gemfile`、`_config.yml`、`package.json`、Dockerfile 或 Jekyll Liquid 模板；归档目录除外。
- `git diff --check -- . ':!prev-information/**'`：通过。
- Prettier 未运行：迁移后项目不包含 Node/npm/Prettier，当前环境也没有 `npx`；Hugo/TOML/Action/浏览器验证覆盖了活动文件。

## 已知风险或未验证内容

- 当前页面是占位内容，尚未把 `prev-information/` 接入 Hugo。
- 部署需在 GitHub 仓库 Settings > Pages 中将 Source 设置为 GitHub Actions。
- 首次远端部署要等合并并推送到 `main` 后才能验证。
- `/publications/` 已兼容跳转到 `/research/`；旧 CV PDF 路径暂未恢复。
