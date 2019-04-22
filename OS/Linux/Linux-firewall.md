# linux中的防火墙配置

- [百度百科](https://baike.baidu.com/item/防火墙/52767)
- firewalld的基本使用

    ```sh
    #启动 
    systemctl start firewalld
    #关闭
    systemctl stop firewalld
    #查看状态
    systemctl status firewalld 
    #开机禁用
    systemctl disable firewalld
    #开机启用
    systemctl enable firewalld
    ```

- iptables

    ```sh
    # 查看防火墙状态
    service iptables status  

    # 停止防火墙
    service iptables stop  

    # 启动防火墙
    service iptables start  

    # 重启防火墙
    service iptables restart  

    # 永久关闭防火墙
    chkconfig iptables off  

    # 永久关闭后重启
    chkconfig iptables on

    ```


