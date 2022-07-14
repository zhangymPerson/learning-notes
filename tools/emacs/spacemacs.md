# spacemacs 结合了 emacs 和 vim

## github 地址

- [https://github.com/syl20bnr/spacemacs](https://github.com/syl20bnr/spacemacs)

## 安装使用

- 需要安装 emacs

- 需要配置 HOME 环境变量。windows 下有多种配置方式

- 拉取 git 到本地某个文件夹下

  `git clone https://github.com/syl20bnr/spacemacs`

- **切换分支为 develop 分支**

  `git branch develop`

- 然后将 git 拉取的的文件夹下 `~/spacemacs/` 下所有的文件 复制到 `HOME/.emacs.d/`

- 启动 emacs 会自动安装相关的插件

- 常用操作

  创建文件夹 `+`

- 配置国内镜像源

  添加下面的代码到.spacemacs 的 dotspacemacs/user-init()

  ```Lisp
  (setq configuration-layer-elpa-archives
        '(("melpa-cn" . "http://elpa.emacs-china.org/melpa/")
          ("org-cn"   . "http://elpa.emacs-china.org/org/")
          ("gnu-cn"   . "http://elpa.emacs-china.org/gnu/")))
  ```

  清华源

  ```Lisp
  (setq configuration-layer--elpa-archives
    '(("melpa-cn" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/melpa/")
      ("org-cn"   . "http://mirrors.tuna.tsinghua.edu.cn/elpa/org/")
      ("gnu-cn"   . "http://mirrors.tuna.tsinghua.edu.cn/elpa/gnu/")))
  ```

  develop 分支

  注意：**修改位置同上，只是 key 变了**

  使用 configuration-layer-elpa-archives 代替原来的 configuration-layer--elpa-archives **( -- 换成 - )**
