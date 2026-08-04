# 恢复首页个人信息与 Console 风格

## 改动背景和目标

Hugo Terminal 迁移后的首页仍是占位内容。本次从 `prev-information/` 归档恢复真实个人信息、头像、联系方式和 News，并加入位于 News 列表上方的求职状态 banner。视觉上借鉴 Hugo Theme Console 的静态终端提示符，不加入命令输入或其他交互终端功能。

## 修改的文件及具体内容

- `hugo.toml`：更新站点元数据和斜杠式导航；配置归档头像与论文图片的 Hugo mounts。
- `content/_index.md`：用首页 shortcode 替换占位内容。
- `data/profile.yaml`：保存个人介绍、研究兴趣、联系方式及求职状态。
- `data/news.yaml`：保存三条真实学术动态。
- `layouts/shortcodes/home-profile.html`：渲染首页结构。
- `static/style.css`：增加静态 Console 提示符、头像、联系方式、News 和响应式样式。

## 核心实现说明

首页内容与模板分离，个人信息集中由 `data/profile.yaml` 管理。头像使用 Hugo mount 从归档文件发布，不创建重复的二进制副本。顶部 `mxmcao:~#` 和各节 `$ cat ...` 只承担视觉语义，不接受用户输入。

## 关键代码摘录及对应文件路径

`layouts/shortcodes/home-profile.html`：

```html
<p class="console-command" aria-hidden="true">$ cat about.md</p>
<h1 id="about-heading">Hi, I'm {{ $profile.name }}.</h1>
```

`hugo.toml`：

```toml
[[module.mounts]]
  source = "prev-information/personal/profile.png"
  target = "static/images/profile.png"
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-home-stage`：通过，生成 10 个页面和 11 个静态文件。
- 检查 `/tmp/mxmcao-home-stage/images/profile.png`：头像 mount 已正确发布。
- 检查生成的 `index.html`：包含个人介绍、Console 导航、求职 banner、Recent News 和完整头像尺寸属性。

## 已知风险或未验证内容

- `weixin://` 链接依赖访问设备安装微信。
- 本次沿用归档中的毕业时间和求职文案，后续状态变化时需更新 `data/profile.yaml`。
