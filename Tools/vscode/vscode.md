# vscode 笔记

- [返回](./README.md)

## 快捷键

- 常用的

  ```sh
  #vscode折叠代码快捷键
  ctrl+k,ctrl+0 (数字0)

  #展开所有代码的快捷键
  ctrl+k,ctrl+j

  #隐藏资源管理器(即文件目录列表)
  ctrl + b

  #快速打开终端和调试窗口
  ctrl + ` (Esc键下面那个键)

  #选中多行
  #按住Alt键点击左键 多选  或者 Alt+Shift键 鼠标左键上下移动多选

  #vscode 1.43.0版本中可以通过菜单栏 点击 - 选择 - 列选择模式 即可开启列选择模式

  #快速查询 替换
  ctrl + f / ctrl + h  (可以进行正则查询替换)

  #查看搜索打开目录下的所有的文件
  ctrl+p

  #打开控制台
  ctrl+shift+p或者 F1

  #打开文件所在文件夹 资源管理器
  #右键 - reveal in explorer
  shift + alt + R

  ```

## 其他配置

- 自动换行

  文件  -> 首选项 -> 设置 -> 编辑器- > 找到控制折行方式。

  可以选择：

  - "off" （禁用折行），
  - "on" （视区折行），
  - "wordWrapColumn"（在"editor.wordWrapColumn"处折行）
  - "bounded"（在视区与"editor.wordWrapColumn"两者的较小者处折行）。 "editor.wordWrap": "off",

- 配置 VS code 显示方式 (空格和 table 的显示方式)

  editor.renderWhitespace : all

- 配置阿里普惠体

  Alibaba Sans

  Alibaba Sans, 'Courier New', monospace

- 配置 JetBrains Mono 字体

  在 file - > preferences -> settings -> search "font family" ->

  修改为 JetBrains Mono, 'Courier New', monospace

## vscode 的远程连接方式

- 插件下载

  Remote Development

  Visual Studio Code Remote 允许开发者将容器，远程计算机，或 Windows Subsystem for Linux (WSL) 作为完整的开发环境。

- 配置相关参数

  ~\.ssh\config

  ```config
  Host Person
      HostName host
      User     root
  ```

  配置文件后，将 ssh 的公钥复制到要连接的服务器中

  **注意**

  - Host 是指别名，你给服务器起的名称
  - HostName 是你的服务器地址 如果 hosts 文件中有别名，可以用别名，没有则必须使用 ip 地址
  - User 用户名 即你的 ssh 连接指定的用户

  然后连接

  vscode 有多个服务器需要远程连接的时候，可以直接查看[ssh 笔记](https://github.com/zhangymPerson/learning-notes/tree/master/Tools/OpenSSH)中的多服务器配置 配置多个服务器

## 使用问题记录

- vscode 字体配置

  微软开源字体

  ```
  Cascadia Code, 'Courier New', monospace
  ```

- vscode 打开 git 日志乱码 中文文件名乱码

  windows 系统下问题

  git status 中文转义致乱码的 解决方案

  在 Git Bash 提示符下输入：

  ```sh
  git config --global core.quotepath false
  ```

  core.quotepath 设为 false 的话，就不会对 0x80 以上的字符进行 quote。中文显示正常。

- vscode 安装 nodejs 代码联想工具

  `npm install -g typings` `typings --version` 常用命令

  ```sh
  # 安装Typings的命令行代码.
  npm install typings --global

  # 搜索对应模块的typings定义.
  typings search tape

  # 根据名称寻找一个可获得的typings定义.
  typings search --name react

  # 如果你用一个独立包的模块:
  # 或者并不是安装全局模块
  # 比如并不是在命令行通过输入npm install -g typings这种方式安装的.
  typings install debug --save

  # 如果是通过script标记
  # 或者是子环境的一部分
  # 或者全局typings命令不可用的时候：
  typings install dt~mocha --global --save

  # 从其他版本处安装typings定义(比如env或者npm).
  typings install env~atom --global --save
  typings install npm~bluebird --save

  # 安装 node提示
  typings install dt~node --global --save

  # 使用该文件`typings/index.d.ts` (在`tsconfig.json`文件使用或者用 `///` 定义).
  cat typings/index.d.ts
  ```

- vscode 中的函数进入退出快捷键

  进入函数详情 ctrl + 鼠标左键

  退回到点击位置 alt + < 右键

- vscode tab 键空格不为 4 个的修改方式

  点击 vscode 右下角 Spaces:n 或者 空格:n (n 为数字) 修改成你需要的长度

- vscode 多行变一行

  按 F1 或者 ctrl+shift+p 输入 Join Lines 回车即可

- vscode 格式化 markdown 使用 Prettier 插件时，换行的问题

  配置 settings : prettier.printWidth 配置一个较大的数字。格式化完成后，恢复默认

- mac 下配置 vscode 快速打开

  F1 -> 输入 code ->  选择Shell Command : Install 'code' command in PATH
