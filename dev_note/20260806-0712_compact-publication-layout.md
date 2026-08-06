# 压缩论文列表与 banner 布局

## 改动背景和目标

Research 页面中单篇论文的字号、预览图占比和纵向留白偏大，导致论文数量增加后页面过长。首页求职 banner 和论文 venue banner 也需要更紧凑，以提升信息密度。

## 修改的文件及具体内容

- `static/style.css`：缩小论文列表字号、行高、预览图列宽、条目 padding、按钮尺寸和年份分组间距。
- `static/style.css`：缩小论文 venue banner 的字号、padding 和阴影。
- `static/style.css`：缩小首页求职 banner 的字号、纵向 padding、间距和外边距。
- `static/style.css`：在移动端限制论文预览图最大宽度，并缩短图片与正文之间的间距。

## 核心实现说明

桌面端论文预览图列从列表宽度的 32% 降至 25%，正文获得更多横向空间，可减少作者列表换行。论文条目使用 `0.88rem` 字号和 `1.38` 行高，并同步压缩标题、元信息、资源按钮和条目上下留白，从多个来源降低单篇论文的实际高度。

移动端继续使用单列布局，但将预览图最大宽度从 `420px` 降至 `340px`，避免窄屏下图片重新成为主要纵向占用。

## 关键代码摘录及对应文件路径

`static/style.css`：

```css
.publication-item {
  grid-template-columns: minmax(180px, 25%) minmax(0, 1fr);
  padding: 0.7rem 0 0.95rem;
  font-size: 0.88rem;
  line-height: 1.38;
}

.job-banner {
  padding: 0.55rem 0.8rem;
  font-size: 0.86em;
  line-height: 1.4;
}
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-compact-publications`：通过，生成 10 个页面、11 个静态文件和 2 个 alias。
- 检查生成的 `/research/index.html`：两篇论文、venue banner、作者、资源按钮和引用数均正常输出。
- 检查生成的 `/index.html`：求职 banner 正常输出。
- 检查生成的 `/style.css`：紧凑后的 publication、venue banner 和 job banner 样式均已进入构建产物。

## 已知风险或未验证内容

- 最终视觉密度仍会受到浏览器字体渲染和用户默认缩放比例影响。
- 当前环境没有可用的浏览器运行时，未执行桌面端和移动端截图复核。
