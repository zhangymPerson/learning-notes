# idea-plug 笔记 (idea 插件)

## 目录

- [返回](./README.md)

### maven 插件-Maven-Helper

- 安装使用

  插件中安装 maven-helper

  然后选择 maven 项目的 pom.xml 文件

  然后会看到文件下面有个 "Dependency Analyzer",点击这个 tab

  切换到此试图即可进行相应操作：

  - Conflicts（查看冲突）
  - All Dependencies as List（列表形式查看所有依赖）
  - All Dependencies as Tree（树形式查看所有依赖）

  冲突 jar 包的解决

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

### lombok plug 安装 (idea 自带)

### 查看 controller 中 RequestMapping 的插件 apifox

- idea 插件地址

  <https://plugins.jetbrains.com/plugin/20549-apifox-helper>

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

### 快速定位代码块的插件 Rainbow Brackets

- 安装使用

  在插件中查找安装

  用法 1:Ctrl+右键单击，高亮显示所选代码块

  用法 2:Alt+右键单击，其他全部为灰色，突出显示选中代码块

### 快速查找分析日志插件 Grep Console

- 安装使用

  在插件中查找安装

  在日志输出区域点击右键进行相关操作和查看

### MyBatisCodeHelper Pro

- mybatis 插件,免费版本够用了
