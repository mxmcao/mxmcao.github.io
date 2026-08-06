# 简化首页 Terminal 区块边界

## 改动背景和目标

首页上一版将每个内容区块做成三边强调色 frame，并加入两个方形端点。虽然 Terminal 识别度明显，但外围框线过强，使页面显得像一组独立面板。此次改为更轻量的终端输出流布局。

## 修改的文件及具体内容

- `static/style.css`
  - 删除 `home-profile__block` 的顶边、左边、底边、定位和额外内边距。
  - 删除区块左上角与右下角的伪元素端点。
  - 删除移动端仅为外围框预留的内边距。
  - 保留区块垂直间距、标题的 `>_` prompt、标题右侧虚线轨道，以及内容级的 Terminal 输出标记。

## 核心实现说明

首页从多个“终端窗口”转为单一的连续输出流。每个内容段落仍以标题 prompt 和虚线轨道明确开始，研究列表、联系方式和新闻条目继续保持输出格式；但正文不再被颜色框线包围，因此视觉重心回到个人内容和学术信息。

## 关键代码摘录及对应文件路径

`static/style.css`：

```css
.home-profile__block {
  margin-top: 3.75rem;
}

.home-profile__block h2::before {
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
- 执行 `hugo --minify --destination /tmp/mxmcao-terminal-flow-check`：通过，生成 10 个页面和 11 个静态文件。
- 检查生成的 `style.css`：已不存在 `home-profile__block::before` 和 `home-profile__block::after` 外围 frame 规则，`>_` prompt 与标题虚线轨道仍然存在。
- 检查运行中的 `http://127.0.0.1:1313/style.css`：与生成结果一致，Hugo live reload 已读取修改后的样式文件。

## 已知风险或未验证内容

- 当前环境没有可用的浏览器自动化组件，最终的留白密度需通过本地浏览器预览确认。
