# emacs 简单使用

- **[emacs 国内社区](https://emacs-china.org/)**

- 使用教程

  [github](https://github.com/emacs-china/Spacemacs-rocks)

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

  Alt + x linum-mode

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

  ```
  ;; 开启全局 Company 补全
  (global-company-mode 1)
  ```
