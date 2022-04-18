# vscode 笔记

- [返回](./README.md)

## vscode 检索 搜索 技巧

- vscode 全局搜索 ctrl + shift +f

- 搜索文件 ctrl + p

- 在 ctrl + p 下

  - 输入 '@' 当前文件内检索

  - 输入 '#' 搜索项目的函数变量名等内容

## 快捷键

- 常用的 vscode 快捷键

  ```sh
  # vscode折叠代码快捷键
  ctrl + k,ctrl + 0 (数字0)

  # 展开所有代码的快捷键
  ctrl + k ,ctrl + j

  # 隐藏资源管理器(即文件目录列表)
  ctrl + b

  # 快速打开终端和调试窗口
  ctrl + ` (Esc键下面那个键)

  #  vscode 回退上一步 退回上一个编辑位置
  ctrl + -
  ```

  ```sh
  # 选中多行
  # 按住Alt键点击左键 多选  或者 Alt+Shift键 鼠标左键上下移动多选

  # vscode 1.43.0版本中可以通过菜单栏 点击 - 选择 - 列选择模式 即可开启列选择模式

  # 快速查询 替换
  ctrl + f / ctrl + h  (可以进行正则查询替换)

  # 查看搜索打开目录下的所有的文件
  ctrl + p

  # 查看某个文件中的变量和函数
  ctrl + p 然后输入 @varname 或者 @methodname

  # 打开控制台
  ctrl + shift + p 或者 F1

  # 打开文件所在文件夹 资源管理器
  # 右键 - reveal in explorer
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

  ```conf
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

  F1 -> 输入 code -> 选择 Shell Command : Install 'code' command in PATH

- vscode 打开文件乱码

  打开“settings”，在搜索框搜索“encoding”，勾选“Files: Auto Guess Encoding”，免得每次都要手动调整编码方式。

- vscode 中的终端乱码问题 terminal 乱码

  setting.json 里面增加

  ```json
  {
    "terminal.integrated.env.linux": {
      "LC_ALL": "zh_CN.UTF-8"
    }
  }
  ```

- vscode 终端输出行数配置

  settings -> terminal.integrated.scrollback 将此数值 1000 根据自己需求改大

- vscode 进程 kill-vscode 进程

  查询某个关键字的进程号

  ps aux|grep vscode|awk '{print $2}'

  **下面的命令需要带 \` 符号**

  kill -s 9 \`ps aux|grep vscode|awk '{print $2}'\`

- vscode json 注释问题 注释飘红

  打开 json 文件,在 vscode 的右下角，选择文件的语言模式 选择 json with comments , json 注释就不飘红了

- vscode 配置文件默认模式 如 \*.json 为 jsonc

  点击 vscode 右下角的文件模式类型，如 Markdown,c++,java,json 等，然后 Configure 'json' language

  按 F1，在帮助菜单中输入 'Configure File Association for '

- vscode tab 多了换行配置 标签页换行设置

  打开 settings 搜索 `wrap tabs` 选中，则 tab 满了会自动换行

- vscode 只有一个 tab 窗口

  打开 setting 搜索 `show tab` 选中第一个 `show tabs`

- vscode 单击预览，双击打开，预览文件倾斜显示，打开的文件正常显示 文件覆盖问题 标签覆盖问题

  配置方式 打开 settings 文件 搜索 `enable preview`

  把`Enable Preview和Enable Preview From Quick Open` 都勾选上，则可以单击预览文件

- vscode 配置标尺辅助线

  防止一行代码过长的问题

  配置 `"editor.rulers": [80, 120]`

- vscode 代码片段 snippets

  单语言 代码片段配置 setting > 搜索 snippets > 单击要选择的语言进行配置

  全局代码片段配置 setting > 搜索 snippets > 选则 > global \*\*\* 进行配置
