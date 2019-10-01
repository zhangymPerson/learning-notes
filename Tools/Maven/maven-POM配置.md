# pom 文件配置说明介绍

- 配置demo

```xml

    <!-- 项目创建组织的标识符，一般是域名的倒写 -->
    <groupId>com.janson.app</groupId>

    <!-- 定义了项目在所属组织的标识符下的唯一标识，一个组织下可以有多个项目 -->
    <artifactId>jansonTest</artifactId>

    <!--  打包的方式，有jar、war、ear等 -->
    <packaging>jar</packaging>

    <!-- 当前项目的版本，SNAPSHOT，表示是快照版本，在开发中 -->
    <version>1.0-SNAPSHOT</version>

    <!-- 项目的名称 -->
    <name>jansonTest</name>

    <!-- 项目的地址 -->
    <url>http://maven.apache.org</url>


    <!--自定义版本号-->
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <!-- spring版本号 -->
        <spring.version>4.3.7.RELEASE</spring.version>
        <!-- mybatis版本号 -->
        <mybatis.version>3.2.6</mybatis.version>
        <!-- log4j日志文件管理包版本 -->
        <slf4j.version>1.7.7</slf4j.version>
    </properties>
    <!-- 构建项目依赖的jar -->
    <dependencies>
        <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>3.8.1</version>
        <scope>test</scope>
        </dependency>
        <!-- spring核心包 -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <!--版本号变量调用方法-->
            <version>${spring.version}</version>
        </dependency>
    </dependencies>

    
```



- maven项目中单独指定maven仓库的配置

```xml

    <!--仓库-->
    <repositories>
        <repository>
            <id>central</id>
            <name>Central Repository</name>
            <url>http://central.maven.org/maven2/</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
        <!--阿里云仓库地址-->
        <repository>
            <id>alimaven</id>
            <name>aliyun maven</name>
            <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </repository>
    </repositories>

```
- maven构建时资源不全部加载的问题

```xml
<!--maven构建加载资源配置-->
<build>
    <resources>
        <resource>
            <directory>src/main/resources</directory>
            <includes>
                <!--包含文件夹以及子文件夹下所有资源-->
                <include>**/*.*</include>
            </includes>
        </resource>
    </resources>
</build>
```

- maven 构建时 资源过滤配置 不过滤可能导致部分文件格式损坏

```xml
            <!--maven 编译时过滤的内容  不对文件进行处理 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-resources-plugin</artifactId>
                <configuration>
                    <nonFilteredFileExtensions>
                        <nonFilteredFileExtension>xlsx</nonFilteredFileExtension>
                        <nonFilteredFileExtension>xls</nonFilteredFileExtension>
                        <nonFilteredFileExtension>zip</nonFilteredFileExtension>
                        <nonFilteredFileExtension>cer</nonFilteredFileExtension>
                        <nonFilteredFileExtension>pfx</nonFilteredFileExtension>
                        <nonFilteredFileExtension>py</nonFilteredFileExtension>
                        <nonFilteredFileExtension>keystore</nonFilteredFileExtension>
                    </nonFilteredFileExtensions>
                </configuration>
            </plugin>
```


- maven jar项目指定启动的类和主方法 maven 启动类的配置
    
    jar中没有主清单属性的时候



```xml
            <!--使用插件 问题时不能自动打包所需的maven依赖包-->
           <plugin>  
                <groupId>org.apache.maven.plugins</groupId>  
                <artifactId>maven-jar-plugin</artifactId>  
                <version>2.4</version>  
                <configuration>  
                    <archive>
                        <manifest>  
                            <addClasspath>true</addClasspath>  
                            <classpathPrefix>lib/</classpathPrefix>  
                            <mainClass>packname.classname</mainClass>  
                        </manifest>  
                    </archive>
                </configuration>  
            </plugin> 
```

- maven 将依赖包一起打包

```xml

            <plugin>
                <artifactId> maven-assembly-plugin </artifactId>
                <configuration>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                    <archive>
                        <manifest>
                            <mainClass>启动的主类全路径名称</mainClass>
                        </manifest>
                    </archive>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
```

- maven 不能clean

    有文件被占用，可以关掉启动程序的客户端或者 terminate ,然后重新执行即可

- maven 确定jdk版本和项目编码的配置

```xml
            <!--idea 编译Java 版本需要不停修改可以添加下面的配置固定jdk编译版本-->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.0</version>
                <configuration>
                    <!--jdk版本-->
                    <source>1.8</source>
                    <target>1.8</target>
                    <!-- 项目编码-->
                    <encoding>UTF-8</encoding>
                </configuration>
            </plugin>
```

