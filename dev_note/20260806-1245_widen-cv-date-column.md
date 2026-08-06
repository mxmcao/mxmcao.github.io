# 加宽 CV 教育与经历时间列

## 改动背景和目标

Education 和 Experience 的日期字段在较窄桌面窗口中可能因为时间列宽度不足而换行。本次为日期分配更宽的左侧列，并强制日期保持单行，提升 CV 时间线的扫描效率。

## 修改的文件及具体内容

- `static/style.css`：将 `.cv-entry` 的时间列从最小 `8.5rem / 17%` 调整为 `11.5rem / 22%`，并为 `.cv-entry__period` 添加 `white-space: nowrap`。
- `dev_note/20260806-1245_widen-cv-date-column.md`：记录本次排版调整。

## 核心实现说明

Education 和 Experience 共用 `.cv-entry` 网格，因此同一列规则同时生效；移动端仍切换为单列布局，日期继续以完整单行显示。

## 实际执行的测试和结果

- `hugo --minify --destination <temporary-directory>`：通过。
- `git diff --check`：通过。
- 检查生成的 CV HTML：Education 和 Experience 的时间字段均保持原始完整文本。

## 已知风险或未验证内容

- 极窄移动端视口下，单行日期可能比可用宽度更长；当前日期长度在常见手机宽度下可容纳，且单列布局避免与正文争抢空间。
