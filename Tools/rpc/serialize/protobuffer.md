# Protocol Buffers 协议

## 介绍说明

- [github](https://github.com/protocolbuffers)

- [官网](https://developers.google.com/protocol-buffers/)

- [百度百科](https://baike.baidu.com/item/protocol%20buffer/1664400)

## 使用方式

### 编译工具 protoc

- 需要先下载安装此工具

- [下载地址](https://github.com/protocolbuffers/protobuf/releases/)

  https://github.com/protocolbuffers/protobuf/releases/

### 编写 proto 文件

- eg

  ```protobuf

  syntax = "proto3";
  package tutorial;

  import "google/protobuf/timestamp.proto";
  // [END declaration]

  // [START java_declaration]
  option java_multiple_files = true;
  option java_package = "com.example.tutorial.protos";
  option java_outer_classname = "AddressBookProtos";
  // [END java_declaration]

  // [START csharp_declaration]
  option csharp_namespace = "Google.Protobuf.Examples.AddressBook";
  // [END csharp_declaration]

  // [START go_declaration]
  option go_package = "github.com/protocolbuffers/protobuf/examples/go/tutorialpb";
  // [END go_declaration]

  // [START messages]
  message Person {
    string name = 1;
    int32 id = 2;  // Unique ID number for this person.
    string email = 3;

    enum PhoneType {
      MOBILE = 0;
      HOME = 1;
      WORK = 2;
    }

    message PhoneNumber {
      string number = 1;
      PhoneType type = 2;
    }

    repeated PhoneNumber phones = 4;

    google.protobuf.Timestamp last_updated = 5;
  }

  // Our address book file is just one of these.
  message AddressBook {
    repeated Person people = 1;
  }
  ```

### 类型介绍

- [官网介绍](https://developers.google.com/protocol-buffers/docs/proto3)

#### message

- message 消息

  ```proto
  syntax = "proto3";
  //定义一个消息
  message MessageName {
      string string = 1;
  }
  ```

#### server

- server 服务

  ```proto
  message String{
      string string = 1;
  }

  message Boolean{
      bool bool = 1;
  }

  service StringService{
      rpc IsEmpty(String) returns (Boolean);
  }

  ```

#### rpc

- rpc 定义一个服务

  **rpc 接口的参数和返回值必须是 message 类型**

- proto 封装好的基本类型

  **protobuf 自己定义好了基本类型的封装 message：Int32Value、BoolValue 等**

  ```proto
  import "google/protobuf/wrappers.proto";

  service UserSevice {
      rpc getById(google.protobuf.Int32Value) returns (User);
  }
  ```

### 编译生成目标语言代码

- java 语言

  `protoc --java_out=./ *.proto`
