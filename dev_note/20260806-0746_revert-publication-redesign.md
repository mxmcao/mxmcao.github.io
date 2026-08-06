# 回退过度压缩的论文页面重做

## 改动背景和目标

Selected Publications 重做版本将论文页面压缩得过于紧凑，影响阅读舒适度。本次回退该版本，恢复至上一版较平衡的论文展示密度。

## 修改的文件及具体内容

- `content/research.md`：恢复页面标题和默认单页 layout。
- `layouts/_default/research.html`：移除 Selected Publications 专用模板。
- `layouts/shortcodes/publications.html`：恢复原有标题、每篇论文的等贡献说明和引用更新时间文本。
- `static/style.css`：恢复前一版论文预览图、正文、venue banner、资源按钮与移动端布局尺寸。
- `dev_note/20260806-0725_redesign-selected-publications.md`：删除已回退版本的改动记录。

## 核心实现说明

本次使用 Git 反向提交回退 `f9ee28e`，没有改写历史，也不影响之后独立提交的首页样式和 GitHub Actions 工作流改动。

## 关键代码摘录及对应文件路径

`static/style.css`：

```css
.publication-item {
  grid-template-columns: minmax(180px, 25%) minmax(0, 1fr);
  padding: 0.7rem 0 0.95rem;
  font-size: 0.88rem;
}
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-publication-rollback`：通过，生成 10 个页面、11 个静态文件和 2 个 alias。
- 检查生成的 `/research/index.html`：恢复 `Research` 与 `Publications` 标题、两篇论文、等贡献说明和引用更新时间。
- 检查生成的 `/style.css`：恢复前一版 `minmax(180px, 25%)` 预览图列、`0.7rem 0 0.95rem` 条目 padding 和前一版按钮尺寸。
- 检查本地预览 `http://127.0.0.1:1313/research/`：Hugo live reload 已恢复上一版页面标题和布局。

## 已知风险或未验证内容

- 本次回退恢复的是前一版紧凑布局，而非论文展示功能引入前的初始布局。
