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

- npm 安装的全局安装目录查看

    ```node
    npm config ls
    ```
- 全局安装和本地安装区别

    npm 的包安装分为本地安装（local）、全局安装（global）两种，
    命令行的差别只是有没有 -g 而已，比如
    ```shell
    npm install express          # 本地安装
    npm install express -g   # 全局安装
    ```
    区别:

    本地安装
    
    将安装包放在 ./node_modules 下（运行 npm 命令时所在的目录），如果没有 node_modules 目录，会在当前执行 npm 命令的目录下生成 node_modules 目录。
    可以通过 require() 来引入本地安装的包。
    
    全局安装
    
    将安装包放在 /usr/local 下或者你 node 的安装目录。
    可以直接在命令行里使用。

- 全局安装 配置的位置 需要 **配置环境变量到Path中** 才能在任何位置使用命令