# 优化 Preprint banner 颜色

## 改动背景和目标

Memory Decoder at Scale 的 `Preprint` banner 原先使用琥珀色。此次改为更具辨识度的深紫色，使其与现有 ICLR 蓝色、NeurIPS 红色和 Tech Report 深青色形成清晰区分，同时保持白色文字的可读性。

## 修改的文件及具体内容

- `data/publications.yaml`：将 Memory Decoder at Scale 的 banner 颜色从 `#a16207` 更新为 `#6d28d9`。

## 核心实现说明

页面模板继续使用 publication 数据中的 `venue.color` 设置 CSS 自定义属性，未引入新的样式规则或改变其他 publication 的颜色。

## 关键代码摘录及对应文件路径

`data/publications.yaml`：

```yaml
short: Preprint
color: "#6d28d9"
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-preprint-banner-stage`：通过。
- 检查生成的 Research 页面：Memory Decoder at Scale banner 输出 `--venue-color:#6d28d9`。

## 已知风险或未验证内容

- 未进行浏览器截图复核；实际显示仍会受到显示器色彩和浏览器缩放影响。
