# Android sdk 安装配置

- android sdk下载地址

    [外网地址](http://developer.android.com/sdk/index.html) - http://developer.android.com/sdk/index.html

    [国内地址](http://www.androiddevtools.cn) - http://www.androiddevtools.cn

- 下载安装

    找到sdk tools 的 zip格式的

    解压

    android-sdk-windows 文件夹内

    运行sdk manager

    选择需要的工具下载

- sdk manger 管理工具配置国内代理  (软件名：SDK Manager.exe)

    启动 Android SDK Manager ;

    打开主界面，菜单依次选择「Tools」、「Options...」;
    
    弹出『Android SDK Manager - Settings』窗口；

    在『Android SDK Manager - Settings』窗口中，
    
    在「HTTP Proxy Server」和「HTTP Proxy Port」输入框内填入mirrors.neusoft.edu.cn和80
    
    **并且选中「Force https://... sources to be fetched using http://...」复选框。**
    
    设置完成后单击「Close」按钮关闭『Android SDK Manager - Settings』，
    
    窗口返回到主界面；

    依次选择「Packages」、「Reload」。


- sdkmanager (软件位置：%Android_home%/tools/bin/sdkmanager)

    使用国内镜像代理下载，常用的国内镜像

    Android SDK 在线更新镜像服务器资源：

    大连东软信息学院镜像服务器地址:
    mirrors.neusoft.edu.cn 端口：80
    郑州大学开源镜像站
    mirrors.zzu.edu.cn 端口：80

    使用指令时附上参数，如下
    sdkmanager --list --no_https --proxy=http --proxy_host=mirrors.neusoft.edu.cn --proxy_port=80

    **使用代理可能造成无任何包显示 需谨慎使用**

- 环境变量配置


    增加ANDROID_HOME环境变量，路径为sdk安装目录，本电脑对应路径D:\android-sdk-windows；
    
    然后在path环境变量中增加路径：;%ANDROID_HOME%\platform-tools;%ANDROID_HOME%\tools; 
    
    **注意相对路径前面一定要加;号**

- 验证sdk环境

    进入命令行，输入命令，出现如下提示，环境配置成功。
    ```    
    C:\Users\Administrator>adb
    Android Debug Bridge version 1.0.41
    Version 29.0.4-5871666
    Installed as C:\Program Files\Java\android-sdk-windows\platform-tools\adb.exe
    ```
    

- 构建apk的时候无licenses

    使用命令
    ```
    ./sdkmanager --licenses
    ```

    报错 Error: Unknown argument --licenses

    更新也没用
    ```
    ./sdkmanager --update
    ```

    从   [国内地址](http://www.androiddevtools.cn) - http://www.androiddevtools.cn 下载 Android sdk工具 - SDK Tools 

    压缩包 解压 执行 
    ```
    ./bin/sdkmanager --licenses
    #全选y
    ```
    将 生成的 licenses目录下的文件复制到 Android_Home中的licenses文件夹中