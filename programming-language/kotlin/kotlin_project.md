# kotlin项目

## Java项目改造成kotlin

### maven项目

 - [文档地址](https://www.kotlincn.net/docs/reference/using-maven.html)

>kotlin-maven-plugin 用于编译 Kotlin 源代码与模块，目前只支持 **Maven V3**


#### java普通maven转kotlin过程

- 添加依赖

    修改 mvn pom.xml

    指定版本
    ```xml
    <properties>
        <kotlin.version>1.3.71</kotlin.version>
    </properties>
    ```

    添加`kotlin`编译所需依赖包

    ```xml
    <dependencies>
        <dependency>
            <groupId>org.jetbrains.kotlin</groupId>
            <artifactId>kotlin-stdlib</artifactId>
            <version>${kotlin.version}</version>
        </dependency>
    </dependencies>
    ```

    编译配置

    要编译源代码，请在 <build> 标签中指定源代码目录
    ```xml
    <build>
        <sourceDirectory>${project.basedir}/src/main/kotlin</sourceDirectory>
        <testSourceDirectory>${project.basedir}/src/test/kotlin</testSourceDirectory>
    </build>
    ```
    需要引用 Kotlin Maven 插件来编译源代码：
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.jetbrains.kotlin</groupId>
                <artifactId>kotlin-maven-plugin</artifactId>
                <version>${kotlin.version}</version>

                <executions>
                    <execution>
                        <id>compile</id>
                        <goals> <goal>compile</goal> </goals>
                    </execution>

                    <execution>
                        <id>test-compile</id>
                        <goals> <goal>test-compile</goal> </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
    ```

    同时编译 Kotlin 与 Java 源代码

    要编译混合代码应用程序，必须在 Java 编译器之前调用 Kotlin 编译器。 

    按照 maven 的方式，这意味着应该使用以下方法在 maven-compiler-plugin 之前运行 kotlin-maven-plugin，

    **确保 pom.xml 文件中的 kotlin 插件位于 maven-compiler-plugin 上面**
    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.jetbrains.kotlin</groupId>
                <artifactId>kotlin-maven-plugin</artifactId>
                <version>${kotlin.version}</version>
                <executions>
                    <execution>
                        <id>compile</id>
                        <goals> <goal>compile</goal> </goals>
                        <configuration>
                            <sourceDirs>
                                <sourceDir>${project.basedir}/src/main/kotlin</sourceDir>
                                <sourceDir>${project.basedir}/src/main/java</sourceDir>
                            </sourceDirs>
                        </configuration>
                    </execution>
                    <execution>
                        <id>test-compile</id>
                        <goals> <goal>test-compile</goal> </goals>
                        <configuration>
                            <sourceDirs>
                                <sourceDir>${project.basedir}/src/test/kotlin</sourceDir>
                                <sourceDir>${project.basedir}/src/test/java</sourceDir>
                            </sourceDirs>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.5.1</version>
                <executions>
                    <!-- 替换会被 maven 特别处理的 default-compile -->
                    <execution>
                        <id>default-compile</id>
                        <phase>none</phase>
                    </execution>
                    <!-- 替换会被 maven 特别处理的 default-testCompile -->
                    <execution>
                        <id>default-testCompile</id>
                        <phase>none</phase>
                    </execution>
                    <execution>
                        <id>java-compile</id>
                        <phase>compile</phase>
                        <goals> <goal>compile</goal> </goals>
                    </execution>
                    <execution>
                        <id>java-test-compile</id>
                        <phase>test-compile</phase>
                        <goals> <goal>testCompile</goal> </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
    ```

- idea中需要添加相关的配置

    创建kotlin源码文件夹 
    
    `${project.basedir}/src/main/kotlin`
    
    在`maven`的`po,.xml`中的 `build`下配置的kotlin源文件位置

    然后打开`project structure`中 `modules` 选择`kotlin` 进行相关的配置 如 `jvm` 和 `language version`等 

- 编写测试代码

    在源文件夹下创建自定义包
    
    编写`App.kt`

    ```kotlin
    fun main() {
        println("Hello world!")
    }
    ```

    正确执行则说明`maven`项目改造成`kotlin`成功

