# Gitbook的搭建和使用

## 简介

- [官网](https://www.gitbook.com/)

- [百度百科](https://baike.baidu.com/item/GitBook/17969908?fr=aladdin)

    GitBook 是一个基于 Node.js 的命令行工具，可使用 Github/Git 和 Markdown 来制作精美的电子书，GitBook 并非关于 Git 的教程。

- 安装

    gitbook 依赖于 nodejs

    安装命令 `npm install gitbook-cli -g`

- 使用

    `gitbook -V` 检查安装是否成功

    创建book文件夹 并进入文件夹

    gitbook init 

    gitbook build 只创建页面文件(html)

    gitbook serve 提供服务 默认接口 4000