# Java项目和docker

## springboot 打包 - 发布到 docker

- 创建好普通springboot项目 可以单独 发布的项目

- 添加mvn - docker 插件

    修改pom.xml的配置

    在 ```<build>  <plugins>``` 标签下添加下面的插件

    ```xml
    <!--打包docker的插件-->
    <plugin>
        <groupId>com.spotify</groupId>
        <artifactId>docker-maven-plugin</artifactId>
        <version>1.0.0</version>
        <configuration>
        <!-- 在docker运行时要用的，只是一个前缀而已，就像包名一样,可自己任意定义此名称 -->
            <imageName>${docker.image.prefix}/${project.artifactId}</imageName>
            <!--docker docker的Dockerfile文件所在的文件夹位置  不要放到 target中 因为mvn clean 会清理 Dockerfile文件 这个文件需自己创建 -->
            <dockerDirectory>${basedir}/docker</dockerDirectory>
            <!--配置docker读取的jar的位置,运行docker打包命令会自动复制配置好的源码jar包到指定的Dockerfile位置-->
            <resources>
                <resource>
                    <targetPath>/</targetPath>
                    <directory>${project.build.directory}</directory>
                    <include>${project.build.finalName}.jar</include>
                </resource>
            </resources>
        </configuration>
    </plugin>
    ```
- 打包命令
    ```sh
    mvn clean package docker:build -Dmaven.test.skip=true
    ```
- 注意事项

    配置文件中的各个参数可以百度自行理解

    Dockerfile文件需要和```<dockerDirectory>${basedir}/docker</dockerDirectory>```配置一致,且手动创建 否则会报错

    Dockerfile文件内容 可自行修改

    ```dockerfile
    FROM frolvlad/alpine-oraclejdk8:slim
    VOLUME /tmp
    ADD springbootlearingone-1.0-SNAPSHOT.jar app.jar
    ENTRYPOINT ["java","-jar","/app.jar"]
    ```