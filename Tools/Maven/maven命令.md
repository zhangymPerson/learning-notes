# maven 相关命令

- maven 的生命流程

    以Default 生命周期为例，并列举部分常用的的阶段：

    compile -> test-compile -> test -> package -> install -> deploy

- 常用命令

    ```sh
    # 查看系统信息
    mvn help:system

    # 创建项目

    #在命令过程中制定值
    mvn archetype:generate 


    # 直接指定值 
    mvn archetype:generate -DgroupId=com.companyname.test -DartifactId=test -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false




    # 构建项目 命令不同 生命周期不同
    ## 顺序 先编译主项目，看是否报错，有报错修改  在编译测试部分  最后打包
    #在项目文件 (pom.xml文件所在的位置) 执行
    # 编译主项目 即 target 目录下多了个编译后的文件 在顶层路径下（一般为classes文件下）classes/ 下执行: java com.test.Test 即可执行
    mvn clean compile

    #测试项目 即将test下面的类进行编译执行
    mvn clean test

    # 打包项目 会把测试也一起编译 
    mvn clean package


    ```