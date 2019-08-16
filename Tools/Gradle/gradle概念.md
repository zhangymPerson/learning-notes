# gradle构建基础


- 概念

    基于jvm的项目构建工具 - ant  和 maven 基础上 基于约定的构建方式


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
