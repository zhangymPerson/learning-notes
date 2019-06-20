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