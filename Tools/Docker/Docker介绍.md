# Docker

## 概念

- 介绍

  Docker 是一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口。

  Docker 是 PaaS 提供商 dotCloud 开源的一个基于 LXC 的高级容器引擎，源代码托管在 Github 上, 基于 go 语言并遵从 Apache2.0 协议开源。

  Docker 架构
  Docker 使用客户端-服务器 (C/S) 架构模式，使用远程 API 来管理和创建 Docker 容器。Docker 容器通过 Docker 镜像来创建。容器与镜像的关系类似于面向对象编程中的对象与类。

  | Docker | 面向对象 |
  | ------ | -------- |
  | 容器   | 对象     |
  | 镜像   | 类       |

  Docker 采用 C/S 架构 Docker daemon 作为服务端接受来自客户的请求，并处理这些请求（创建、运行、分发容器）。

  客户端和服务端既可以运行在一个机器上，也可通过 socket 或者 RESTful API 来进行通信。

  Docker daemon 一般在宿主主机后台运行，等待接收来自客户端的消息。

  Docker 客户端则为用户提供一系列可执行命令，用户用这些命令实现跟 Docker daemon 交互。

  [Docker-百度百科](https://baike.baidu.com/item/Docker/13344470)

  [Docker-Docker 中文网](http://www.docker.org.cn/index.mhtml)

## Docker 原理

## 自定义镜像
