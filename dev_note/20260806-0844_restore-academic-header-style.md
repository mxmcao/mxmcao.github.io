# 回退学术页标题字体与分割线

## 改动背景和目标

commit `ef275d18a51dabcd77902bb0b320e3f9c1721771` 为 Research 与 CV 引入了统一的终端式页头，但其中固定字号的标题排版与 `[+] ... [>]` 信号轨道偏离了 Hugo Terminal 主题原生页面标题。此次仅回退字体格式和分割线，保留共享页头、CV 去重 H1、Google Scholar 入口与论文排序等结构和功能。

## 修改的文件及具体内容

- `layouts/partials/academic-page-header.html`：恢复主题原生 `post-title` 标题类和标题自链接，移除 `>_` 提示符与自定义轨道节点。
- `static/style.css`：删除学术页头固定字号、提示符和信号轨道规则，恢复 Scholar 辅助文字在标题内的原有排版及移动端换行行为。

## 核心实现说明

共享 partial 继续服务 Research 与 CV，但将 H1 接回主题的 `post-title` 样式。标题字号重新继承主题 H1 规则，颜色、间距和双点线分割线重新由主题统一维护。Research 的 Scholar 文案仍作为小号辅助信息显示；CV 不传辅助链接，因此只显示标准标题。

## 关键代码摘录及对应文件路径

`layouts/partials/academic-page-header.html`：

```html
<h1 class="post-title academic-page-header__title" id="{{ .id }}">
  <a href="{{ $page.Permalink }}">{{ $page.Title | markdownify }}</a>
</h1>
```

`static/style.css`：

```css
.academic-page-header__title .publication-page__scholar {
  font-size: 0.48em;
  font-weight: normal;
}
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-academic-header-rollback-20260806-0844`：通过，生成 10 个页面、12 个静态文件和 2 个 alias。
- 检查生成的 `/research/index.html` 与 `/cv/index.html`：每页均只有一个 H1，且 H1 使用 `post-title academic-page-header__title`；Research 继续输出 Google Scholar 链接。
- 检查生成的主题 CSS：`post-title` 的双点线规则正常存在；源码和生成的站点自定义 CSS 均不再包含 academic prompt、divider、`[+]` 或 `[>]` 规则。

## 已知风险或未验证内容

- 当前环境没有 Chromium、Chrome 或 Playwright 可执行文件，未进行浏览器截图复核。
