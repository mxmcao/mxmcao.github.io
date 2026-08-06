# 简化学术页标题分割线

## 改动背景和目标

Research 与 CV 在恢复 Hugo Terminal 原生页头后使用两条 `3px` 点线，视觉重量仍然偏高。此次采用“终端提示符 + 单条全宽点线”方案，在保留主题标题字号和页面结构的前提下，降低分割线存在感，并与首页已经使用的 `>` 视觉语言保持一致。

## 修改的文件及具体内容

- `layouts/partials/academic-page-header.html`：在共享 H1 中加入对辅助技术隐藏的 `>` 提示符，并为标题链接增加专用 class。
- `static/style.css`：将学术页标题底边覆盖为一条 `1px` muted 点线，关闭主题生成的第二条点线，并设置提示符和标题颜色。

## 核心实现说明

页头继续保留 `post-title` class，因此字号、外边距和底部留白仍跟随 Hugo Terminal 主题。自定义样式只覆盖颜色和分割线：提示符使用 `var(--accent)`，标题使用 `var(--foreground)`，点线使用 `var(--border)`。点线直接绘制在全宽 H1 的底边，不增加额外布局节点。

装饰性的提示符使用 `aria-hidden="true"`，不会干扰读屏软件读取页面标题。Google Scholar 辅助链接及其移动端换行规则保持不变。

## 关键代码摘录及对应文件路径

`layouts/partials/academic-page-header.html`：

```html
<span class="academic-page-header__prompt" aria-hidden="true">&gt;</span>
<a class="academic-page-header__title-link" href="{{ $page.Permalink }}">
  {{ $page.Title | markdownify }}
</a>
```

`static/style.css`：

```css
.academic-page-header__title {
  border-bottom: 1px dotted var(--border);
}

.academic-page-header__title::after {
  display: none;
}
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-academic-header-divider-20260806-0856`：通过，生成 10 个页面、12 个静态文件和 2 个 alias。
- 使用 `xmllint` 检查生成页面：Research 与 CV 各只有一个 H1，两个标题均包含内容为 `>`、`aria-hidden="true"` 的提示符；Research 继续包含一个 Google Scholar 链接。
- 检查生成 CSS 与样式表顺序：自定义 `1px dotted var(--border)` 和 `::after { display: none; }` 均已输出，且 `/style.css` 在主题 `post.css` 之后加载，可以覆盖原生双点线。

## 已知风险或未验证内容

- 当前环境没有 Chromium、Chrome 或 Playwright 可执行文件，未进行浏览器截图复核。
