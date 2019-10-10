# idea 创建gradle项目

- 安装好gradle


    [](https://blog.csdn.net/shuai_wy/article/details/80394443)

    创建gradle项目

    file - new project - java - GroupId / ArtifacId - next -
    

## gradle 构建java

- setting.gradle 和 build.gradle说明

### setting.gradle

- 内容参数说明

    Gradle 中就是通过执行 Settings 类来完成构建的 初始化阶段。

    settings.gradle对应于 Settings 类

    gradle 默认只执行当前目录下的build.gradle 脚本

    多个模块依赖的，这时需要我们对多个目录同时编译，那就需要我们创建一个settings.gradle  文件 管理多模块　

    父目录下有settings.gradle （没有则需要自己创建,位置和父build.gradle一致）,里边添加其他目录，会继续执行其他目录下的build.gradle

    每一个 project 的路径都是相对于根project而言的，路径的分隔符是 : 而不是\。

    如 ```:路径1:路径2```

    ```gradle
    添加一个 project
    //添加:app这个module参与构建
    include ":app"
    ```
### build.gradle

- 参数的说明

- apply (配置插件)

    ```gradle
    apply plugin: 'java'
    apply plugin: 'application'
    ```

- dependencies (依赖)

    第一个参数的含义：
    
    - complile（编译时）
    
    - runtime（运行时）
    
    - testCompile（测试编译时）
    
    - testRuntime（测试运行时）
    ```gradle
    testCompile group: 'junit', name: 'junit', version: '4.12'
    ```
    
- repositories(配置仓库)

    ```gradle
    repositories {
        mavenCentral()
    }
    ```