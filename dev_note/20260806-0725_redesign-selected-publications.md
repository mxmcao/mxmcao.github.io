# 重做 Selected Publications 页面

## 改动背景和目标

上一版仅缩小了论文卡片内部间距，页面仍受主题默认大标题、年份块和卡片式图片布局影响，单篇论文的纵向占用仍然偏高。本次将页面改为高密度论文列表，并增加 Google Scholar 全部论文入口。

## 修改的文件及具体内容

- `content/research.md`：页面标题改为 `Selected Publications`，指定论文页专用 layout。
- `layouts/_default/research.html`：增加紧凑标题行，并在标题后以小字链接 Google Scholar 全部论文列表。
- `layouts/shortcodes/publications.html`：移除重复大标题，将 equal-contribution 说明合并到列表底部。
- `static/style.css`：重做年份、缩略图、论文信息、venue banner、资源按钮和页脚的高密度布局。
- `static/style.css`：移动端保持小缩略图横排，避免重新变成占据大块纵向空间的单列图片。

## 核心实现说明

论文页面使用独立 Hugo layout，绕开主题单页默认的双虚线标题和 `25px` 内容顶部间距。标题与 Scholar 入口在同一行展示。

年份变为 `3.1rem` 的左侧窄列，论文主体使用 `140px + 1fr` 双栏。单篇论文只保留 `0.5rem` 上下 padding，并使用细虚线区分条目。预览图固定为 `2.5:1`，venue banner、作者、venue 名称和资源按钮分别使用更小的稳定字号。

## 关键代码摘录及对应文件路径

`layouts/_default/research.html`：

```html
<h1 id="selected-publications-heading">{{ .Title }}</h1>
<p class="publication-page__scholar">
  All publications on <a href="...">Google Scholar</a>.
</p>
```

`static/style.css`：

```css
.publication-item {
  grid-template-columns: 140px minmax(0, 1fr);
  padding: 0.5rem 0;
  font-size: 0.75rem;
  line-height: 1.25;
}
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-selected-publications`：通过，生成 10 个页面、11 个静态文件和 2 个 alias。
- 检查生成的 `/research/index.html`：只保留一个 `Selected Publications` 标题；Google Scholar 全部论文链接、两篇论文、资源按钮、等贡献说明和引用更新时间均正常输出。
- 检查本地预览 `http://127.0.0.1:1313/research/`：标题、Scholar 链接和紧凑样式已由 Hugo live reload 生效。
- 检查生成与预览中的 `style.css`：桌面论文条目为 `140px + 1fr`，条目 padding 为 `0.5rem`，venue banner 与资源按钮均采用紧凑尺寸。

## 已知风险或未验证内容

- 当前环境没有可用的浏览器自动化组件，未执行桌面端和移动端截图复核。
