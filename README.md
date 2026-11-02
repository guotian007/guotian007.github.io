# TinySky 个人主页

原生 HTML/CSS 静态主页，适用于 GitHub Pages，无需安装依赖。

本地预览：`python3 -m http.server 4387 --bind 127.0.0.1`

GitHub Pages：Settings → Pages → Deploy from a branch → main → / (root)。

## 中文排版

标题：思源宋体 Light（300），最大 64px；正文：思源宋体 Regular（400）。导航和按钮保留思源黑体。英文保持原有 Georgia 与系统无衬线字体搭配。

网页字体按当前页面文字生成子集，并更名为 TinySky Han Serif / TinySky Han Sans。新增中文文案时需要重新生成子集。

- 思源宋体源文件：https://github.com/adobe-fonts/source-han-serif/blob/release/Variable/WOFF2/TTF/Subset/SourceHanSerifCN-VF.ttf.woff2
- 思源黑体源文件：https://github.com/adobe-fonts/source-han-sans/blob/release/Variable/WOFF2/TTF/Subset/SourceHanSansCN-VF.ttf.woff2
- 宋体授权：SERIF-FONT-LICENSE.txt；黑体授权：FONT-LICENSE.txt。

宋体子集可通过 `subset_serif.py <原始字体文件>` 重新生成，需要 Python 的 fonttools 和 brotli。
