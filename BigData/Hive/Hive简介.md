# hive 简介

- [阿里云教程](https://edu.aliyun.com/course/1531)


## hive说明

- [Hive-百度百科](https://baike.baidu.com/item/hive/67986)
- [github地址](https://github.com/apache/hive)
- [Hive优秀博客](https://blog.csdn.net/youyou1543724847/article/details/83446908)
- 定义

    数据仓库工具
    
    hive是基于Hadoop的一个数据仓库工具，可以将结构化的数据文件映射为一张数据库表，并提供简单的sql查询功能，可以将sql语句转换为MapReduce任务进行运行。 其优点是学习成本低，可以通过类SQL语句快速实现简单的MapReduce统计，不必开发专门的MapReduce应用，十分适合数据仓库的统计分析。

    Hive是建立在 Hadoop 上的数据仓库基础构架。它提供了一系列的工具，可以用来进行数据提取转化加载（ETL），这是一种可以存储、查询和分析存储在 Hadoop 中的大规模数据的机制。Hive 定义了简单的类 SQL 查询语言，称为 HQL，它允许熟悉 SQL 的用户查询数据。同时，这个语言也允许熟悉 MapReduce 开发者的开发自定义的 mapper 和 reducer 来处理内建的 mapper 和 reducer 无法完成的复杂的分析工作。


- Hive是map-reduce的封装

- Hive 数据分析 类sql != sql (类似不完全一样)   不能存储数据，只是计算引擎，基于map-reduce; 


    原理: hive sql解析引擎 - 将sql解析成一个/多个map-reduce任务;最后在hadoop上运行; 
    
    表是纯粹的逻辑表  不支持修改和删除;(后续支持)  对修改和删除支持不到位

    数据分割 空格 \t  \001  
    列分割符 \n

    读取数据方法 TextFile SequenceFile(二进制格式，序列化和反序列化) RCFile 是hive专门推出的面向列的存储格式

- 读时模式-写时模式

    RDBMS是写模式
    Hive是读模式

- Hive中主要包含以下几种数据模型：Table(表)，External Table(外部表)，Partition(分区)，Bucket(桶)

- 分区分表  方便查询  方便采样

