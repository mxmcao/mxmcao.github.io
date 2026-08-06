# 将联系入口移至 Header 并增加 WeChat 二维码弹窗

## 改动背景和目标

首页的 `Let's connect` 区块与其余主页内容重复占用纵向空间。此次将 Email、GitHub、Google Scholar、LinkedIn 和 WeChat 移至 About / Research / CV 所在的导航行，以图标形式呈现。

WeChat 入口不再跳转 `weixin://` 协议，而是弹出仓库已有的加好友二维码。图标沿用旧 `main` 分支使用的 Font Awesome `fa-weixin` 品牌外形。

## 修改的文件及具体内容

- `layouts/shortcodes/home-profile.html`
  - 删除 `Let's connect` 主页区块。
- `layouts/partials/header.html`
  - 在导航区域加入联系图标组。
- `layouts/partials/header-socials.html`
  - 从 `data/profile.yaml` 渲染五个联系入口；WeChat 使用弹窗触发按钮。
  - 输出原生 `dialog` 和二维码图片。
- `layouts/partials/social-icon.html`
  - 为 WeChat 增加与旧站一致的品牌图标路径。
- `assets/js/wechat-dialog.js`
  - 实现打开、关闭按钮和点击遮罩关闭二维码弹窗；原生 dialog 同时支持 `Esc` 关闭。
- `layouts/partials/extended_footer.html`
  - 构建并加载二维码弹窗脚本。
- `hugo.toml`
  - 将 `prev-information/avatar/wechat.png` 挂载为 `static/images/wechat.png`。
- `static/style.css`
  - 添加图标导航与小尺寸二维码弹窗样式，移除不再使用的首页联系列表样式。

## 核心实现说明

桌面端图标组与 About / Research / CV 位于同一导航行；移动端因文字菜单收起，图标组独立显示在 Header 下方，确保联系方式仍可访问。

二维码弹窗使用原生 `<dialog>`，总宽度限制为 `260px`，并按 viewport 限制图片高度。二维码源文件保持不变，构建输出与源文件使用相同校验和。

## 关键代码摘录及对应文件路径

`layouts/partials/header-socials.html`：

```html
<button data-wechat-dialog-open aria-haspopup="dialog">
  {{ partial "social-icon.html" . }}
</button>
```

`static/style.css`：

```css
.wechat-dialog {
  box-sizing: border-box;
  width: min(16.25rem, calc(100vw - 2rem));
  max-height: calc(100vh - 2rem);
}
```

## 实际执行的测试和结果

- 执行 `git diff --check`：通过，没有空白符错误。
- 执行 `hugo --minify --destination /tmp/mxmcao-header-wechat-final-check`：通过，生成 10 个页面、12 个静态文件和二维码弹窗脚本。
- 检查生成首页：含一个 `data-wechat-dialog-open` 触发器、一个原生 dialog、关闭按钮与 `aria-haspopup="dialog"`；不再输出 `weixin://` 跳转。
- 校验 `prev-information/avatar/wechat.png` 与构建输出的 `images/wechat.png`：SHA-256 一致。
- 检查运行中的本地 Hugo server：首页已输出 WeChat 触发器、关闭按钮和二维码资源路径。

## 已知风险或未验证内容

- 当前环境没有可用的浏览器自动化组件，未自动执行真实点击、关闭和扫码测试。
- 当前环境未安装 Node.js，因此未单独运行 `node --check`；Hugo 已成功完成该脚本的 JS 构建。
- WeChat 加好友和扫码行为由用户设备上的 WeChat 客户端处理。
