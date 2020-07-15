## idea 添加 external tool 命令

- 菜单栏->「File」->「Settings」->「Tools」->「External Tools」->点击加号

## idea 的字符串模板功能

- 快捷键操作过程 创建 json 字符模板

  输入代码`String str = "";`

  焦点定位到双引号里面，使用 `Alt+Enter`

  快捷键弹出 `inject language or reference`

  选择字符模板语言

  焦点定位到双引号里面，再次使用 `Alt+Enter` 快捷键

  可以看到`Edit JSON Fragment` 选择

  可以看到编辑 JSON 文件的视图

  编辑`json`

- 取消字符模板

  使用 `Alt+Enter` 快捷键

  选择 `un-inject language....` 那个选项就可以取消字符模板了

* 涉及到的相关配置

  setting -> keymap -> alt enter

  setting -> intentions -> 下各语言相关配置

  setting -> 搜索 `inject` 选中相关的配置 不选则在字符串中按快捷键 alt + enter 无任何提示
