# 环境变量/命令代理

- 原理

  自定义一个类似于 `.bash_profile` 文件，然后将自己平常用的命令和地址写入该文件

  在 shell 中使用 先定义一个隐藏文件 如 .person 然后写入自己日常使用的工作目录下

  每次打开新 shell,先执行 `source ~/.person` 将自定义的变量和命令定义好

## 自定义自己的环境变量

- 配置常用的工作目录

  如 在 .person 文件中写入

  ```bash
  work=/home/work
  root=/root
  ```

- 添加自定义的变量到 base_profile 中

  要求 .person 文件与 .base_profile 一致

  ```shell
  if test -f .person ; then
    source .person
  fi
  ```

## 定义自己的常用命令简写

- 配置常用的命令

  如结合上面的变量 在 .person 文件中写入

  ```bash
  alias work='cd ${work}'
  ```

## 生效

- 执行 `source ~/.person` 命令 ，即可使自己配置环境变量只在自己的项目中生效

- 写脚本每次打开新 shell 执行下 **自定义环境变量的方式**

  `source command.shell`

  ```shell
  #!/bin/bash
  # 定义自定义变量和常用命令
  echo "定义自定义环境变量"
  work=/home/work/work
  alias work='cd ${work}'
  echo "自定义command"
  alias
  ```
