# 安装gradle

- 前提

    环境中需要提前安装好java环境

        java -version

- 官网下载

    windows 下安装 zip文件包

    解压到指定位置

    配置环境变量

    GRADLE_HOME=安装目录

    PATH下添加 GRADLE_HOME/bin

    测试命令

        gradle -v

    查看安装是否成功，安装的版本号

- 修改本地仓库地址

    设置本地仓库目录

    GRADLE_USER_HOME=

- 修改Gradle版本 

    在项目的gradle目录下

    wrapper目录下

    gradle-wrapper.properties 配置文件中

    修改 distributionUrl 参数路径 指定使用的gradle
    ```properties
    distributionUrl=https\://services.gradle.org/distributions/gradle-5.4.1-all.zip
    ```

    gradle 配置使用本地的zip包

    提前下载好zip包文件 然后指向即可

    ```properties
    distributionUrl=file\:/D:/zidingyipath/.gradle/wrapper/dists/gradle-2.10-all/a4w5fzrkeut1ox71xslb49gst/gradle-2.10-all.zip
    ```