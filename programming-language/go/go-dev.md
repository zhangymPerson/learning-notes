## go 的 vscode 开发

- 安装 go 插件

  vscode 的插件库中查找 `go` 。找到第一个微软官方的 go 插件安装即可

- 安装 go 的 tool

  使用快捷键：command+shift+P，然后键入：go:install/update tools，将所有 16 个插件都勾选上，然后点击 OK 即开始安装。

  go 插件部分需要科学上网 或者配置公开的镜像源进行下载安装

  使用 `F1` 键 也可以有类似的作用

- go 语言 vscode 配置 test

  在 vscode 中 找到 settings 配置位置 搜索 `Go:Test Tags` 修改此项，加入 `-v`

- 镜像安装失败 则需要配置国内的源

  配置方法 见 [README.md](./README.md#go语言的国内代理配置)
