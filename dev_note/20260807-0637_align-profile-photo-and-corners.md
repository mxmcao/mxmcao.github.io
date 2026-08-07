# 对齐主页头像与 terminal 四角标记

## 改动背景和目标

主页头像与四个 terminal 角标存在垂直错位。原因是主题全局 `img` 规则默认添加 `25px 0` 外边距，而角标相对头像 `figure` 容器定位，导致图片实际起点低于上方角标、下方角标也远离图片边缘。

## 修改的文件及具体内容

- `static/style.css`：为 `.home-profile__portrait img` 显式设置 `display: block` 和 `margin: 0`，覆盖主题图片默认外边距。
- `dev_note/20260807-0637_align-profile-photo-and-corners.md`：记录错位原因、实现和验证结果。

## 核心实现说明

图片移除上下 `25px` 默认外边距后，头像的上、下边缘直接与 `figure` 内容边界对齐。四个以 `top`/`bottom: -0.45rem` 定位的角标将与图片保持一致的外侧间距，无需分别调整图片和下方标记的位置。

## 实际执行的测试和结果

- `hugo --minify --destination <temporary-directory>`：通过。
- `git diff --check`：通过。
- 检查生成首页：头像及四个 `.home-profile__corner` 元素均存在。

## 已知风险或未验证内容

- 角标仍刻意保留 `0.45rem` 的外侧偏移，以维持 terminal 取景框效果；如希望角标直接贴在图片边缘，可将对应的 `top`、`right`、`bottom`、`left` 值改为 `0`。
