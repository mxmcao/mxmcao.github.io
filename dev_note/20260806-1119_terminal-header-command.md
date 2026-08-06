# Terminal header command

## 改动背景和目标

顶部 logo 右侧原本是渐隐分割线。将其替换为简短的 terminal 命令和闪烁光标，并让 About、Research、CV 页面分别显示不同命令。

## 修改文件

- `data/terminal_prompts.yaml`：保存各页面的命令文案。
- `layouts/partials/header.html`：根据当前页面文件名选择命令并输出光标结构。
- `static/style.css`：增加 monospace 命令样式、块状光标和闪烁动画；移动端缩小光标和字号。

## 核心实现

```go
{{- $terminalCommand := index site.Data.terminal_prompts $promptKey | default site.Data.terminal_prompts.home -}}
```

当前命令为 `whoami`、`cd research` 和 `less cv`。命令区域作为装饰内容使用 `aria-hidden`，不会干扰屏幕阅读器导航；用户启用减少动画时光标停止闪烁。

## 测试

- `hugo --minify --destination <temporary-directory>`
- `git diff --check`（headline 数据中的 Markdown 强制换行空格除外）

## 已知风险

页面识别依赖 content 文件名 `research.md` 和 `cv.md`。如果以后改名，需要同步更新 `data/terminal-prompts.yaml` 或 header 的 key 选择逻辑。
