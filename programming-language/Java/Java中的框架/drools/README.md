# drools

- Java的规则引擎框架

- [github地址](https://github.com/kiegroup/drools)

    https://github.com/kiegroup/drools

## 基本介绍

Drools是一个业务管理系统，基于前向链接和后向链接的推理规则引擎，可以快速可靠地评估业务规则和进行复杂事件处理。

## 官方使用demo

- [官方样例](https://github.com/kiegroup/drools/tree/master/drools-examples)

    https://github.com/kiegroup/drools/tree/master/drools-examples

## 主要开发步骤

- 导入maven配置

- 编写配置文件

    在`~/src/main/resources/META-INF/`下
    编写 `kmodule.xml` 文件

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <kmodule xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns="http://www.drools.org/xsd/kmodule">
        <!-- 包根路径基于 ~/src/main/resources/  -->
        <!-- 即：~/src/main/resources/org/drools/examles/helloword/下的文件 -->
        <kbase packages="org.drools.examples.helloworld">
            <!-- 这个配置会在代码中使用 会自动匹配到包下的规则文件 -->
            <ksession name="HelloWorldKS"/>
        </kbase>
    </kmodule>
    ```
- 规则文件 **.drl 文件

