# Java中的jar脚本编写

- 使用maven创建项目

    找到要创建的文件目录

    使用命令
    
    ```sh
    # 构建命令
    mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=myapp -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

    # 进入项目目录下
    # 清理命令
    mvn clean 
    # 构建
    mvn install
    ```

    


- 在pom中添加构建信息

    ```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>1.2.1</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <!--这个位置填写jar包启动入口的类名 全路径名-->
                                    <mainClass>com.cooix.util.SystemUtil</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
    ```