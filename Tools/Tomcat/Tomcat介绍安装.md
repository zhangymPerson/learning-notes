# Tomcat 介绍

- [百度百科](https://baike.baidu.com/item/tomcat/255751)

- [github地址](https://github.com/apache/tomcat)


## 安装使用

- 下载

    wget 官网下载地址

- 解压

    ```sh
    #解压到指定文件夹下面
    tar -xvzf ***.tar.gz -C /*/* 
    ```
- 启动
    ```sh
    #进入安装目录
    cd $tomcathome/bin

    #启动tomcat
    ./startup.sh
    ```

- 查看日志

    ```sh
    #进入安装目录
    cd $tomcathome/log

    #查看日志
    tailf catalina.out
    ```
