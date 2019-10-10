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


