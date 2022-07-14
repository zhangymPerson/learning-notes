# emacs 简单使用

## 目录

- [返回](../README.md)

- **[emacs 国内社区](https://emacs-china.org/)**

- 使用教程

  [github](https://github.com/emacs-china/Spacemacs-rocks)

## 配置文件说明

Windows 下 Emacs 就按如下方式来查找配置文件：

- 如果设置了 HOME 环境变量，那么就用它的值作为 home 目录~
- 如果存在注册表键值 HKCU\SOFTWARE\GNU\Emacs\HOME，就用它的值作为 home 目录~
- 如果存在注册表键值 HKLM\SOFTWARE\GNU\Emacs\HOME，就用它的值作为 home 目录~（和 2 的区别是，2 只是针对当前用户的注册表路径，3 则是针对所有用户）
- 如果存在 C:\.emacs，就用 C:\作为 home 目录~
- 如果以上都不存在的话，就使用<system root>\Users\<user name>\AppData\Roaming 作为 home 目录~（对于 XP 和较早 windows 用户，需要到 Documents and Settings 目录下去找）

## 安装

- 安装网址:<http://ftp.gnu.org/gnu/emacs/>

## 常用体验

- 打开退出

  ```sh
  #打开文件
  emacs filename
  #退出
  # windows 下 ctrl + x ctrl + c
  ```

- 移动

  ```sh
  #向下移动
  ctrl + v
  # 向上移动 alt 在xshell中需要配置
  # File => Properties => Terminal => Keyboard => Use ALT key as Meta key
  alt + v
  # 移动当前行到屏幕中间
  ctrl + l

  # n next 下一行 p previous 上一行 b backward 回退 f forward 前进
  #下一行
  ctrl + n
  #上一行
  ctrl + p
  # 向前
  ctrl + b
  #向后
  ctrl + f
  ```

- 失去响应

  ctrl + g 终止一条执行时间太长得命令

- backspace 在 linux 终端中得问题 被映射成 ctrl + h

  在~/.emacs 中添加下面两句话：

  ```emacs
  (global-set-key "\C-h" 'backward-delete-char-untabify)
  (global-set-key "\d" 'delete-char)
  ```

- 显示行号

  `Alt + x linum-mode`

- 获取帮助

  Emacs 是一个富文档编辑器（Self document, extensible editor）而下面的三种方法在学 习 Emacs 的过程中也非常重要。他们分别是，

  - C-h k 寻找快捷键的帮助信息
  - C-h v 寻找变量的帮助信息
  - C-h f 寻找函数的帮助信息

- lisp 代码体验

  ```lisp
  ;; This buffer is for text that is not saved, and for Lisp evaluation.
  ;; To create a file, visit it with C-x C-f and enter text in its buffer.
  ;;简单函数
  ;;在 emacs buffers下 新建 *scratch*
  ;; 执行lisp代码的方式 光标在要执行的括号后面 然后 ctrl + x ctrl +e
  ;;执行结果在 下面的栏中显示
  (+ 22 22)
  ;;注释
  (+ 2 (* 3 4))
  ;;设置变量 name = emacs
  ;;调用系统函数 message  类似print()函数
  (setq name "emacs")
  (message "heollo %s" name)

  ;;定义函数
  (defun funOne ()(
          message "hello word"))
  ;;调用函数
  (funOne)

  ;;查看函数
  ```

- 插件管理

  使用默认的插件管理系统（可在菜单栏 Options > Manage Emacs Packages 中找到）

  点击 Company 插件 然后在 help 页面中 点击 install，

  是一个用于代码补全的插件。它的名字代表补全一切的意思（ Comp lete Any thing）。

  使用的下面的配置将 Company-mode 在全局模式下激活

  ```lisp
  ;; 开启全局 Company 补全
  (global-company-mode 1)
  ```

- 窗口操作说明

  | 按键      | 命令                                | 作用                           |
  | --------- | ----------------------------------- | ------------------------------ |
  | C-x 2     | split-window-vertically             | 垂直拆分窗口                   |
  | C-x 3     | split-window-horizontally           | 水平拆分窗口                   |
  | C-x o     | other-window                        | 选择下一个窗口                 |
  | C-M-v     | scroll-other-window                 | 滚动下一个窗口                 |
  | C-x 4 b   | switch-to-buffer-other-window       | 在另一个窗口打开缓冲           |
  | C-x 4 C-o | display-buffer                      | 在另一个窗口打开缓冲，但不选中 |
  | C-x 4 f   | find-file-other-window              | 在另一个窗口打开文件           |
  | C-x 4 d   | dired-other-window                  | 在另一个窗口打开文件夹         |
  | C-x 4 m   | mail-other-window                   | 在另一个窗口写邮件             |
  | C-x 4 r   | find-file-read-only-other-window    | 在另一个窗口以只读方式打开文件 |
  | C-x 0     | delete-window                       | 关闭当前窗口                   |
  | C-x 1     | delete-other-windows                | 关闭其它窗口                   |
  | C-x 4 0   | kill-buffer-and-window              | 关闭当前窗口和缓冲             |
  | C-x ^     | enlarge-window                      | 增高当前窗口                   |
  | C-x {     | shrink-window-horizontally          | 将当前窗口变窄                 |
  | C-x }     | enlarge-window-horizontally         | 将当前窗口变宽                 |
  | C-x -     | shrink-window-if-larger-than-buffer | 如果窗口比缓冲大就缩小         |
  | C-x +     | balance-windows                     | 所有窗口一样高                 |

- shell

  执行一个 shell 命令
  M-!

  **mac 中的 Meta 键可能是 Esc，需要在设置中 用 option 键替换 esc 键**

  在当前区域中执行 shell 命令

  M-|

  开启一个 shell 窗口

  M-x shell

- shell 多开

  每次打开 shell 的时候，shell 所在 buffer 的名字是 _shell_ ， 因此，每次你键入上面的命 令都会切换到这个 buffer；

  你可以使用 M-x rename-buffer 来为这个 buffer 起个新名字。比如 shell-debug；

  这样再使用 M-x shell 的时候就会新开一个 shell。以这种方式，你可以开任意 多个 shell。
