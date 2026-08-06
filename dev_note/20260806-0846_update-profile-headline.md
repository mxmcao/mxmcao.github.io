# 更新首页个人 headline

## 改动背景和目标

将 About 首页头像旁的身份描述更新为当前实习职位。

## 修改的文件及具体内容

- `data/profile.yaml`：将 `headline` 从 `LLM Researcher at Shanghai Jiao Tong University` 更新为 `Pre-train Intern @ IQuest Research`。

## 核心实现说明

首页 `home-profile` shortcode 从 `site.Data.profile.headline` 读取该字段，因此无需修改模板。现有 affiliation `LUMIA Group` 保持不变，并继续显示在 headline 后方。

## 关键代码摘录及对应文件路径

`data/profile.yaml`：

```yaml
headline: Pre-train Intern @ IQuest Research
```

## 实际执行的测试和结果

- 执行 `git diff --check`：通过，没有空白符错误。
- 执行 `hugo --minify --destination /tmp/mxmcao-headline-check`：通过，生成 10 个页面和 12 个静态文件。
- 检查生成首页：已输出 `Pre-train Intern @ IQuest Research`。
- 检查运行中的 `http://127.0.0.1:1313/`：已同步新的 headline。

## 已知风险或未验证内容

- 此次只修改页面可见 headline，没有同步修改站点 SEO description 或其他个人简介段落。
