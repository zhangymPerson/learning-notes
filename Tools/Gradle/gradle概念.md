# gradle构建基础


- 概念

    基于jvm的项目构建工具 - ant  和 maven 基础上 基于约定的构建方式

- 工程结构

    - 工程结构说明
        ```
        ├── build.gradle  
        ├── gradle
        │   └── wrapper
        │       ├── gradle-wrapper.jar  
        │       └── gradle-wrapper.properties  
        ├── gradlew  
        ├── gradlew.bat  
        └── settings.gradle  
        ```

    - build.gradle:文件包含项目构建所使用的脚本。

    - settings.grdle:文件将包含必要的一些设置，例如，任务或项目之间的依懒
    - gradlew: linux环境下的运行脚本

    - gradlew.bat: windows环境下的运行脚本

    - gradle文件夹:
    
        gradle文件中存在着wrapper文件夹，
        在wrapper下存在以下两个文件
        
            gradle-wrapper.jar
            
            gradle-wrapper.properties

    - src文件夹：

            这个文件夹主要是存放项目的代码文件和项目配置文件，跟maven一样，存在main文件和test文件

- 测试

    gradle 命令行 创建helloword任务流程

    创建build.gradle

    代码
    ```
    task helloword {
        doLast{
            println 'Hello word!'
        }
    }
    ```

    运行 gradle -q helloword



## gradle 构建包含三个基本块 

- project 和 tasks 和 property

### project 项目

项目包含多个 tasks

gradle中的build.gradle文件类似maven中的pom.xml文件

- Gradle 里的任何东西都是基于这两个基础概念:

    projects ( 项目 )
    
    tasks ( 任务 )

    每一个构建都是由一个或多个 projects 构成的. 一个 project 到底代表什么取决于你想用 Gradle 做什么. 举个例子, 一个 project 可以代表一个 JAR 或者一个网页应用. 它也可能代表一个发布的 ZIP 压缩包, 这个 ZIP 可能是由许多其他项目的 JARs 构成的. 但是一个 project 不一定非要代表被构建的某个东西. 它可以代表一件**要做的事, 比如部署你的应用.

    不要担心现在看不懂这些说明. Gradle 的合约构建可以让你来具体定义一个 project 到底该做什么.

    每一个 project 是由一个或多个 tasks 构成的. 一个 task 代表一些更加细化的构建. 可能是编译一些 classes, 创建一个 JAR, 生成 javadoc, 或者生成某个目录的压缩文件.
    
    目前, 我们先来看看定义构建里的一些简单的 task. 以后的章节会讲解多项目构建以及如何通过 projects 和 tasks 工作.



- 练习构建第一个gradle项目(Hello Word!)

    你可以通过在命令行运行 gradle 命令来执行构建，gradle 命令会从当前目录下寻找 build.gradle 文件来执行构建。我们称 build.gradle 文件为构建脚本。严格来说这其实是一个构建配置脚本;

    编写build.gradle文件
    ```gradle
    //编写一个helloword的任务
    task hello {
        doLast {
            println 'Hello world!'
        }
    }
    ```
    上面的脚本定义了一个叫做 hello 的 task，并且给它添加了一个动作。当执行 gradle hello 的时候, Gralde 便会去调用 hello 这个任务来执行给定操作。这些操作其实就是一个用 groovy 书写的闭包。

    在文件所在目录下执行 gradle -q hello

    **注意：高版本不支持 task << hello {}这种写法**

    ```gradle
    //依赖任务必须在前面 写到 intro 后面报错
    task hello  {
        println 'Hello world!'
    }
    // intro 任务依赖 hello 任务
    task intro(dependsOn: hello)  {
        println "I'm Gradle"
    }
    ```

    延时依赖
    ```gradle
    // 依赖任务上添加[ ' ] 可以延时依赖
    task taskX(dependsOn: 'taskY')  {
        println 'taskX'
    }
    task taskY  {
        println 'taskY'
    }
    ```

## gradle的生命周期

### 三个阶段：初始化阶段,配置阶段,执行阶段
 
- 初始化阶段

    gradle为项目创建了一个Project实例 

- 配置阶段

- 执行阶段


## gradle版本介绍

### gradle的3种版本

- gradle-xx-all.zip是完整版，包含了各种二进制文件，源代码文件，和离线的文档。

    例如：https://services.gradle.org/distributions/gradle-*.*-all.zip

- gradle-xx-bin.zip是二进制版，只包含了二进制文件（可执行文件），没有文档和源代码。

    例如：https://services.gradle.org/distributions/gradle-*.*-bin.zip

- gradle-xx-src.zip是源码版，只包含了Gradle源代码，不能用来编译你的工程。

    例如：https://services.gradle.org/distributions/gradle-*.*-src.zip