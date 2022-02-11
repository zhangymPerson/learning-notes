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

### 编译生成目标语言代码

- java 语言

  `protoc --java_out=./ *.proto`