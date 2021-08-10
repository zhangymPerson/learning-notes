# spacevim 的使用

## 介绍和安装

- [spacevim](https://spacevim.org/cn/)

- 安装指南

  在安装 SpaceVim 之前，你需要确保电脑上已经安装了 Git 和 cURL。这两个工具用来 下载插件以及字体。

  如果在终端中使用 Vim 或 Neovim，还需要设置终端的字体。

- Linux 或 macOS

  `curl -sLf https://spacevim.org/cn/install.sh | bash`

  安装结束后，初次打开 Vim 或者 gVim 时，SpaceVim 会自动下载并安装插件。

  如果需要获取安装脚本的帮助信息，可以执行如下命令，包括定制安装、更新和卸载等。

  `curl -sLf https://spacevim.org/cn/install.sh | bash -s -- -h`

- Windows

  Windows 下最快捷的安装方法是下载安装脚本 install.cmd 并运行。

- 注意事项 如果不能连接外网 github 需要使用代理地址

  修改 install.sh 文件中的 github 地址 为 hub.fastgit.org 注意改动范围，别全部替换。
