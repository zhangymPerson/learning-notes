# 错误记录

- 跳过test编译

    **windows下必须加引号**
     mvn clean package -D'maven.test.skip=true'


- maven 项目多模块打包时报错，找不到子模块问题

    log: Failed to execute goal on project/Could not resolve dependencies for project

    解决方法：

        maven 工程，父子类关系，子类关系互相引用时，必须先父类工程install一下，才能编译子类模块
        
        需要把parent工程，也就是package是pom的那个工程先install一下；之后再install公共引入的模块，最后就可以单独编译子模块。

        不用install，直接编译parent项目；这种方式只能在parent项目下进行，不能单独编译子模块。


- 子模块无法引入父模块中的pom.xml文件时，或者jar包无法引入时，检查子模块的pom.xml文件

    修改子pom.xml文件的 \<parent\>标签
    ```xml
     <parent>
        <artifactId>baseutil</artifactId>
        <groupId>cn.danao</groupId>
        <version>1.0-SNAPSHOT</version>
        <!-- maven父子项目依赖关系无法建立，需指定父pom.xml文件的位置 -->
        <relativePath>./pom.xml</relativePath>
    </parent>
    ```

- 如果父子模块中的单独处理。则
    
    父模块中的pom.xml文件需要
    ```xml
        <!--父pom.xml文件如果使用 dependencyManagement 标签，
        则 子maven项目不能直接使用父中引入的jar包，
        而直接使用dependencies则可以使用不需要再次引入-->
        <dependencyManagement>
            <dependencies>
                <dependency>
                    <groupId>junit</groupId>
                    <artifactId>junit</artifactId>
                    <version>4.12</version>
                    <!--<scope>compile</scope>-->
                </dependency>
                <!--lombok-->
                <dependency>
                    <groupId>org.projectlombok</groupId>
                    <artifactId>lombok</artifactId>
                    <version>${lombok.version}</version>
                    <!--<scope>provided</scope>-->
                </dependency>
            </dependencies>
        </dependencyManagement>
    ```