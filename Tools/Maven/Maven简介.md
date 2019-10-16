# Maven 

## 概念介绍

- 概念

    Maven是一个项目管理工具，它包含了一个项目对象模型 (Project Object Model)，一组标准集合，一个项目生命周期(Project Lifecycle)，一个依赖管理系统(Dependency Management System)，和用来运行定义在生命周期阶段(phase)中插件(plugin)目标(goal)的逻辑。当你使用Maven的时候，你用一个明确定义的项目对象模型来描述你的项目，然后Maven可以应用横切的逻辑，这些逻辑来自一组共享的（或者自定义的）插件。

    Maven 有一个生命周期，当你运行 mvn install 的时候被调用。这条命令告诉 Maven 执行一系列的有序的步骤，直到到达你指定的生命周期。遍历生命周期旅途中的一个影响就是，Maven 运行了许多默认的插件目标，这些目标完成了像编译和创建一个 JAR 文件这样的工作。

    Project Object Model 即项目对象模型 ，整个maven项目最重要的是pom.xml文件
    
    
    [Maven-百度百科](https://baike.baidu.com/item/Maven)


    [阿里云maven地址搜索地址](https://maven.aliyun.com/mvn/search)


    **注意**：Maven构建工具的特点，**约定优于配置**
## 原理

### Maven 


- 项目构成

默认约定

- 默认源码：${basedir}/src/main/java
- 资源文件:${basedir}/src/main/resources
- 测试代码：${basedir}/src/main/test
- 编译文件存放在:${basedir}/target
- JAR文件存放在:${basedir}/target

- maven项目结构

    ```
    ├─springboot-log                        #项目名称
    │  ├─src                                            #源码位置
    │  │  ├─main                                  #项目源码编写
    │  │  │  ├─java                               # java 代码存放位置
    │  │  │  │  └─cn
    │  │  │  │      └─danao
    │  │  │  │          ├─annotation
    │  │  │  │          ├─aop
    │  │  │  │          ├─controller
    │  │  │  │          ├─exception
    │  │  │  │          └─util
    │  │  │  └─resources                     #项目使用的配置文件位置
    │  │  └─test                                     #测试的java代码位置
    │  │      ├─cn
    │  │      │  └─danao
    │  │      │      └─test
    │  │      │          └─base
    │  │      └─resources                     #测试配置位置
    │  └─target								     # mvn clean 清理该文件夹 mvn install / mvn package 生成该文件夹
    │      ├─classes                              #编译好的二进制文件所在位置
    │      │  └─cn
    │      │      └─danao
    │      │          ├─annotation
    │      │          ├─aop
    │      │          ├─controller
    │      │          ├─exception
    │      │          └─util
    │      ├─generated-sources
    │      │  └─annotations
    │      ├─maven-archiver
    │      ├─maven-status
    │      │  └─maven-compiler-plugin
    │      │      └─compile
    │      │          └─default-compile
    │      ├─springbootlog-1.0-SNAPSHOT.jar  #编译生成的jar包
    │      └─test-classes

    ```


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

## 仓库概念

![maven仓库结构图](../../Picture/maven%E4%BB%93%E5%BA%93%E5%9B%BE.png)
    
- 本地仓库配置

    maven安装目录下$MAVEN_HOME/conf/setting.xml:
    ```xml
      <localRepository>D:\Program Files (x86)\apache-maven-3.6.1\repository</localRepository>
    ```
- 远程仓库配置:

    1.修改maven的setting.xml文件格式
    ```xml
    <mirrors>
        <!-- mirror
        | Specifies a repository mirror site to use instead of a given repository. The repository that
        | this mirror serves has an ID that matches the mirrorOf element of this mirror. IDs are used
        | for inheritance and direct lookup purposes, and must be unique across the set of mirrors.
        |
        <mirror>
        <id>mirrorId</id>
        <mirrorOf>repositoryId</mirrorOf>
        <name>Human Readable Name for this Mirror.</name>
        <url>http://my.repository.com/repo/path</url>
        </mirror>
        -->
        <mirror>
        <id>nexus-aliyun</id>
        <mirrorOf>central</mirrorOf>
        <name>nexus-aliyun</name>
        <url>http://maven.aliyun.com/nexus/content/groups/public</url>
        </mirror> 
    </mirrors>
    ```
    2.修改单个项目的pom.xml文件
    ```xml
    <repositories>
        <repository>
            <id>maven-aliyun</id>
            <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>true</enabled>
                <updatePolicy>always</updatePolicy>
                <checksumPolicy>fail</checksumPolicy>
            </snapshots>
        </repository>
    </repositories>
    ```
## 作用

## maven 各个阶段的依赖关系

### maven各个阶段的依赖关系 - 生命周期 maven构建的关键生命周期


- clean 清理上次构建

- validate 验证项目定义的正确性

- compile 编译源代码

- test 测试源代码

- package 打包 jar 和 war

- integration-test  运行集成测试

- verify 对组装的工作进行校验检查

- install 安装工件到本地仓库

- deploy 部署到远程仓库

### maven笔记

- 插件
    maven被设计成将主要职责委培给一组maven插件来处理

- 项目的概念模型

    依赖管理

    远程仓库

    全局性构建逻辑重用

    工具可移植性/集成

    便于搜索和过滤构件


