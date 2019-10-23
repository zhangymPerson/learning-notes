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
    
