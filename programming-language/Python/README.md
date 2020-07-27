# 此笔记主要记录 Python 开发中遇到的问题

## 目录

## 其他

## 学习网站

  [Python - 菜鸟教程](http://www.runoob.com/python/python-tutorial.html)

## python3 的安装

- 官网

  [python 官网](https://www.python.org/)

- 下载安装包

  wget

- 解压到指定位置

  tar -xvzf \*_.tar.gz -C /_/\*

- 安装

  需要先安装编译依赖的工具包

  `yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel`

  ```sh
  #可以填写参数 编译配置
  ./configure

  #编译
  make && make install
  ```
