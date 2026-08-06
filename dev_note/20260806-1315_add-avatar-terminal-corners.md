# 添加头像四角 terminal 标记

## 改动背景和目标

头像原先使用完整的绿色实线边框，视觉重量较高。本次改为更轻量的 terminal 四角标记，保留终端识别度，同时让头像主体更自然地融入页面。

## 修改的文件及具体内容

- `layouts/shortcodes/home-profile.html`：在头像图片上添加四个装饰性 corner 元素，分别对应四个角。
- `static/style.css`：移除头像完整边框；使用四个绝对定位的 L 形标记覆盖头像四角，利用透明强调色降低视觉重量。
- `dev_note/20260806-1315_add-avatar-terminal-corners.md`：记录本次头像装饰调整。

## 核心实现说明

每个 corner 元素绘制一个相邻角线：例如左上角使用 `border-width: 2px 0 0 2px`，右下角使用 `border-width: 0 2px 2px 0`。角线颜色为 `color-mix(in srgb, var(--accent) 58%, transparent)`，不会形成完整外围框。

## 实际执行的测试和结果

- `hugo --minify --destination <temporary-directory>`：通过。
- `git diff --check`：通过。
- 检查生成的 About HTML：头像仍使用 `/images/profile/chosen-one.png`。

## 已知风险或未验证内容

- 四角标记通过伪元素叠加在图片外侧，极窄视口下可能需要进一步减小偏移量。
