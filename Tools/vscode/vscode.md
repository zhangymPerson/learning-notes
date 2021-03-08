# vscode 笔记

## 插件

- Chinese (Simplified) Language Pack for Visual Studio Code

- CodeBing

  查询插件 - 使用方式 alt + shift + f 或者控制台输入 Bing

- Git History

  git 日志查看插件 - 右键文件 选择 git history 即可

- **Git File History**

  git 文件修改历史查看便捷神器插件 直观查看 git 对文件的修改历史 使用方式 ctrl + shift + p 然后输入命令 Git File History 可以动态查看文件 git 提交记录

- **Git History Diff**

  git 文件查看插件，会在鼠标所在行显示修改历史

- **Prettier - Code formatter**

  代码格式化插件，最重要的是能格式化 markdown

- vscode-icons

  这个也是 vscode 官方提供的插件，作用是给 vscode 编辑的文件增加图标。这里再推荐一个相同功能的插件**vscode-icons-mac**，文件图标变成 Mac 风格，相当美观。

- vim 插件

- 括号插件 Bracket Pair Colorizer

  这个插件的作用是给代码中的括号增加颜色，同一对括号是相同的颜色，尤其是在括号中还包着括号的时候，看起来更加的清晰。

- 路径自动补全 Path Intellisense

  这个插件的作用是当代码中读入文件名或者文件路径时，提供文件名或者文件路径的自动补全

- Beautify 代码美化

- [vscode-快捷键说明文档](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

- vscode 中制作流程图的插件 - Draw.io Integration

  [Draw.io](https://app.diagrams.net/)

  vscode 中安装插件之后，可以在本地进行相关图形的绘制

  如 [draw-png.drawio](./draw-png.drawio)

- [REST Client](https://github.com/Huachao/vscode-restclient)

  http 测试工具插件测试 api.的插件通过文件来发现和测试 [测试文件](./restclient.http)

- vscode 自动代码提示补全插件工具

  TabNine 智能代码补全插件

  **Postfix Completion** (下称 Postfix) 是一种通过 . + 模板 Key 来对当前已经输出的表达式，添加和应用预设代码模板的编码增强能力。

  idea 自带的代码自动补全相关功能 vscode 需要搜索查询相关插件

  其核心要解决的问题是，将编码过程中一些通用的代码结构范式进行抽象和沉淀，并能在同类型的场景下，通过 . + 模板 Key 的方式进行唤醒和复用。

- vscode 错误信息在当前行显示的插件 error lens

  [github - error lens](https://github.com/usernamehw/vscode-error-lens)

- [vscode-翻译插件 search-online](https://github.com/Wscats/search-online)

  [中文使用说明](https://gitee.com/wscats/search-online/blob/master/README.CN.md)

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
