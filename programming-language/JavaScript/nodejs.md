# nodejs 说明

- [nodejs官网](http://nodejs.cn/)

- [教程](http://www.runoob.com/nodejs/nodejs-tutorial.html)

- [安装教程](http://www.runoob.com/nodejs/nodejs-install-setup.html)

- 查看版本

    ```sh
    node -v 

    node --version

    nodejs -v
    ```

- 修改镜像地址为淘宝的地址

    [查看说明]https://npm.taobao.org/

    安装报错

        #安装旧版本
        npm install -g npm@5.6.0

    ```sh
    $ npm install -g cnpm --registry=https://registry.npm.taobao.org

    #安装模块
    $ cnpm install [name]
    #同步模块
    $ cnpm sync connect

    #部分系统自带的node 的命令是nodejs 需要做链接
    ln -s /usr/bin/nodejs /usr/bin/node
    ```
