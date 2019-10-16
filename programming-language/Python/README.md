# 此笔记主要记录Python开发中遇到的问题


## 学习网站

![Python - 菜鸟教程](http://www.runoob.com/python/python-tutorial.html)


## python3的安装

- 官网 

    [python官网](https://www.python.org/)

- 下载安装包

    wget 

- 解压到指定位置

    tar -xvzf **.tar.gz -C /*/*

- 安装


    需要先安装编译依赖的工具包

        yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel


    ```
    #可以填写参数 编译配置
    ./configure

    #编译
    make && make install
    ```