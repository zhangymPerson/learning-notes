# Mycat的安装部署使用
---
### Mycat配置入门

- 配置：

    --bin 启动目录

    --conf 配置文件存放配置文件：

    ```
    --server.xml：是Mycat服务器参数调整和用户授权的配置文件。

    --schema.xml：是逻辑库定义和表以及分片定义的配置文件。

    --rule.xml：  是分片规则的配置文件，分片规则的具体一些参数信息单独存放为文件，也在这个目录下，配置文件修改需要重启MyCAT。

    --log4j.xml： 日志存放在logs/log中，每天一个文件，日志的配置是在conf/log4j.xml中，根据自己的需要可以调整输出级别为debug                           debug级别下，会输出更多的信息，方便排查问题。

    --autopartition-long.txt,partition-hash-int.txt,sequence_conf.properties， sequence_db_conf.properties 分片相关的id分片规则配置文件

    --lib	    MyCAT自身的jar包或依赖的jar包的存放目录。

    --logs        MyCAT日志的存放目录。日志存放在logs/log中，每天一个文件
    
    ```
    ![配置说明](https://camo.githubusercontent.com/af0b8c0147e92f5e63e83f1558b39e178fb4d50c/687474703a2f2f736f6e677769652e636f6d2f61747461636865642f696d6167652f32303136303230352f32303136303230353136343535385f3135342e706e67)

- 逻辑库配置：

    配置server.xml

    添加两个mycat逻辑库：user,pay: system 参数是所有的mycat参数配置，比如添加解析器：defaultSqlParser，其他类推 user 是用户参数。
    ```xml
    <system>

        <property name="defaultSqlParser">druidparser</property>

    </system>

    <user name="mycat">

        <property name="password">mycat</property>

        <property name="schemas">user,pay</property>

    </user>
    ```

    编辑schema.xml

    修改dataHost和schema对应的连接信息，user,pay 垂直切分后的配置如下所示：

    schema 是实际逻辑库的配置，user，pay分别对应两个逻辑库，多个schema代表多个逻辑库。

    dataNode是逻辑库对应的分片，如果配置多个分片只需要多个dataNode即可。

    dataHost是实际的物理库配置地址，可以配置多主主从等其他配置，多个dataHost代表分片对应的物理库地址，下面的writeHost、readHost代表该分片是否配置多写，主从，读写分离等高级特性。

    以下例子配置了两个writeHost为主从。
    ```xml
    <schema name="user" checkSQLschema="false" sqlMaxLimit="100" dataNode="user" />
    <schema name="pay"  checkSQLschema="false" sqlMaxLimit="100" dataNode="pay" >
    <table name="order" dataNode="pay1,pay2" rule="rule1"/>
    </schema>

    <dataNode name="user" dataHost="host" database="user" />
    <dataNode name="pay1" dataHost="host" database="pay1" />
    <dataNode name="pay2" dataHost="host" database="pay2" />

    <dataHost name="host" maxCon="1000" minCon="10" balance="0"
    writeType="0" dbType="mysql" dbDriver="native">
    <heartbeat>select 1</heartbeat>
    <!-- can have multi write hosts -->
    <writeHost host="hostM1" url="ip:port" user="root" password="root" />
    <writeHost host="hostM2" url="ip:port" user="root" password="root" />
    </dataHost>
    ```
    分片规则配置：

    该规则配置了order表的数据切分方式，及数据切分字段。

    ```xml
    <mycat:rule xmlns:mycat="http://org.opencloudb/"> 
    <tableRule name="rule1">
        <rule>
        <columns>user_id</columns>
        <algorithm>func1</algorithm>
        </rule>
    </tableRule>
    <function name="func1" class="org.opencloudb.route.function.PartitionByLong">
        <property name="partitionCount">2</property>
        <property name="partitionLength">512</property>
    </function>
    </mycat:rule>
    ```