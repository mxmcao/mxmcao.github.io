# mxmcao.github.io

A minimal academic homepage built with Hugo and [hugo-theme-terminal](https://github.com/panr/hugo-theme-terminal).

## Requirements

- Hugo Extended 0.90.0 or newer
- Go 1.19 or newer

The repository currently pins Terminal theme `v4.2.3` through Hugo Modules.

## Local development

```bash
hugo server
```

Open <http://localhost:1313/>. To include draft content, run `hugo server -D`.

## Production build

```bash
hugo --gc --minify --cleanDestinationDir
```

The generated site is written to `public/`, which is intentionally ignored by Git.

## Content and data

- `content/_index.md` renders the academic profile, job-search banner, and news from `data/profile.yaml` and `data/news.yaml`.
- `content/research.md` renders publications from `data/publications.yaml`; publication images remain preserved under `prev-information/` and are exposed through Hugo mounts.
- `data/citations.yaml` is the fallback Google Scholar snapshot. Validate it locally with `python scripts/update_scholar_citations.py --check`.
- `prev-information/` remains the read-only archive of the previous al-folio site and its personal/academic source material.

## Deployment

Pushes to `main`, manual runs, and the weekly schedule trigger `.github/workflows/hugo.yml`. The workflow attempts to refresh Google Scholar citation counts, falls back to the committed snapshot on failure, builds the site, and deploys the `public/` artifact to GitHub Pages. The repository's Pages source must be set to **GitHub Actions**.

## Jupyter Lab 使用

只有 JupyterLab 端口时，推荐使用 jupyter-server-proxy，把 Hugo 的 1313 端口挂到 JupyterLab 地址下面。我检查过，当前环境尚未安装该扩展。

### 1. 在 JupyterLab Terminal 中安装

```bash
python -m pip install jupyter-server-proxy
```

安装后需要从平台界面重启整个 Jupyter 实例，仅刷新浏览器不够。

### 2. 确定公开的 Jupyter 地址

假设浏览器中的 JupyterLab 地址是：

```text
https://你的域名/siflow/changliu/jupyter/skyinfer/yshi02/jupyter-cpu/lab
```

那么代理地址就是：

```text
https://你的域名/siflow/changliu/jupyter/skyinfer/yshi02/jupyter-cpu/proxy/1313/
```

### 3. 重启后运行 Hugo

在 JupyterLab Terminal 执行，注意把“你的域名”换成浏览器地址里的实际域名：

```bash
cd /volume/yshi02/projects/mxmcao.github.io

hugo server \
  --bind 127.0.0.1 \
  --port 1313 \
  --appendPort=false \
  --liveReloadPort 443 \
  --baseURL "https://你的域名/siflow/changliu/jupyter/skyinfer/yshi02/jupyter-cpu/proxy/1313/"
```

然后访问：

```text
https://你的域名/siflow/changliu/jupyter/skyinfer/yshi02/jupyter-cpu/proxy/1313/
```

保持运行 Hugo 的终端不要关闭，修改网页文件后会自动重新构建。停止预览时按 Ctrl+C。

如果你把当前 JupyterLab 的浏览器地址发给我（Token 可以删掉），我可以直接帮你拼好完整命令和预览地址。
