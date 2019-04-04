# springboot 搭建过程

- 官方maven搭建

	- [网站](https://start.spring.io/)

- 基本的pom.xml文件

	```xml
	<?xml version="1.0" encoding="UTF-8"?>
	<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
		<modelVersion>4.0.0</modelVersion>

		<!--自定义部分-->
		<!--可以使用各种工具构建-->
		<groupId>com.example</groupId>
		<artifactId>myproject</artifactId>
		<version>0.0.1-SNAPSHOT</version>

		<!-- Inherit defaults from Spring Boot -->
		<parent>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-parent</artifactId>
			<!--版本可以选择-->
			<version>2.1.3.RELEASE</version>
		</parent>

		<!--
			自定义变量，父子间pom.xml 子可以使用父中的变量
			创建方式<properties>标签中创建
			<java.version>1.8</java.version>
			使用方式 ${java.version}
		-->
		<properties>
			<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
			<java.version>1.8</java.version>
		</properties>

		<!-- Add typical dependencies for a web application -->
		<dependencies>

			<dependency>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-starter</artifactId>
			</dependency>

			<dependency>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-starter-test</artifactId>
				<scope>test</scope>
			</dependency>
			<dependency>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-starter-web</artifactId>
			</dependency>
		</dependencies>

		<!-- Package as an executable jar -->
		<build>
			<plugins>
				<plugin>
					<groupId>org.springframework.boot</groupId>
					<artifactId>spring-boot-maven-plugin</artifactId>
				</plugin>
			</plugins>
		</build>
	</project>
	```

- 创建启动类

	在${project-path}/src/main/java

	ApplicationName.java
	```java
	//三个注解，下面两个可以没有，
	//第二个配置是跳过数据库的自动配置启动
	@SpringBootApplication
	@EnableAutoConfiguration(exclude={DataSourceAutoConfiguration.class})
	@ServletComponentScan
	public class ApplicationName {

		public static void main(String[] args) {
			SpringApplication.run(ApplicationName.class, args);
		}

	}
	```

- 创建请求

	在${project-path}/src/main/java
	
	创建package controller
	
	创建类HelloController

	```java
	import org.springframework.web.bind.annotation.RequestMapping;
	import org.springframework.web.bind.annotation.RestController;

	//controller基本注解
	@RestController
	//配置路由
	@RequestMapping("/test")
	public class HelloController {

		//配置请求路由
		@RequestMapping("/hello")
		public String index() {
			return "Hello World";
		}
	}
	```


- 启动 ApplicationName 类 主函数即可启动该springboot项目


- 查看下jar包的依赖关系

	```sh
	//在项目路径下(pom.xml文件所在位置)
	mvn dependency:tree。该命令会打印一个当前项目的依赖树。
	```

- springboot项目热部署 (不重启自动加载)

	添加maven得jar包支持
	```
    <!-- springboot工具 修改代码后不需重启即生效 -->
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>springloaded</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-devtools</artifactId>
        <!-- 这个需要为 true 热部署才有效 -->
        <optional>true</optional>
    </dependency>
	```
	
	idea 设置

	- “File” -> “Settings” -> “Build,Execution,Deplyment” -> “Compiler”，选中打勾 “Build project automatically” 。

	- 组合键：“Shift+Ctrl+Alt+/” ，选择 “Registry” ，选中打勾 “compiler.automake.allow.when.app.running”

- springboot 多配置文件选择

	```
	# 定义多个配置文件
	# 配置文件说明
	application.properties      默认配置文件
	application-dev.properties  开发环境配置
	application-test.properties 测试环境配置
	application-prod.properties 生产环境配置
	```
- 主配置文件

	```properties
    
	#application.properties
     
    添加配置
    #后面添加要选择得配置文件
    #spring.profiles.active=default
    #spring.profiles.active=dev
    #spring.profiles.active=test
    spring.profiles.active=prod
	```