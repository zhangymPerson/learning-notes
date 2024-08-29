# markdown 导出工具

- [返回](./README.md)

## vscode 自带预览/导出有插件

## typora 软件自带导出

## 带导航的工具

## markdown 转 word 工具

### 工具 markdown 转 word 插件 writage

- [writage 官网](https://www.writage.com/)

- 使用

  官网直接下载安装,然后在 word 中打开原生 markdown 文件 ,然后另存为 word 文件即可

### pandoc 工具 [github](https://github.com/jgm/pandoc)

- 安装

  去 `github` [https://github.com/jgm/pandoc](https://github.com/jgm/pandoc) 下载安装包

- 简单使用 markdown 转 word

  `pandoc a.md -o a.docx`

- 支持的 pdf 引擎 
  
  `wkhtmltopdf`

  [weasyprint](https://github.com/Kozea/WeasyPrint) 引擎支持的种类多，能导出各种复杂的文档需要安装 `python` `pip install weasyprint` 

  `pagedjs-cli`

  `prince`

  `pdflatex`

  `lualatex`

  `xelatex`

  `latexmk`

  `tectonic`

  `pdfroff`

  [typst](https://github.com/typst/typst) 引擎

  `context`

  `pandoc -o test.pdf --pdf-engine=xelatex`
