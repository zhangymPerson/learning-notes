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

- project 和 tasks
