# 打开客服端

- redis-cli

    ```
    #打开本地
    redis-cli
    #打开远程 
    redis-cli -h host -p port -a password
    ```

- 中文乱码

    ```
    #要在 redis-cli 后面加上 --raw
    redis-cli --raw
    ```
- 登陆

    ```
    # 没有登陆则操作报错
    (error) NOAUTH Authentication required.
    #密码登陆
    redis-cli -h 127.0.0.1 -p 6379 -a myPassword
    ```

    [redis-命令参考](http://doc.redisfans.com/)


