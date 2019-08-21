# maven 相关命令


**maven在windows下的命令参数需要加 “ ‘ ”,不然报错,生命周期不存在**


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


    #创建Maven的普通Java项目:
    mvn archetype:create -DgroupId=packageName -DartifactId=projectName
    
    #创建Maven的Web项目：
    mvn archetype:create -DgroupId=packageName  -DartifactId=webappName -DarchetypeArtifactId=maven-archetype-webapp
    
    #编译源代码：
    mvn compile
    #编译测试代码：
    mvn test-compile
    #运行测试:
    mvn test
    #产生site：
    mvn site
    #打包：
    mvn package
    #在本地Repository中安装jar：
    mvn install
    例：installing D:\xxx\xx.jar to D:\xx\xxxx
    #清除产生的项目：
    mvn clean
    #生成eclipse项目：
    mvn eclipse:eclipse
    #生成idea项目：
    mvn idea:idea
    #组合使用goal命令，如只打包不测试：
    mvn -Dtest package
    #编译测试的内容：
    mvn test-compile
    #只打jar包:
    mvn jar:jar
    #只测试而不编译，也不测试编译：
    mvn test -skipping compile -skipping test-compile
    ( -skipping 的灵活运用，当然也可以用于其他组合命令) 
    #清除eclipse的一些系统设置:
    mvn eclipse:clean 
    #查看当前项目已被解析的依赖：
    mvn dependency:list
    #上传到私服：
    mvn deploy
    #强制检查更新，由于快照版本的更新策略(一天更新几次、隔段时间更新一次)存在，如果想强制更新就会用到此命令: 
    mvn clean install-U
    #源码打包：
    mvn source:jar
    或
    mvn source:jar-no-fork
    ```


- maven信息查看命令

    ```sh
    #显示版本信息 :
    mvn -version/-v

    #创建mvn项目:
    mvn archetype:create -DgroupId=com.oreilly -DartifactId=my-app

    #生成target目录，编译、测试代码，生成测试报告，生成jar/war文件 :
    mvn package

    #运行项目于jetty上:
    mvn jetty:run

    #显示详细错误 信息:
    mvn -e

    #验证工程是否正确，所有需要的资源是否可用:
    mvn validate

    #在集成测试可以运行的环境中处理和发布包:
    mvn integration-test

    #运行任何检查，验证包是否有效且达到质量标准:
    mvn verify

    #产生应用需要的任何额外的源代码，如xdoclet :
    mvn generate-sources

    #使用 help 插件的  describe 目标来输出 Maven Help 插件的信息:
    mvn help:describe -Dplugin=help

    #使用Help 插件输出完整的带有参数的目标列 :
    mvn help:describe -Dplugin=help -Dfull

    #获取单个目标的信息,设置  mojo 参数和  plugin 参数。此命令列出了Compiler 插件的compile 目标的所有信息 :
    mvn help:describe -Dplugin=compiler -Dmojo=compile -Dfull

    #列出所有 Maven Exec 插件可用的目标:
    mvn help:describe -Dplugin=exec -Dfull

    #看这个“有效的 (effective)”POM，它暴露了 Maven的默认设置 :
    mvn help:effective-pom

    #想要查看完整的依赖踪迹，包含那些因为冲突或者其它原因而被拒绝引入的构件，打开 Maven 的调试标记运行 :
    mvn install -X

    #给任何目标添加maven.test.skip 属性就能跳过测试 :
    mvn install -Dmaven.test.skip=true

    #构建装配Maven Assembly 插件是一个用来创建你应用程序特有分发包的插件 :
    mvn install assembly:assembly

    #生成Wtp插件的Web项目 :
    mvn -Dwtpversion=1.0 eclipse:eclipse

    #清除Eclipse项目的配置信息(Web项目) :
    mvn -Dwtpversion=1.0 eclipse:clean

    #将项目转化为Eclipse项目 :
    mvn eclipse:eclipse

    #mvn exec命令可以执行项目中的main函数 :
    首先需要编译java工程：mvn compile
    不存在参数的情况下：mvn exec:java -Dexec.mainClass="***.Main"
    存在参数：mvn exec:java -Dexec.mainClass="***.Main" -Dexec.args="arg0 arg1 arg2"
    指定运行时库：mvn exec:java -Dexec.mainClass="***.Main" -Dexec.classpathScope=runtime

    #打印出已解决依赖的列表 :
    mvn dependency:resolve

    #打印整个依赖树 :
    mvn dependency:tree
    ```

- maven 部署到本地仓库

    windows下需要 -D 添加 [ ' ] Linux下不需要
    ```shell
    mvn install:install-file -D'file=D:\person\github\base-java-utils\baseutil\baseprint\target\baseprint-1.0-SNAPSHOT.jar' -D'groupId=cn.danao' -D'artifactId=baseutil' -D'version=1.0-SNAPSHOT' -D'packaging=jar'
    ```