# 保留滚动新闻的完整历史

## 改动背景和目标

上一版滚动 Recent News 使用 `first 5`，虽然限制了首页高度，但也把第 6 条及更早的历史新闻从页面中移除了。此次修正为保留全部新闻数据，让“最多显示五条”只表示滚动窗口的可视容量。

## 修改的文件及具体内容

- `layouts/shortcodes/home-profile.html`：将新闻列表从 `range first 5 site.Data.news` 改为 `range site.Data.news`，滚动区域继续使用固定最大高度。
- `dev_note/20260806-1229_keep-full-news-history.md`：记录本次行为修正和验证结果。

## 核心实现说明

`data/news.yaml` 仍按日期从新到旧排列，最新新闻位于滚动窗口顶部；`news-list__viewport` 的 `max-height: 14rem` 和 `overflow-y: auto` 控制可视区域，用户可以滚动查看全部历史条目。顶部命令 `$ head -n 5 news.log` 保留为“默认查看最新五条”的终端提示。

## 关键代码摘录及对应文件路径

`layouts/shortcodes/home-profile.html`：

```html
<div class="news-list__viewport" role="region" aria-label="Recent news" tabindex="0">
  <ol class="news-list">
    {{ range site.Data.news }}
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-news-history-stage`：通过。
- 检查生成首页：新闻条目数量与 `data/news.yaml` 全部条目一致（当前为 7 条），命令提示和滚动区域语义保持不变。

## 已知风险或未验证内容

- 当前环境未进行浏览器截图复核；滚动条的具体外观会随浏览器和操作系统而变化。
