# 统一 Publications 与 CV 的学术页标题

## 改动背景和目标

About 页面使用终端式 `>` 与 `>_` 标记组织身份和内容区块，而 Publications 与 CV 仍使用 Hugo 主题默认的博客双虚线标题；CV 还存在页面标题和正文 `# CV` 的重复。此次统一学术内容页标题语言，同时保留 Publications 的 Scholar 入口。

## 修改的文件及具体内容

- `layouts/partials/academic-page-header.html`：新增可复用的学术页标题 partial。
- `layouts/_default/academic.html`：新增 CV 等通用学术内容页 layout。
- `layouts/_default/research.html`：改为复用标题 partial，继续仅在论文页加载排序脚本。
- `content/cv.md`：使用 academic layout，移除重复的正文 H1，并更新页面描述。
- `static/style.css`：新增统一标题样式和终端信号轨道分割线。

## 核心实现说明

学术页标题采用 `>_` 前缀、标准 H1、可选的小号辅助链接和自定义分割线。分割线由 `[+]`、虚线信号轨道、轨道节点和 `[>]` 组成，延续终端主题但避免复用博客文章的双重虚线。

Research 通过 partial 传入 Google Scholar 链接；CV 使用同一标题骨架但没有辅助链接。两页因此共享视觉语法，同时仍保留内容上的差异。

## 关键代码摘录及对应文件路径

`layouts/partials/academic-page-header.html`：

```html
<span class="academic-page-header__prompt" aria-hidden="true">&gt;_</span>
<h1 class="academic-page-header__title">{{ $page.Title }}</h1>
<div class="academic-page-header__divider" aria-hidden="true"><span></span></div>
```

`static/style.css`：

```css
.academic-page-header__divider::before { content: "[+]"; }
.academic-page-header__divider::after { content: "[>]"; }
.academic-page-header__divider span { border-top: 1px dashed currentColor; }
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-academic-headers`：通过，生成 10 个页面、11 个静态文件和 2 个 alias。
- 检查生成的 `/research/index.html`：仅有一个 `Selected Publications` H1，标题后正常输出 Google Scholar 链接和 academic header 分割线。
- 检查生成的 `/cv/index.html`：仅有一个 `CV` H1，不再输出正文 `# CV`；academic header 分割线正常存在。
- 检查生成的 `/style.css`：`[+]`、虚线轨道、信号节点和 `[>]` 分割线规则已进入构建产物，移动端辅助信息会换行显示。

## 已知风险或未验证内容

- 当前环境没有浏览器自动化组件，未执行截图复核；以 Hugo 构建和生成 HTML/CSS 检查为主。
