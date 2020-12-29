## idea-plug 笔记 (idea 插件)

### maven 插件-Maven-Helper

- 安装使用

  插件中安装 maven-helper

  然后选择 maven 项目的 pom.xml 文件

  然后会看到文件下面有个 "Dependency Analyzer",点击这个 tab

  切换到此试图即可进行相应操作：

  - Conflicts（查看冲突）
  - All Dependencies as List（列表形式查看所有依赖）
  - All Dependencies as Tree（树形式查看所有依赖）

  **冲突 jar 包的解决**

  切换到 maven 依赖视图选择冲突选项，如果有冲突，在左下面区域会有红色显示。

  解决冲突，右键单击红色区域，弹出菜单选择 Exclude 命令，对冲突进行排除。

### IDEA 有一个插件可以自动生成时序图-SequenceDiagram

- 使用

  选中方法名（注意不要选类名），然后点击鼠标右键（显示可选项），选择 Sequence Diagram

  根据弹出框，根据自己的情况，设置调用深度，点击 OK 就可以生成时序图了

  查看生成的时序图

### vim 插件

- 名称 ideaVim

- 安装

  点击 File > settings - > plugins > 搜索 vim > IdeaVim

- 配置

  ideavim 的快速打开配置文件

  在 idea 软件打开后，右下角有一个 vim 的图标，点击后，选择 `Open ~/.ideavimrc`

  即可在 idea 中打开 vim 的相关配置并进行相关的设置

  用户目录下添加配置文件 C:\Users\Administrator

  创建 .ideavimrc 文件

  不能直接创建.\*\*的文件 可以 cmd / powershell

  windows 下 配置文件 .ideavimrc 和 \_ideavimrc 均可

  ```sh
  echo a > .ideavimrc
  ```

  **注意：修改 vim 配置要生效，需要重启 idea**

  ```vim
  imap <C-e> <END>
  imap <C-a> <HOME>
  imap ll <Right>
  imap hh <Left>
  " 显示当前的模式
  set showmode
  " 共享系统粘贴板
  set clipboard=unnamed
  " 高亮显示查询结果
  set hlsearch
  " 查询不分大小写 小写全匹配，有一个大写则按照大小写规则匹配
  set ignorecase smartcase

  " 下面的配置只能在idea系列中生效
  " Leader默认的键盘位置是 \
  " 使用 \ r 相当于 idea ctrl + r
  nnoremap <Leader>r :action Replace<CR>
  " 使用 \ / 相当于 idea ctrl + f
  vnoremap <Leader>/ :action Find<CR>
  nnoremap <Leader>/ :action Find<CR>
  " 使用 \ . / 相当于 ctrl + shift + f
  vnoremap <Leader>./ :action FindInPath<CR>
  nnoremap <Leader>./ :action FindInPath<CR>
  ```

### lombok plug 安装

- idea 使用 lombok

  在插件中查找该插件并安装 lombok

  重启 idea

  安装完成后需要配置,在配置 setting 中查找

  **Annotation Processors** -> **Enable annotation processing** 是否勾选 为勾选需要勾选

  **Obtain processors from project classpath option is selected** 也需要选择

  idea 升级如果引起 lombok 不生效,则可以去[idea-github](https://github.com/JetBrains/intellij-community) 和 [lombok-intellij-plugin-github](https://github.com/mplushnikov/lombok-intellij-plugin)查找解决方案

### 查看 controller 中 RequestMapping 的插件 Request mapper

- idea 插件地址

  快速查看项目中后台路由 如 "/boot/hello/word"

  https://plugins.jetbrains.com/plugin/9567-request-mapper

- 插件安装后使用快捷键为

  `ctrl + shift + \`

### idea 代码缩略图的插件 idea 代码查看插件

- 安装使用

  File->Settings->Plugins->MarketPlace->搜索 CodeGlance 并安装

  Ctrl+Shift+G 可以显示和隐藏

  如果插件的 idea 缩略图看不见了，可以配置 ： 在 file -> settings -> search :codeglance -> 去掉 disable 选项

### 字节码增强插件 jclasslib

- 安装使用

  File->Settings->Plugins->MarketPlace->搜索 jclasslib 并安装

  代码编译后在菜单栏”View”中选择”Show Bytecode With jclasslib”，可以很直观地看到当前字节码文件的类信息、常量池、方法区等信息。

### 正则测试插件 regex-tester

- 安装使用

  在插件中查找该插件并且安装。
