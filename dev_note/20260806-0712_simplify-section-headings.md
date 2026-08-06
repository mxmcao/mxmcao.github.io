# 简化页面区块标题

## 改动背景和目标

首页原先使用 `$ cat research-interests.md`、`$ finger mxmcao` 等模拟终端命令作为标题前缀。此次改动移除这些命令式文案，只保留正常的页面标题，同时通过克制的边界和强调色维持 Terminal 风格，并让各内容区块之间更容易区分。

## 修改的文件及具体内容

- `layouts/shortcodes/home-profile.html`
  - 删除 Profile、Research、Connect 和 News 区块的模拟终端命令。
  - 为四个首页区块统一添加 `home-profile__block` 类。
- `layouts/shortcodes/publications.html`
  - 删除 Publications 标题上方的 `$ ls publications/` 命令，保持站内标题规则一致。
- `static/style.css`
  - 删除不再使用的 `.console-command` 样式。
  - 为首页区块增加细顶部边界、短强调色线和统一内边距。
  - 调整桌面端与移动端的区块间距。

## 核心实现说明

区块仍然是无外框、无阴影的页面内容，不使用卡片式容器。每个区块顶部使用一条低对比度细线，其中左侧短段使用主题强调色；配合等宽字体和方正布局保留 Terminal 气质，同时避免重复的命令提示符和文件名。

首个 Profile 区块不增加额外顶部外边距，避免首页首屏内容下沉。后续区块保留较大的垂直间距，在移动端缩小间距和左内边距。

## 关键代码摘录及对应文件路径

`layouts/shortcodes/home-profile.html`：

```html
<section class="home-profile__block" aria-labelledby="interests-heading">
  <h2 id="interests-heading">Research interests</h2>
</section>
```

`static/style.css`：

```css
.home-profile__block {
  position: relative;
  margin-top: 3.5rem;
  padding: 1.5rem 0 0 1.25rem;
  border-top: 1px solid var(--border);
}

.home-profile__block::before {
  position: absolute;
  top: -1px;
  left: 0;
  width: 3.5rem;
  height: 2px;
  background: var(--accent);
  content: "";
}
```

## 实际执行的测试和结果

- 执行 `hugo --minify --destination /tmp/mxmcao-site-check`：通过，生成 10 个页面和 11 个静态文件。
- 执行 `git diff --check`：通过，没有空白符错误。
- 搜索 `console-command` 及原有 `$ cat`、`$ finger`、`$ tail`、`$ ls` 文案：无残留。

## 已知风险或未验证内容

- 当前环境没有可用的浏览器自动化组件，未生成桌面端和移动端截图；需在可访问的本地预览或 GitHub Pages 预览中进行最终视觉确认。
- 此次仅调整标题和区块边界，没有修改页面内容、数据文件或主题色。
