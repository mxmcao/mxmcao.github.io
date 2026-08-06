# 强化首页 Terminal 区块样式

## 改动背景和目标

上一版首页区块只使用低对比度细顶线和短强调色线，在实际页面中分割不够明显，Terminal 视觉语言也偏弱。此次重新设计区块边界，在不恢复 `$ cat ...` 等伪命令标题的前提下，让页面具有更鲜明的终端界面特征。

## 修改的文件及具体内容

- `static/style.css`
  - 将首页区块改为强调色顶边、左侧轨道和虚线底边组成的开放式 Terminal frame。
  - 在区块左上角和右下角增加方形端点，强化边界起止位置。
  - 为首页主标题增加 `>` 前缀，为二级标题增加静态 `>_` prompt 和延伸虚线。
  - 为研究方向列表、联系方式标签和 News 日期增加轻量终端输出标记。
  - 调整移动端区块 padding、标题间距和标题轨道最小宽度。

## 核心实现说明

新版不使用圆角、阴影或独立卡片背景。区块通过三边开放式框线区分，保持页面布局通透；所有边界直接使用 `var(--accent)`，在亮色和暗色主题下均保持可见。

标题内容仍为标准的 `h1` 和 `h2` 文本，`>` 与 `>_` 仅通过 CSS 伪元素展示，不进入文档结构，也不模拟具体 shell 命令。

## 关键代码摘录及对应文件路径

`static/style.css`：

```css
.home-profile__block {
  padding: 1.5rem 0 2rem 1.5rem;
  border-top: 2px solid var(--accent);
  border-bottom: 1px dashed var(--accent);
  border-left: 2px solid var(--accent);
}

.home-profile__block h2::before {
  color: var(--accent);
  content: ">_";
}

.home-profile__block h2::after {
  flex: 1 1 auto;
  border-top: 1px dashed var(--accent);
  content: "";
}
```

## 实际执行的测试和结果

- 执行 `git diff --check`：通过，没有空白符错误。
- 执行 `hugo --minify --destination /tmp/mxmcao-terminal-frame-check`：通过，生成 10 个页面和 11 个静态文件。
- 检查生成的首页 HTML：Profile、Research、Connect 和 News 四个区块均保留 `home-profile__block` 类和正常标题层级。
- 检查生成的 `style.css`：Terminal frame、`>_` prompt、标题虚线轨道和移动端覆盖规则均存在。

## 已知风险或未验证内容

- 当前环境没有可用的浏览器自动化组件，无法生成桌面端和移动端截图。
- 视觉强度仍会受到用户显示器对比度和浏览器缩放比例影响，但新版不再依赖低对比度的 `--border` 作为主要分割线。
