# 优化首页 headline 字体

## 改动背景和目标

首页的职位与 affiliation 原先完全继承 Terminal 主题的等宽正文字体，与个人简介缺少层级差异。初版 `0.88rem` 字号在实际预览中偏小，此次改用更接近正文大小的学术编辑风格字体，并将职位与机构合并为单个 headline 字段。

## 修改的文件及具体内容

- `static/style.css`
  - 为 `.home-profile__headline` 设置 Georgia/Cambria 系统 serif 字体栈。
  - 将字号固定为 `0.96rem`，使用轻斜体与 `1.45` 行高。
  - 将 letter spacing 明确保持为 `0`。
  - 为 headline 内的 IQuest 链接保留主题强调色，并使用更细、偏离文字的下划线。
- `layouts/shortcodes/home-profile.html`
  - 仅渲染一个支持 Markdown 的 headline，不再拼接独立 affiliation 字段。
- `data/profile.yaml`
  - 将职位、`@` 和带链接的 IQuest 机构名合并进单个 headline。

## 核心实现说明

页面主体继续使用 Fira Code，完整 headline 行使用 serif italic，形成克制的字体对比。headline 通过 Markdown 保存 IQuest 链接，模板和数据层不再区分职位与 affiliation。字体全部来自现有主题或操作系统，不增加 Web Font、网络请求或构建依赖。

## 关键代码摘录及对应文件路径

`static/style.css`：

```css
.home-profile__headline {
  font-family: Georgia, Cambria, "Times New Roman", Times, serif;
  font-size: 0.96rem;
  font-style: italic;
  line-height: 1.45;
  letter-spacing: 0;
}
```

## 实际执行的测试和结果

- `git diff --check`：通过，未发现空白符错误。
- `hugo --minify --destination /tmp/mxmcao-headline-unified-check`：通过，共生成 10 个页面并处理 12 个静态文件。
- 检查生产构建结果与本地实时页面：均输出合并后的 `Pre-train Researcher @ IQuest`，IQuest 链接指向 `https://github.com/IQuestLab`。
- 检查页面样式：headline 使用 `0.96rem` serif italic 字体，不再包含 affiliation 或独立 `@` 的渲染逻辑。

## 已知风险或未验证内容

- 系统字体在 macOS、Windows 和 Linux 上会略有差异，但均保留 serif italic 的设计意图。
- 当前环境没有浏览器自动化组件，未生成跨平台字体渲染截图。
