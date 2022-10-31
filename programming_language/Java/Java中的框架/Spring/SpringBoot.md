# SpringBoot 的笔记

- [返回](./README.md)

## 常用 github 地址

- [Spring Boot 基础教程 - 代码](https://github.com/dyc87112/SpringBoot-Learning)

- [Spring Boot 基础教程](http://blog.didispace.com/Spring-Boot%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B/)

- [基础 helloword 项目 demo](https://github.com/dyc87112/SpringBoot-Learning/tree/master/Chapter1)

- [配置文件详解：自定义属性、随机数、多环境配置等 demo](https://github.com/dyc87112/SpringBoot-Learning/tree/master/Chapter2-1-1)

  各种环境的多配置文件的配置方式

  读取配置文件内容

- [项目运行中添加自定义逻辑的方式](https://github.com/dyc87112/SpringBoot-Learning/tree/master/Chapter2-1-2)

  启动前执行的代码

  启动后执行的代码

  启动过程中执行的代码

- [ Spring Boot 2.0 新特性：配置绑定 2.0 全解析](https://github.com/dyc87112/SpringBoot-Learning/tree/master/Chapter2-2-1)

### springboot 的常见问题

- 启动类上面的注解是@SpringBootApplication，它也是 Spring Boot 的核心注解，主要组合包含了以下 3 个注解：

  @SpringBootConfiguration：组合了 @Configuration 注解，实现配置文件的功能。

  @EnableAutoConfiguration：打开自动配置的功能，也可以关闭某个自动配置的选项，如关闭数据源自动配置功能： @SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })。

  @ComponentScan：Spring 组件扫描。
