# 加强学术页标题分割线

## 改动背景和目标

Research 与 CV 页头已经采用终端提示符加单条全宽点线，但原来的 `1px` muted 点线在页面中辨识度不足。此次在不改变页头结构、字体和移动端布局的前提下，提高分割线的视觉重量，并继续使用主题强调色保持终端风格一致。

## 修改的文件及具体内容

- `static/style.css`：将 `.academic-page-header__title` 的底部点线从 `1px dotted var(--border)` 调整为 `2px dotted var(--accent)`。

## 核心实现说明

分割线仍直接绘制在共享 H1 的底边，主题原生的第二条点线继续通过 `::after { display: none; }` 禁用，因此 Research 与 CV 都只保留一条全宽分割线。使用 `var(--accent)` 与页头 `>` 提示符共享颜色，提升识别度而不引入新的颜色变量或额外 DOM。

## 关键代码摘录及对应文件路径

`static/style.css`：

```css
.academic-page-header__title {
  border-bottom: 2px dotted var(--accent);
  color: var(--foreground);
}
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-academic-header-divider-20260806-0955`：通过，生成站点页面。
- 检查生成的 Research 与 CV 页面：两页均只有一个 H1，且共享 `>` 提示符和单条 `2px dotted var(--accent)` 分割线。

## 已知风险或未验证内容

- 当前环境未进行浏览器截图复核；实际点线密度可能随浏览器缩放比例略有变化。
