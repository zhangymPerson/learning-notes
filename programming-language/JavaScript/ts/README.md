# Ts开发

- [菜鸟教程](https://www.runoob.com/typescript/ts-tutorial.html)

## 安装ts
- 安装ts (需要先安装nodejs 和 npm)

    全局安装ts `npm install -g typescript`

- 测试安装成功命令

    `tsc -v`

## vscode 下开发配置

- 创建新开发的文件夹

- 初始化项目

    命令`tsc --init` 它会给我们创建一个tsconfig.json的文件，初始化一个项目目录。

- 配置相关设置

    在tsconfig.json 中做一下修改：`"outDir": "./js"` 
    指定ts文件输入位置
    
    为了避免每次都用命令生成js 可以配置vscode监听任务
    
    vscode ->任务->运行任务->监视tsconfig.json

- 编写ts文件，即可实时编译成js文件了