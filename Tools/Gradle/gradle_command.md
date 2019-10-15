# 常用命令

- 下载安装以后

    ```sh
    gradle -v 

    gradle -h
    ```
- 构建

    ```sh
    #hello 是 task name
    gradle -q hello
    gradle hello

    #构建
    gradle build 
    #列出项目的所有属性. 这样你就可以看到 Java 插件加入的属性以及它们的默认值.
    gradle properties
    #来列出该项目的所有任务。
    gradle tasks 
    ```