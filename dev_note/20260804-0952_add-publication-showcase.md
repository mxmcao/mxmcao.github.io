# 增加带图片与 venue banner 的论文展示

## 改动背景和目标

Research 页面原本只有占位文本。本次恢复旧站两篇论文的真实元数据和预览图，保留图片上的 NeurIPS/ICLR banner，并结合 John Math Research 页面的年份分组与紧凑资源按钮。

## 修改的文件及具体内容

- `content/research.md`：改为渲染论文 shortcode，并保留 `/publications/` 兼容地址。
- `data/publications.yaml`：集中保存论文、作者、venue、图片和外部资源链接。
- `layouts/shortcodes/publications.html`：按年份渲染论文列表。
- `layouts/partials/publication-buttons.html`：按数据条件渲染 arXiv、Code、Hugging Face 等按钮。
- `static/style.css`：增加论文双栏布局、venue banner、终端风格按钮和移动端布局。

## 核心实现说明

论文页使用一份 Hugo Data 数据作为单一信息源。预览图片通过上一阶段配置的 Hugo mount 从归档目录发布；venue 色彩和链接保留旧站设置。桌面端图片在左、信息在右，移动端自动切换为单列。

## 关键代码摘录及对应文件路径

`layouts/shortcodes/publications.html`：

```html
<a class="publication-venue" style="--venue-color: ...">
  {{ .venue.short }} {{ .venue.year }}
</a>
```

`layouts/partials/publication-buttons.html`：

```html
{{ with .arxiv }}
  <a class="publication-button publication-button--arxiv" href="{{ . }}">arXiv</a>
{{ end }}
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-research-stage`：通过，生成 10 个页面和 11 个静态文件。
- 检查两个 `/images/publications/*.png`：归档论文图片已通过 mount 发布。
- 检查生成的 `/research/index.html`：包含 2026/2025 年份分组、两篇论文、venue banner、作者、资源按钮和 equal-contribution 说明。
- 检查 `/publications/index.html`：旧地址 alias 已生成。

## 已知风险或未验证内容

- 论文元数据目前由 `data/publications.yaml` 手工维护；新增论文时需要更新该文件。
- 作者姓名当前只突出显示 Jiaqi Cao，没有启用作者主页自动链接。
