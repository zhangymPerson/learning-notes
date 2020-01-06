# nginx用户

- 用户模块

    Nginx 主进程（master process）会以 root 权限运行，之后主进程会读取 /etc/nginx/nginx.conf 文件中的 user 模块的配置，nginx 会使用这个指定的用户启动工作进程

    ```nginx.conf
    #user  nobody;
    #user配置需要和conf文件权限所有者一致，否则启动报错 403
    user  root;
    worker_processes  1;
    ```

- 查看用户启动用户名

    ps aux | grep "nginx: worker process" | awk '{print $1}'

    ps aux | grep "nginx: worker process" 

    如果是默认的nobody 则需要修改，否则可能页面访问不到