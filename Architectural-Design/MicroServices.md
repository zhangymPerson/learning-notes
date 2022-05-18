# 微服务(micro-services)

## 微服务的理论

- [微服务论坛](https://microservices.io/)

- [微服务概念理论-英文](https://martinfowler.com/articles/microservices.html)

- 定义

  In short, the **microservice architectural style** is an approach to developing **a single application** as a suite of small services, each **running in its own process** and **communicating with lightweight mechanisms**, often an HTTP resource API. These services are built around business capabilities and independently deployable by fully automated deployment machinery. There is a bare minimum of centralized management of these services, which may be written in different programming languages and use different data storage technologies.

- 要点

  - 单独拆分成单一的服务，模块之间独立

  - 项目运行在独立的进程中，互相不干扰

  - 项目使用轻量级的交互协议，简单易于实现 常用 http rpc 等

## 企业应用组成

- 企业应用 Enterprise Applications

  Enterprise Applications are often built in three main parts: a client-side user interface (consisting of HTML pages and javascript running in a browser on the user's machine) a database (consisting of many tables inserted into a common, and usually relational, database management system), and a server-side application. The server-side application will handle HTTP requests, execute domain logic, retrieve and update data from the database, and select and populate HTML views to be sent to the browser. This server-side application is a monolith - a single logical executable. Any changes to the system involve building and deploying a new version of the server-side application.

- 要点

  前端(客户端)

  DB(数据库系统)

  后台服务逻辑

- All in one 点单应用的问题 整体应用的问题

  云的发展，导致软件发布变更周期要求更短，但是每一次小的改动都需要整体编译，影响整个项目的发布进度，并且模块之间容易互相产生影响，随着时间的推移，软件开发者很难保持原有好的模块架构，使得一个模块的变更很难不会影响到其它的模块，而且在扩展方面也只能进行整体的扩展，而不能根据进行部分的扩展。

- 微服务起源很早，但是没引起足够的重视

- 微服务的实现框架

  [springcloud 官方 github 地址](https://github.com/spring-cloud)

  [dubbo-apache 孵化](https://github.com/apache/incubator-dubbo)
