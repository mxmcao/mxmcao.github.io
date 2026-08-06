# 解耦论文预览图路径

## 改动背景和目标

论文数据中的 `preview` 应该描述站点发布后的根路径，而不是依赖归档目录的 Hugo mount。此次将论文预览图纳入站点自己的静态资源目录，让 Research 页面在归档目录布局变化后仍能稳定引用图片。

## 修改的文件及具体内容

- `data/publications.yaml`：将两篇论文的 `preview` 改为根路径 `/images/publications/*.png`。
- `static/images/publications/mlp-memory.png`：新增站点静态资源副本。
- `static/images/publications/memory-decoder.png`：新增站点静态资源副本。
- `hugo.toml`：移除从 `prev-information/publications/images` 到 `static/images/publications` 的 module mount。

## 核心实现说明

Hugo 会自动发布 `static/images/publications/` 下的文件，模板继续通过 `relURL` 处理 `preview`，因此部署到子路径时仍能生成正确 URL。`prev-information/publications/images/` 保持原样，继续作为旧站归档，不再参与当前站点构建。

## 关键代码摘录及对应文件路径

`data/publications.yaml`：

```yaml
preview: /images/publications/mlp-memory.png
```

`hugo.toml`：删除旧归档图片目录的 module mount。

## 实际执行的测试和结果

- 使用 `sha256sum` 比对两组图片：站点副本与归档原图完全一致。
- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-publication-preview-path`：通过。
- 检查生成的 Research 页面：两个图片 URL 均为 `/images/publications/*.png`，且对应静态文件均存在。

## 已知风险或未验证内容

- 站点静态资源现在保留了归档目录之外的两份图片副本；归档原图未删除，以保持历史资料完整性。