- mvn 发布到本地仓库的配置

    **注意事项：**
    
    **1.配置在子pom中，packaging类型为pom的一般是父项目的pom.xml文件**
    
    配置文件中的含义：
        
        project.basedir=pom.xml文件所在文件夹的位置
        
        project.build.directory = ${project.basedir}/target

        其他的可以在idea中根据 pom.xml 文件点击进去查看

    ```xml
    <!--配置在子pom.xml中，packaging 类型不为 pom 类型的pom.xml中-->
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-install-plugin</artifactId>
        <version>2.4</version>
        <executions>
            <execution>
                <id>install-find-repo</id>
                <goals>
                    <goal>install-file</goal>
                </goals>
                <phase>install</phase>
                <configuration>
                    <file>
                        ${project.build.directory}/${project.build.finalName}.jar
                    </file>
                    <sources>${project.build.directory}/${project.build.finalName}-sources.jar</sources>
                    <groupId>${project.groupId}</groupId>
                    <artifactId>${project.artifactId}</artifactId>
                    <version>${project.version}</version>
                    <packaging>jar</packaging>
                </configuration>
            </execution>
        </executions>
    </plugin>
    <!--打包源码的jar配置  在有源码的位置配置，不要配置在父pom.xml中-->
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-source-plugin</artifactId>
        <executions>
            <execution>
                <id>attach-sources</id>
                <goals>
                    <goal>jar</goal>
                </goals>
            </execution>
        </executions>
    </plugin>
    ```

- maven打包源码

    插件:maven-source-plugin
    ```xml
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-source-plugin</artifactId>
            <executions>
                <execution>
                    <id>attach-sources</id>
                    <goals>
                        <goal>jar</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    ```
- maven 打包生成文档插件

    ```xml
    <!-- 文档 插件 -->
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-javadoc-plugin</artifactId>
        <version>2.7</version>
        <executions>
            <execution>
                <id>attach-javadocs</id>
                <goals>
                    <goal>jar</goal>
                </goals>
                <configuration>
                    <additionalparam>-Xdoclint:none</additionalparam>
                </configuration>
            </execution>
        </executions>
    </plugin>
    ```

- maven中jar包引入的scope范围

    maven的哲学在上次技术分享的时候也提到了：约定大于配置，所以在maven中，很多内容都有默认值，scope的默认值是compile，那么scope还能有哪些选项呢？

    scope的分类
    
    - compile：默认值 他表示被依赖项目需要参与当前项目的编译，还有后续的测试，运行周期也参与其中，是一个比较强的依赖。打包的时候通常需要包含进去

    - test：依赖项目仅仅参与测试相关的工作，包括测试代码的编译和执行，不会被打包，例如：junit

    - runtime：表示被依赖项目无需参与项目的编译，不过后期的测试和运行周期需要其参与。与compile相比，跳过了编译而已。例如JDBC驱动，适用运行和测试阶段

    - provided：打包的时候可以不用包进去，别的设施会提供。事实上该依赖理论上可以参与编译，测试，运行等周期。相当于compile，但是打包阶段做了exclude操作

    - system：从参与度来说，和provided相同，不过被依赖项不会从maven仓库下载，而是从本地文件系统拿。需要添加systemPath的属性来定义路径

- scope的依赖传递

    a.pom 引入 b，b依赖c。当前项目为a，只当b在a项目中的scope，那么c在a中的scope是如何得知呢？

    当C是test或者provided时，c直接被丢弃，a不依赖c；（排除传递依赖）

    否则a依赖c，c的scope继承于b的scope


- 错误配置分析(pom配置)

```xml
    <!--parent 标签中的变量 不能使用子项目中的变量 -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <!--todo
            远程父项目中的变量
            不能在子项目中定义；
            否则报错找不到版本号
        -->
        <version>2.1.0.RELEASE</version>
        <relativePath/>
    </parent>
```
报错如下:
```
[ERROR] [ERROR] Some problems were encountered while processing the POMs:
[FATAL] Non-resolvable parent POM for cn.danao:springboot-jdbc:1.0-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:${springboot.version} from/to alimaven (http://maven.aliyun.com/nexus/content/groups/public/): TransferFailedException and 'parent.relativePath' points at no local POM @ line 15, column 13
 @ 
[ERROR] The build could not read 1 project -> [Help 1]
[ERROR]   
[ERROR]   The project cn.danao:springboot-jdbc:1.0-SNAPSHOT (E:\work\git\github\springboot-learing\springboot-jdbc\pom.xml) has 1 error
[ERROR]     Non-resolvable parent POM for cn.danao:springboot-jdbc:1.0-SNAPSHOT: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:${springboot.version} from/to alimaven (http://maven.aliyun.com/nexus/content/groups/public/): TransferFailedException and 'parent.relativePath' points at no local POM @ line 15, column 13: ClientProtocolException: Invalid redirect URI: https://maven.aliyun.com/nexus/content/groups/public/org/springframework/boot/spring-boot-starter-parent/${springboot.version}/spring-boot-starter-parent-${springboot.version}.pom: Illegal character in path at index 106: https://maven.aliyun.com/nexus/content/groups/public/org/springframework/boot/spring-boot-starter-parent/${springboot.version}/spring-boot-starter-parent-${springboot.version}.pom -> [Help 2]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/ProjectBuildingException
[ERROR] [Help 2] http://cwiki.apache.org/confluence/display/MAVEN/UnresolvableModelException
```