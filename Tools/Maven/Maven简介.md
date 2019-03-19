# Maven 

## 概念介绍

    - 概念
    Maven是一个项目管理工具，它包含了一个项目对象模型 (Project Object Model)，一组标准集合，一个项目生命周期(Project Lifecycle)，一个依赖管理系统(Dependency Management System)，和用来运行定义在生命周期阶段(phase)中插件(plugin)目标(goal)的逻辑。当你使用Maven的时候，你用一个明确定义的项目对象模型来描述你的项目，然后Maven可以应用横切的逻辑，这些逻辑来自一组共享的（或者自定义的）插件。

    Maven 有一个生命周期，当你运行 mvn install 的时候被调用。这条命令告诉 Maven 执行一系列的有序的步骤，直到到达你指定的生命周期。遍历生命周期旅途中的一个影响就是，Maven 运行了许多默认的插件目标，这些目标完成了像编译和创建一个 JAR 文件这样的工作。

    Project Object Model 即项目对象模型 ，整个maven项目最重要的是pom.xml文件
    
    
    [Maven-百度百科](https://baike.baidu.com/item/Maven)


    [阿里云maven地址搜索地址](https://maven.aliyun.com/mvn/search)

## 原理

### Maven 


- 项目构成

默认约定

默认源码：${basedir}/src/main/java
资源文件:${basedir}/src/main/resources
测试代码：${basedir}/src/main/test
编译文件存放在:${basedir}/target
JAR文件存放在:${basedir}/target


- 管理项目依赖

    maven中的坐标，maven通过坐标确定项目组件位置；

    maven中的坐标元素有:groupId,artifactId,version,packaging,classfier

    groupId: 当前maven所属的实际项目

    artifactId:项目中的一个maven模块，

    version:版本，指定选择模块的版本

    packaging:定义maven的打包方式

    classfier:用来帮助定义构建输出的一些附属组件
    
    eg:
    ```xml
    <dependency>
        <groupId>io.netty</groupId>
        <artifactId>netty-all</artifactId>
        <version>4.1.32.Final</version>
    </dependency>
    ```

- 仓库

    本地仓库:

    远程仓库:
## 作用