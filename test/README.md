# 测试

## 开发中的测试

### mock测试

- 概念
    
    就是在测试过程中，对于某些不容易构造或者不容易获取的对象，用一个虚拟的对象来创建以便测试的测试方法。

- Java中的测试框架

    [Mockito](https://github.com/mockito/mockito)
    
    使用Mockito一般分三个步骤：1、模拟测试类所需的外部依赖；2、执行测试代码；3、判断执行结果是否达到预期；
    
- springboot

    MockMvc是由spring-test包提供，实现了对Http请求的模拟，能够直接使用网络的形式，转换到Controller的调用，使得测试速度快、不依赖网络环境。同时提供了一套验证的工具，结果的验证十分方便。

    使用需要导入**spring-boot-starter-test**包

### 单元测试

### 测试框架工具

- postman