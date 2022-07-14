# windows 下安装 gvim

## 下载安装

## 配置文件

> 查看 vim 配置文件的方式 在 vim 下 执行 :version 即可查看

- 使用 vim 命令

  ```sh
  vim
  #查看配置文件所在位置
  :version
  ```

  配置文件所在位置

  ```sh
  系统 vimrc 文件: "$VIM\vimrc"
  用户 vimrc 文件: "$HOME\_vimrc"
  第二用户 vimrc 文件: "$HOME\vimfiles\vimrc"
  第三用户 vimrc 文件: "$VIM\_vimrc"
  用户 exrc 文件: "$HOME\_exrc"
  第二用户 exrc 文件: "$VIM\_exrc"
  ```

- 修改配置

  查看目录位置 powershell 下

  ```sh
  echo $HOME
  ```

  创建\_vimrc 文件作为自定义的配置文件
