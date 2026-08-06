# 优化 WeChat 二维码弹窗视觉

## 改动背景和目标

首版 WeChat 二维码弹窗宽度较小，并使用强调色外框，视觉上偏紧凑和生硬。此次适当放大二维码，并用柔和阴影和背景虚化取代外框。

## 修改的文件及具体内容

- `static/style.css`
  - 将弹窗最大宽度从 `260px` 提升到 `320px`。
  - 删除弹窗强调色边框。
  - 增加轻微圆角、柔和阴影和半透明背景。
  - 为页面遮罩增加半透明黑色背景和 `8px` 模糊。
  - 为弹窗自身增加 `16px` 背景模糊，使其与遮罩过渡更自然。

## 核心实现说明

二维码原图、弹窗结构和交互逻辑保持不变。使用 `backdrop-filter` 和 `-webkit-backdrop-filter` 同时覆盖现代 Chromium/Firefox 与 Safari；不支持背景模糊的浏览器仍会显示半透明遮罩和弹窗阴影。

## 关键代码摘录及对应文件路径

`static/style.css`：

```css
.wechat-dialog {
  width: min(20rem, calc(100vw - 2rem));
  border: 0;
  box-shadow: 0 18px 55px color-mix(in srgb, #000 35%, transparent);
  backdrop-filter: blur(16px);
}

.wechat-dialog::backdrop {
  background: color-mix(in srgb, #000 42%, transparent);
  backdrop-filter: blur(8px);
}
```

## 实际执行的测试和结果

- 执行 `git diff --check`：通过，没有空白符错误。
- 执行 `hugo --minify --destination /tmp/mxmcao-wechat-visual-check`：通过，生成 10 个页面和 12 个静态文件。
- 检查生成的 `style.css`：弹窗宽度为 `20rem`、`border: 0`，包含弹窗 `16px` blur 和遮罩 `8px` blur。
- 检查运行中的 `http://127.0.0.1:1313/style.css`：已同步相同规则。

## 已知风险或未验证内容

- 当前环境没有可用的浏览器自动化组件，未生成 blur 效果的实际截图。
- 不支持 `backdrop-filter` 的旧浏览器会退化为半透明遮罩，不影响二维码查看和弹窗交互。
