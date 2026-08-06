# 增加 Nanbeige 4.2 与 Memory Decoder at Scale

## 改动背景和目标

Research 页面需要展示两项新的近期工作：Nanbeige 4.2 和 Memory Decoder at Scale。此次复用现有论文卡片结构，使用用户提供的预览图，并为两个条目增加准确的论文、项目和模型链接。

## 修改的文件及具体内容

- `data/publications.yaml`：新增两个 2026 publication；Nanbeige 作者按要求只显示 `Core Contributor`，Memory Decoder at Scale 显示论文作者列表并突出 Jiaqi Cao。
- `hugo.toml`：将根目录 `images/` 挂载到 `static/images`，使现有预览图以 `/images/publications/` URL 发布。
- `dev_note/20260806-1145_add-publications-nanbeige-memory-decoder-scale.md`：记录来源、实现和验证结果。

## 核心实现说明

Nanbeige 条目使用 `Tech Report` banner 和深青色 `#0f766e`；Memory Decoder at Scale 使用 `Preprint` banner 和琥珀色 `#a16207`。两种颜色与现有 ICLR 蓝色和 NeurIPS 红色区分，同时保持白色文字的对比度。

Nanbeige 元数据来自 [arXiv:2607.22083](https://arxiv.org/abs/2607.22083) 和 [Nanbeige4.2-3B 模型卡](https://huggingface.co/Nanbeige/Nanbeige4.2-3B)。Memory Decoder at Scale 元数据来自 [arXiv:2607.27919](https://arxiv.org/abs/2607.27919)；代码、模型和项目页分别链接到 [GitHub 仓库](https://github.com/LUMIA-Group/MemoryDecoder-at-Scale)、[Hugging Face collection](https://huggingface.co/collections/Rubin-Wei/memorydecoder-at-scale) 和 [项目主页](https://rubin-wei.github.io/memory-decoder-at-scale/)。

## 关键代码摘录及对应文件路径

`data/publications.yaml`：

```yaml
- id: nanbeige-4-2
  venue:
    short: Tech Report
    color: "#0f766e"
  authors:
    - name: Core Contributor

- id: memory-decoder-at-scale
  venue:
    short: Preprint
    color: "#a16207"
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-publications-stage`：通过。
- 检查生成的 Research 页面：2026 年分组包含 Nanbeige 4.2、Memory Decoder at Scale 和 MLP Memory 三个条目。
- 检查生成 HTML：两个新增预览图 URL 分别为 `/images/publications/nanbeige-4.2.png` 和 `/images/publications/memdec-at-scale.png`，对应文件均存在。
- 检查生成 HTML：Nanbeige 作者只输出 `Core Contributor`；Memory Decoder at Scale 输出 7 位作者并突出 Jiaqi Cao。

## 已知风险或未验证内容

- 新增条目没有配置 `scholar_id`，因此当前不会显示 Google Scholar 引用按钮，也不会参与引用数快照更新。
- Nanbeige 的公开报告作者列表较长，页面按需求使用简化署名 `Core Contributor`。
