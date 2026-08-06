# 使用 chosen-one 头像路径

## 改动背景和目标

主页头像已准备为 `images/profile/chosen-one.png`，本次将 About 页头像从旧的 `images/profile.png` 映射切换到用户指定的根路径 `/images/profile/chosen-one.png`。

## 修改的文件及具体内容

- `layouts/shortcodes/home-profile.html`：将头像 `src` 改为 `/images/profile/chosen-one.png`。
- `dev_note/20260806-1300_use-chosen-profile-image.md`：记录路径切换和验证结果。

## 核心实现说明

该路径以站点根目录为基准，不经过 `relURL` 处理，生成页面会直接请求 `/images/profile/chosen-one.png`。图片文件位于 `images/profile/chosen-one.png`，由 `hugo.toml` 中现有的 `images -> static/images` mount 输出到该 URL。

## 实际执行的测试和结果

- `hugo --minify --destination <temporary-directory>`：通过。
- `git diff --check`：通过。
- 检查生成的 About HTML：头像 URL 为 `/images/profile/chosen-one.png`。
- 检查生成的静态文件：`images/profile/chosen-one.png` 存在且为 800×800 PNG。

## 已知风险或未验证内容

- 根路径写法适用于当前部署在域名根目录的 GitHub Pages；如果未来将站点部署到子路径，需要改回 `relURL` 或使用 Hugo 的 `absURL` 配置。
