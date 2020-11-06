## Gradle wrapper 介绍

- 简单说明

  Gradle 可以在没有安装 Gradle 的情况下使用，这时候就需要 Gradle Wrapper 了。Gradle Wrapper 其实就是一个脚本文件，它会在没有安装 Gradle 的情况下为我们下载 Gradle，之后我们就可以使用 gradlew 命令，像使用 gradle 一样来使用 Gradle 了。

### 项目中的使用

- wrappr 文件位置

  创建 gradle 项目时会自动创建改目录\$project_path/gradle/wrapper/目录

- 创建 Gradle Wrapper 文件

  使用 gradle wrapper 来创建一组 Wrapper 文件。Gradle 官方建议我们在所有 Gradle 项目中都创建 Wrapper 文件，方便没有安装 Gradle 的用户使用。创建完毕之后，会发现我们的项目中多了如下一些文件：

  gradlew (Unix Shell 脚本)
  gradlew.bat (Windows 批处理文件)

  gradle/wrapper/gradle-wrapper.jar (Wrapper JAR 文件)
  gradle/wrapper/gradle-wrapper.properties (Wrapper 属性文件)

  Gradle Wrapper 会自动为我们下载合适的 Gradle 版本。

  默认情况下，下载位置是

  > **\$USER_HOME/.gradle/wrapper/dists**

  如果设置了 GRADLE_USER_HOME 环境变量，

  那么就会下载到

  > **GRADLE_USER_HOME/wrapper/dists**

### 设置不同版本

- 使用命令

  gradle wrapper --gradle-version 3.2.1

- 编辑配置文件

  **gradle/wrapper/gradle-wrapper.properties**文件

  文件内容如下，可以编辑最后面的 gradle-3.3-all.zip 来配置版本。

  ```properties
  distributionBase=GRADLE_USER_HOME
  distributionPath=wrapper/dists
  zipStoreBase=GRADLE_USER_HOME
  zipStorePath=wrapper/dists
  distributionUrl=https\://services.gradle.org/distributions/gradle-3.3-all.zip
  ```

  然后使用 gradlew -v 来查看变更之后的版本。每次更改版本，都会下载对应版本的 Gradle 文件。不过只需要下载一次，之后再次使用相同的版本就不会下载了。
