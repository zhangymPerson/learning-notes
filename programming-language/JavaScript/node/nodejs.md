# nodejs 说明

- [nodejs 官网](http://nodejs.cn/)

- [教程](http://www.runoob.com/nodejs/nodejs-tutorial.html)

- [安装教程](http://www.runoob.com/nodejs/nodejs-install-setup.html)

* [淘宝的 nodejs 镜像网站](https://npm.taobao.org/)

* [nodejs 教程-github](https://github.com/tuture-dev/nodejs-roadmap)

* 查看版本

  ```sh
  node -v

  node --version

  nodejs -v
  ```

* 修改镜像地址为淘宝的地址

  [查看说明]https://npm.taobao.org/

  安装报错

  #安装旧版本 npm install -g npm@5.6.0

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

  **全局安装需要配置全局位置，否则会认为命令执行的位置为全局安装目录**

  ```sh
  #查看全局安装位置
  npm config ls
  #查看所有默认的配置
  npm config ls -l
  #配置全局安装目录 并将改目录配置到环境变量下面 否则 npm install -g *** 安装后不能全局使用
  #path为全局安装目录所在位置
  npm config set prefix "path"
  #举例
  npm config set prefix "C:\Users\Administrator\AppData\Roaming\npm"
  ```

- 全局安装和本地安装区别

  npm 的包安装分为本地安装（local）、全局安装（global）两种，命令行的差别只是有没有 -g 而已，比如

  ```shell
  # 本地安装
  npm install express
  # 全局安装
  npm install express -g
  #卸载全局安装的软件命令
  npm uninstall -g react-native-cli
  ```

- 区别:

- 本地安装

  将安装包放在 ./node_modules 下（运行 npm 命令时所在的目录），如果没有 node_modules 目录，会在当前执行 npm 命令的目录下生成 node_modules 目录。可以通过 require() 来引入本地安装的包。

- 全局安装

  将安装包放在 /usr/local 下或者你 node 的安装目录。可以直接在命令行里使用。

- 全局安装 配置的位置 需要 **配置环境变量到 Path 中** 才能在任何位置使用命令

* 安装淘宝的镜像

  ```sh
  $ npm install -g cnpm --registry=https://registry.npm.taobao.org
  ```

### node js 全局库配置

- 查看全局安装库的位置

  ```sh
  npm config ls

  #查看 prefix 即为全局安装的包的位置
  ```

- 配置全局包的环境变量

  NODE_PATH=为 prefix 目录下/node_modules/

- 这样 js 可以直接使用相关库中的 js 文件

* nodejs 包管理器 npm 查看代理

  ```sh
  #置空
  npm config set proxy null
  npm config set https-proxy null
  #查看代理
  npm config get proxy
  npm config get https-proxy
  ```
