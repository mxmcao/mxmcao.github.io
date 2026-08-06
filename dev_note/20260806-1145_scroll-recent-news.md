# 滚动显示近期新闻

## 改动背景和目标

首页 Recent news 当前会直接展开全部新闻，随着历史记录增加会占用过多纵向空间。此次沿用旧版 `$ tail -n 3 news.log` 的终端视觉语言，改为 `$ head -n 5 news.log`，只展示最新五条，并将内容放入可滚动区域。

## 修改的文件及具体内容

- `layouts/shortcodes/home-profile.html`：在新闻列表上方加入 `$ head -n 5 news.log` 命令提示；使用 Hugo `first 5` 取最新五条，并包裹可键盘聚焦的滚动区域。
- `static/style.css`：增加命令提示、固定最大高度、纵向滚动、滚动条预留空间和键盘焦点样式。
- `dev_note/20260806-1145_scroll-recent-news.md`：记录实现和验证结果。

## 核心实现说明

`data/news.yaml` 已按日期从新到旧排列，因此 `first 5 site.Data.news` 会得到最新五条。滚动容器使用 `max-height: 14rem` 和 `overflow-y: auto`，不改变新闻条目的原有日期/正文布局；`tabindex="0"` 让键盘用户可以聚焦并滚动新闻区域，`aria-label` 为区域提供语义名称。

## 关键代码摘录及对应文件路径

`layouts/shortcodes/home-profile.html`：

```html
<p class="console-command news-console-command" aria-hidden="true">$ head -n 5 news.log</p>
<div class="news-list__viewport" role="region" aria-label="Recent news" tabindex="0">
  {{ range first 5 site.Data.news }}
```

`static/style.css`：

```css
.news-list__viewport {
  max-height: 14rem;
  overflow-y: auto;
  scrollbar-gutter: stable;
}
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-news-scroll-stage`：通过。
- 检查生成首页：命令提示为 `$ head -n 5 news.log`，新闻条目数量为 5，滚动容器包含 `role="region"`、`tabindex="0"` 和 `max-height: 14rem` 样式。

## 已知风险或未验证内容

- 当前环境未进行浏览器截图复核；滚动条的具体外观会随浏览器和操作系统而变化。
