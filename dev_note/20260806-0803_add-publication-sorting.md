# 为 Selected Publications 增加 Scholar 入口和排序

## 改动背景和目标

在保持上一版论文卡片密度不变的前提下，将 Research 页面明确定位为精选论文页，并让访问者能按年份或引用数查看相同的论文集合。

## 修改的文件及具体内容

- `content/research.md`：页面标题改为 `Selected Publications`，指定论文页专用 layout。
- `layouts/_default/research.html`：在标题后增加小号 Google Scholar 全部论文链接，并仅加载本页排序脚本。
- `layouts/shortcodes/publications.html`：增加 `Year` 和 `Citations` 分段排序控件、引用数数据属性以及 citation 视图容器。
- `assets/js/publication-sort.js`：实现按引用数降序排序，并在切回年份时还原原始年份分组与顺序。
- `static/style.css`：增加标题辅助文字与排序控件样式，不调整现有论文卡片的尺寸和密度。

## 核心实现说明

年份模式直接使用 Hugo 生成的年份分组。切换到引用模式时，脚本移动同一组论文 DOM 节点到平铺列表，按引用数降序、年份降序和原始顺序排序；切回年份模式时按原始父列表恢复。该方式不会复制论文内容或产生重复 ID。

## 关键代码摘录及对应文件路径

`assets/js/publication-sort.js`：

```js
items
  .slice()
  .sort((left, right) => citationCount(right) - citationCount(left))
  .forEach((item) => citationList.append(item));
```

`layouts/_default/research.html`：

```html
<span class="publication-page__scholar">
  All publications on <a href="...">Google Scholar</a>.
</span>
```

## 实际执行的测试和结果

- `git diff --check`：通过，无空白错误。
- `hugo --gc --minify --cleanDestinationDir --destination /tmp/mxmcao-publication-sorting`：通过，生成 10 个页面、11 个静态文件和 2 个 alias。
- 检查生成的 `/research/index.html`：包含 `Selected Publications` 标题、Google Scholar 全部论文链接、`Year / Citations` 控件和本页指纹化排序脚本。
- 检查排序数据属性：MLP Memory 为 `data-publication-year="2026" data-publication-citations="19"`，Memory Decoder 为 `data-publication-year="2025" data-publication-citations="16"`。
- 检查本地预览 `http://127.0.0.1:1313/research/`：标题、Scholar 链接和排序控件已由 Hugo live reload 生效。

## 已知风险或未验证内容

- Citation 排序使用构建时 `data/citations.yaml` 中的引用数；需运行现有引用更新脚本后才会反映最新数据。
- 当前环境没有 Node 或浏览器运行时，未执行自动化点击排序测试；Hugo 的 `js.Build` 已成功解析并打包该脚本。
