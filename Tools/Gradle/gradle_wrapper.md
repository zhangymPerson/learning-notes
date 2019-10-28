## Gradle wrapper介绍

- 简单说明

    Gradle可以在没有安装Gradle的情况下使用，这时候就需要Gradle Wrapper了。Gradle Wrapper其实就是一个脚本文件，它会在没有安装Gradle的情况下为我们下载Gradle，之后我们就可以使用gradlew命令，像使用gradle一样来使用Gradle了。

### 项目中的使用

- wrappr文件位置

    创建gradle项目时会自动创建改目录$project_path/gradle/wrapper/目录

- 创建Gradle Wrapper文件

    使用gradle wrapper来创建一组Wrapper文件。Gradle官方建议我们在所有Gradle项目中都创建Wrapper文件，方便没有安装Gradle的用户使用。创建完毕之后，会发现我们的项目中多了如下一些文件：

    gradlew (Unix Shell 脚本)
    gradlew.bat (Windows批处理文件)
    
    gradle/wrapper/gradle-wrapper.jar (Wrapper JAR文件)
    gradle/wrapper/gradle-wrapper.properties (Wrapper属性文件)

    Gradle Wrapper会自动为我们下载合适的Gradle版本。
    
    默认情况下，下载位置是 
    
    >**$USER_HOME/.gradle/wrapper/dists**
    
    如果设置了GRADLE_USER_HOME环境变量，
    
    那么就会下载到 
    
    >**GRADLE_USER_HOME/wrapper/dists**

### 设置不同版本

- 使用命令

    gradle wrapper --gradle-version 3.2.1
    
- 编辑配置文件

    **gradle/wrapper/gradle-wrapper.properties**文件

    文件内容如下，可以编辑最后面的gradle-3.3-all.zip来配置版本。

    ```properties
    distributionBase=GRADLE_USER_HOME
    distributionPath=wrapper/dists
    zipStoreBase=GRADLE_USER_HOME
    zipStorePath=wrapper/dists
    distributionUrl=https\://services.gradle.org/distributions/gradle-3.3-all.zip
    ```

    然后使用gradlew -v来查看变更之后的版本。每次更改版本，都会下载对应版本的Gradle文件。不过只需要下载一次，之后再次使用相同的版本就不会下载了。
