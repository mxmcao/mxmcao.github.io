# Refine terminal header styling

## 改动背景和目标

顶部命令行已经替代原有渐隐分割线，但命令文字偏小、偏细。此次提高文字辨识度，并在闪烁光标后保留渐隐 rail，使 terminal 命令和页面顶部的横向结构同时成立。

## 修改文件

- `layouts/partials/header.html`：在光标后增加 `header__terminal-rail`。
- `static/style.css`：使用主题已有的 `Fira Code` 字体，提高字号和字重，增加渐隐线以及移动端尺寸适配。

## 核心实现

```css
.header__terminal {
  font-family: "Fira Code", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  font-size: 0.94rem;
  font-weight: 600;
}
```

渐隐线作为独立 flex 子项放在 cursor 后面，不参与命令文字的省略；命令文字在窄屏下优先收缩，光标和 rail 保持稳定尺寸。

## 测试

- `hugo --minify --destination <temporary-directory>`：通过。
- 检查 About、Research、CV 生成 HTML：命令、光标和 rail 结构均存在。

## 已知风险

`Fira Code` 由当前 terminal theme 提供。如果以后更换主题且不再加载该字体，将自动回退到系统等宽字体。
