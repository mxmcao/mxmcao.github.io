# 整理头像生成设计方案

## 改动背景和目标

当前个人网站采用 Hugo Terminal 的终端式视觉。用户希望将此前讨论的头像风格方案统一落盘，并删除所有彩色点缀设计，使后续头像生成严格使用黑、白和中性灰。

## 修改的文件及具体内容

- `prev-information/avatar/avatar-gen-guide.md`：新增完整头像生成指南，整理输入素材、统一约束、八种设计方向、可复制 prompt、迭代模板、选择排序和验收清单。
- `dev_note/20260805-0526_document-avatar-generation-designs.md`：记录本次文档改动、验证结果与未验证内容。

## 核心实现说明

指南将 `avatar-1.png` 定义为首选身份参考，将 `avatar-2.png` 定义为可选侧面构图参考。所有方案共用高身份保真、方形构图、小尺寸清晰度和无色相单色灰阶约束。

八种方向包括技术杂志线描、单色丝网印刷、极简钢笔、终端抖动像素、木刻版画、纯灰阶编辑摄影、现代学术档案雕刻和深色学术雕刻。其中现代学术档案雕刻为首选，但明确要求保持机构中立，不复制奖项品牌，也不添加奖章、月桂或标识。

## 关键代码摘录及对应文件路径

`prev-information/avatar/avatar-gen-guide.md`：

```text
Color palette: Strict achromatic monochrome only: pure black, pure white, and neutral gray. Overall saturation must be zero.
```

```text
Constraints: Change only the visual rendering style. Preserve identity with high fidelity.
```

## 实际执行的测试和结果

- 检查 Markdown 结构：标题层级、代码围栏、表格和任务清单完整。
- 检索颜色表述：prompt 中只允许纯黑、纯白和中性灰，不包含任何彩色点缀方案。
- `git diff --check`：通过，无空白错误。
- 本次仅新增文档，没有修改网站模板、CSS、配置或线上头像资源。

## 已知风险或未验证内容

- 尚未调用图像生成工具，因此没有验证各 prompt 的实际输出稳定性。
- 尚未把任何候选头像放入 Hugo 页面进行桌面端、移动端和明暗主题截图比较。
- 后续生成结果仍需按指南中的 `220 x 220 px` 验收清单人工检查身份相似度。
