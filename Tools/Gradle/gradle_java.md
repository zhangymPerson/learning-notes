## Java构建入门 gradle构建java

- gradle中引入java插件

    build.gradle
    ```gradle
    apply plugin: 'java'
    ```
    （注：此例子的代码可以再所有“-all”结尾的发行版的samples/java/quickstart目录下找到）
    它将会把 Java 插件加入到你的项目中, 这意味着许多预定制的任务会被自动加入到你的项目里.
    
    Gradle 默认在 src/main/java 目录下寻找到你的正式（生产）源码, 在 src/test/java 目录下寻找到你的测试源码, 并在src/main/resources目录下寻找到你准备打包进jar的资源文件。测试代码会被加入到环境变量中设置的目录里运行。所有的输出文件都会被创建在构建目录里, 生成的JAR文件会被存放在 build/libs 目录下.
    
    **都加了什么可以执行的任务呢?**
    
    请在项目目录下使用 gradle tasks 来列出该项目的所有任务。

- 加入 Maven 仓库

    build.gradle
    ```gradle
    repositories {
        mavenCentral()
    }
    ```

- 加入依赖

    build.gradle
    ```gradle
    dependencies {
        compile group: 'commons-collections', name: 'commons-collections', version: '3.2'
        testCompile group: 'junit', name: 'junit', version: '4.+'
    }
    ```
- 定制 MANIFEST.MF 文件

    build.gradle
    ```gradle
    sourceCompatibility = 1.5
    version = '1.0'
    jar {
        manifest {
            attributes 'Implementation-Title': 'Gradle Quickstart', 'Implementation-Version': version
        }
    }
    ```
- 测试阶段加入一个系统属性
    build.gradle
    ```gradle
    test {
        systemProperties 'property': 'value'
    }
    ```

- 发布 JAR 文件

    通常 JAR 文件需要在某个地方发布. 为了完成这一步, 你需要告诉 Gradle 哪里发布 JAR 文件. 在 Gradle 里, 生成的文件比如 JAR 文件将被发布到仓库里. 在我们的例子里, 我们将发布到一个本地的目录. 你也可以发布到一个或多个远程的地点.
    build.gradle
    ```gradle
    uploadArchives {
        repositories {
            flatDir {
                dirs 'repos'
            }
        }
    }
    ```
    运行 gradle uploadArchives 命令来发布 JAR 文件.
- 多项目构建

    为了定义一个多项目构建, 你需要创建一个设置文件 ( settings file). 设置文件放在源代码的根目录, 它指定要包含哪个项目. 它的名字必须叫做 settings.gradle. 在这个例子中, 我们使用一个简单的分层布局. 下面是对应的设置文件:
    - 多项目构建 的 settings.gradle file
    settings.gradle
    ```gradle
    include "shared", "api", "services:webservice", "services:shared"
    ```

- 多项目构建 - 通用配置

   build.gradle
    ```gradle
    subprojects {
        apply plugin: 'java'
        apply plugin: 'eclipse-wtp'

        repositories {
            mavenCentral()
        }

        dependencies {
            testCompile 'junit:junit:4.11'
        }

        version = '1.0'

        jar {
            manifest.attributes provider: 'gradle'
        }
    } 
    ```
- 多项目构建 - 项目之间的依赖

    api/build.gradle
    ```gradle
    dependencies {
        compile project(':shared')
    }
    ```