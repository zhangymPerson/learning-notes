# grpc

## 定义介绍

### RPC

- rpc

  RPC（Remote Procedure Call）—远程过程调用，它是一种通过网络从远程计算机程序上请求服务，而不需要了解底层网络技术的协议。

- [百度百科](https://baike.baidu.com/item/%E8%BF%9C%E7%A8%8B%E8%BF%87%E7%A8%8B%E8%B0%83%E7%94%A8/7854346?fromtitle=RPC&fromid=609861&fr=aladdin)

### grpc 介绍

- 定义

  gRPC (gRPC Remote Procedure Calls) 是 Google 发起的一个开源远程过程调用系统，该系统基于 HTTP/2 协议传输，介绍 gRPC 的基础概念，首先通过关系图直观展示这些基础概念之间关联，介绍异步 gRPC 的 Server 和 Client 的逻辑；然后介绍 RPC 的类型，阅读和抓包分析 gRPC 的通信过程协议，gRPC 上下文；最后分析 grpc.pb.h 文件的内容，包括 Stub 的能力、Service 的种类以及与核心库的关系。

- [官网](https://grpc.io/)

- 基本原理

  ![](../.../../Picture/../../../picture/grpc.svg)

- protobuffer

  详细文档：https://developers.google.com/protocol-buffers/docs/overview
  版本下载：https://developers.google.com/protocol-buffers/docs/downloads

  proto 文件定义了服务 Greeter 和 API SayHello：

  ```proto
  // helloworld.proto
  // The greeting service definition.
  service Greeter {
    // Sends a greeting
    rpc SayHello (HelloRequest) returns (HelloReply) {}
  }
  ```

### java 和 go 的跨语言调用

### 基础介绍

- 各个语言支持情况

  | Language    | OS                     | Compilers / SDK               |
  | ----------- | ---------------------- | ----------------------------- |
  | **Go**      | Windows, Linux, Mac    | Go 1.13+                      |
  | **Java**    | Windows, Linux, Mac    | Java 8+ (KitKat+ for Android) |
  | C/C++       | Linux, Mac             | GCC 6.3+, Clang 6+            |
  | C/C++       | Windows 10+            | Visual Studio 2017+           |
  | C#          | Linux, Mac             | .NET Core, Mono 4+            |
  | C#          | Windows 10+            | .NET Core, NET 4.5+           |
  | Dart        | Windows, Linux, Mac    | Dart 2.12+                    |
  | Kotlin      | Windows, Linux, Mac    | Kotlin 1.3+                   |
  | Node.js     | Windows, Linux, Mac    | Node v8+                      |
  | Objective-C | macOS 10.10+, iOS 9.0+ | Xcode 12+                     |
  | PHP         | Linux, Mac             | PHP 7.0+                      |
  | Python      | Windows, Linux, Mac    | Python 3.5+                   |
  | Ruby        | Windows, Linux, Mac    | Ruby 2.3+                     |

#### java 端

- 项目创建

- 版本`jdk 1.8` 构建工具`gradle 7.5`

- 编写 proto 文件

- 使用 gradle 插件 生成 java 代码 和 grpc 代码

- java 实现 extends \*ImplBase 类，并且重写 proto 文件中的 rpc 函数

- java 使用 netty 作为基础通信包 注册服务端并启动项目

- java 实现客户端 并使用 netty 作为基础通信包 发送请求

#### go 端

- 项目创建

- 版本`go 1.18.3` 构建工具`go mod`

- 使用 protoc 工具生成 go 的代码 使用 protoc-gen-go 生成 go 的 grpc 样例代码

  `protoc -I proto/ proto/product_info.proto --go_out=go/server/ --go-grpc_out=go/server/`

- go 实现 server 方法

- 运行 server 方法

- go 实现客户端

- 运行 client 代码

- 代码样例 github

  [grpc-demo](https://github.com/CatNum/grpc_samples)
