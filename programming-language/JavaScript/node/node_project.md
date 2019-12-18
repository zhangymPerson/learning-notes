# node 项目结构

## 目录

|文件路径|说明|其他|
|-|-|-|
|bin|项目的启动文件，也可以放其他脚本
|node_modules|用来存放项目的依赖库
|public|用来存放静态文件(css,js,img)
|routes|路由控制器
|views|视图目录(相当于MVC中的V)
|app.js|项目入口及程序启动文件
|package.json|包描述文件及开发者信息


## 初始化一个nodejs项目

- 命令

    `node init`

## nodejs project git过滤

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

- [文档首页](https://docsite.js.org/zh-cn/docs/installation.html)

    阿里巴巴开源的nodejs展示markdown笔记的工具