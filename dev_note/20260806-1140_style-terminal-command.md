# Style terminal command text

## 改动背景和目标

命令行文字此前使用较小、较细的等宽字体，并接近前景色。此次将文字改成 accent 色和更具装饰性的衬线斜体，同时保持 terminal 光标与渐隐 rail 的结构。

## 修改文件

- `static/style.css`：调整 `.header__terminal` 的颜色、字体、字号、字重和字距。

## 核心实现

```css
.header__terminal {
  color: var(--accent);
  font-family: "Baskerville", "Iowan Old Style", Georgia, Cambria, "Times New Roman", Times, serif;
  font-size: 0.98rem;
  font-style: italic;
  font-weight: 700;
}
```

字体优先使用系统中的 Baskerville/Iowan Old Style；其他平台会回退到 Georgia 或 Times。命令、光标和渐隐 rail 仍通过原有 terminal header 结构呈现。

## 测试

- `hugo --minify --destination <temporary-directory>`：通过。
- `git diff --check`：通过。

## 已知风险

不同操作系统是否安装 Baskerville 或 Iowan Old Style 不一致；未安装时会使用 serif 回退字体，版式仍可用但字形会有所差异。
