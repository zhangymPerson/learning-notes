# node 项目结构

## 目录

| 文件路径     | 说明                             | 其他 |
| ------------ | -------------------------------- | ---- |
| bin          | 项目的启动文件，也可以放其他脚本 |      |
| node_modules | 用来存放项目的依赖库             |      |
| public       | 用来存放静态文件(css,js,img)     |      |
| routes       | 路由控制器                       |      |
| views        | 视图目录(相当于 MVC 中的 V)      |      |
| app.js       | 项目入口及程序启动文件           |      |
| package.json | 包描述文件及开发者信息           |      |

## 初始化一个 nodejs 项目

- 命令

  `npm init`

## nodejs project git 过滤

- .gitignore 文件配置

  ```.gitignore
  *.iml
  node_modules/
  tmp/
  temp/
  *.log
  .DS_Store
  npm-debug.log
  .idea
  coverage
  test/docsite-project
  package-lock.json
  ```

- .npmignore 文件配置

  ```gitignore
  node_modules/
  .travis.yml
  *.swp
  .DS_Store
  .idea
  npm-debug.log
  coverage
  test
  ```

## nodejs 博客系统


- [docsite-阿里开源博客展示]

  阿里巴巴开源的 nodejs 展示 markdown 笔记的工具

  [网址首页](https://docsite.js.org/zh-cn/index.html)

  [github地址](https://github.com/txd-team/docsite)

- [vuepress 博客系统](https://www.vuepress.cn/)

  [vuepress-github 地址](https://github.com/vuejs/vuepress)

  [说明文档](https://www.vuepress.cn/)
