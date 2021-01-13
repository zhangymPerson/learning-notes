# shell 基本概念和变量

[返回](./README.md)

- 概念

  在计算机科学中，Shell 俗称壳（用来区别于核），是指“为使用者提供操作界面”的软件（命令解析器）。它类似于 DOS 下的 command.com 和后来的 cmd.exe。它接收用户命令，然后调用相应的应用程序。 - 百度百科

- shell 类型

  ```sh
  #可以在这个文件中修改用户登陆后的默认的shell
  #查看用户的shell权限
  cat /etc/passwd
  ```

- shell 中的关系

  shell 中父子关系

  父 shell ---创建子 shell---> 子 shell

  ```sh
  # 命令
  # PPID这一列即为父进程的ID
  ps -f

  # 查看父子进程关系
  ps --forest
  ```

  **shell 中添加分号可直接一行中执行多个命令**

- Linux 上的 shell

  建议:学会使用 vim 等 linux 上的编辑器

  第一个 shell

  ```sh
  vim a.sh

  #!/bin/bash
  echo "Hello World !"

  #运行shell
  #为脚本添加可执行权限
  chmod +x a.sh
  #在脚本目录文件下
  ./a.sh

  #作为解释器参数

  #这种运行方式是，直接运行解释器，其参数就是 shell 脚本的文件名，如：
  sh test.sh

  ```

  **注意** : 如果#!/bin/bash 报错 可使用 which bash 查找 bash 的路径

- shell 中的变量

  - shell 中的变量命名规则：

    命名只能使用英文字母，数字和下划线，首个字符不能以数字开头。

    中间不能有空格，可以使用下划线（\_）。

    不能使用标点符号。

    不能使用 bash 里的关键字（可用 help 命令查看保留关键字）

  **注意，变量名和等号之间不能有空格**

- shell 命令成功与否的判断

  ```sh

  if [ $? -eq 0 ]; then
      echo "success"
  else
      echo "fail"
  fi

  ```

- shell 在 Ubuntu 下报错 function: not found

  解决方案:

  ubuntu 的 dash 兼容性不好导致，而编译常用的是 bash。

  所以大家可以直接将 ubuntu 的编辑器(shell)操作进行更改。命令如下：

  `sudo dpkg-reconfigure dash`

  运行后 选择 no。
