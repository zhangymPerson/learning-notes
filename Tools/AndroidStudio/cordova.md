# cordova使用 

- [中文支持网站](http://cordova.axuer.com/docs/zh-cn/latest/)


## 简介

Apache Cordova是一个开源的移动开发框架。允许你用标准的web技术-HTML5,CSS3和JavaScript做跨平台开发。 应用在每个平台的具体执行被封装了起来，并依靠符合标准的API绑定去访问每个设备的功能，比如说：传感器、数据、网络状态等。


## 安装

- 前提

    安装[node.js](https://nodejs.org/en/download/)

- 在OS X和Linux上:

   ```shell
   $ sudo npm install -g cordova
   ```

    在OS X和Linux上, npm命令加上前缀sudo因为cordova可能需要安装在其他的受限制目录比如 /usr/local/share。如果你使用可选工具nvm/nave或者具有安装目录的写权限，那么你可以省略sudo前缀。这里有更多提示 可用在使用 npm 没有 sudo前缀时，如果你想那么做。

- 在Windows上:

    ```
    C:\>npm install -g cordova
    ```

    -g标志是告诉 npm 我们全局安装 cordova。否则我们将会安装在当前工作目录的 node_modules子目录。

    安装完成后，你应该能够在命令行中运行cordova命令，在没有任何参数的时候会打印一些帮助信息。

