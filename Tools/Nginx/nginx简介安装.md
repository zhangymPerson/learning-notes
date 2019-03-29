# nginx介绍

- [百度百科介绍](https://baike.baidu.com/item/nginx/3817705)

    Nginx (engine x) 是一个高性能的HTTP和反向代理服务，也是一个IMAP/POP3/SMTP服务

    Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，并在一个BSD-like 协议下发行。其特点是占有内存少，并发能力强，事实上nginx的并发能力确实在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。

- 安装 


- 官网下载安装(tar包)

    - 依赖包安装
    ```
    yum -y install zlib zlib-devel openssl openssl-devel pcre pcre-devel
    ```

    - 解压tar包

    - 编译
    ```
    cd nginx-1.7.6
    ./configure   
    make
    make install  
    ```

    - 启动运行

- yum安装

    ```sh
    #安装nginx
    sudo yum install nginx 

    #测试配置文件  查看配置文件位置
    nginx -t

    #指定配置文件
    nginx -c /usr/local/nginx/conf/nginx.conf

    # 重新载入配置文件
    /usr/local/webserver/nginx/sbin/nginx -s reload

    #重启 Nginx
    /usr/local/webserver/nginx/sbin/nginx -s reopen

    #启动
    systemctl start nginx

    # 查找nginx
    which nginx
    $ /usr/sbin/nginx 
    
    #直接运行
    /usr/sbin/nginx

    ```