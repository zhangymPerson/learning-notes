# hdfs操作简介

    主要参考资料Hadoop权威指南

## 介绍

- 介绍

    Hadoop分布式文件系统(HDFS)被设计成适合运行在通用硬件(commodity hardware)上的分布式文件系统。它和现有的分布式文件系统有很多共同点。但同时，它和其他的分布式文件系统的区别也是很明显的。HDFS是一个高度容错性的系统，适合部署在廉价的机器上。HDFS能提供高吞吐量的数据访问，非常适合大规模数据集上的应用。HDFS放宽了一部分POSIX约束，来实现流式读取文件系统数据的目的。HDFS在最开始是作为Apache Nutch搜索引擎项目的基础架构而开发的。HDFS是Apache Hadoop Core项目的一部分。

    [中文文档](http://hadoop.apache.org/docs/r1.0.4/cn/hdfs_design.html)


## HDFS设计思想

- 超大文件

    指百MB，百G,百T的文件存储集群；

- 流式数据访问

    一次写入，多次读取的设计；
    为分析而生的文件存储系统，读取整个文件的延时比读取文件个别记录的延时更重要

- 商用硬件

    可以部署再廉价的服务器上，有自动恢复的功能；体会不到明显的故障；


- 低时间延迟的数据访问

    时间响应高的数据不适合存储再hdfs上，hdfs是为了高吞吐量的应用优化的，牺牲了响应时间；

- 大量的小文件

    不适合存储太多的小文件

- 多用户写入，任意修改文件

## HDFS中的概念

    
- 数据块

    hdfs默认的数据块大小是128MB,
    
    块比较大的原因是为了最小化寻址时间，

    命令

        hdfs fsck / -files -blocks
    

## NameNode和DataNode


- namenode (管理节点)

    namenode是主节点，是HDFS主从结构中主节点上运行的主要进程，它指导主从结构中的从节点，数据节点(DataNode)执行底层的I/O任务。

    主要记录hdfs上的文件元数据
    
    文件拥有者和权限
    
    文件包含哪些块
    
    每个块保存在哪个DataNode上（由DataNode启动时上报）
    
    **每个块保存在哪个DataNode上，这个信息不会保存在NameNode磁盘上，而是当HDFS系统启动时，DataNode会将此信息上报给NameNode，由NameNode保存在内存中，并且每隔一段时间都会重新上报一次。**

    重要：如果namenode的服务器损坏，则会丢失所有的文件，无法找到datanode中的数据块；

- SecondaryNameNode（SNN）

    它不是NameNode的备份（但可以做一部分备份），它的主要工作是帮助NameNode合并edits日志，减少NameNode的启动时间。

    由于对文件的操作不会直接修改fsimage，而是在edits文件中记录相应操作，所以需要将edits与fsimage合并，而在合并时需要频繁的I/O操作。如果该操作有NameNode自己完成，则计算机需要分配大量资源支持它完成合并，但是NameNode的主要任务是接受客户端读写服务，若大量资源都去支持edits与fsimage合并，那么读写服务就会变得很慢，所以NameNode不做合并，而是由SecondaryNameNode完成，并且HDFS配置时，这两个节点一般配置在不同的电脑上，因此不会相互占用资源。在合并完之后，会得到一个新的fsimage文件，将其传送给NameNode，并替换原始的fsimage文件。

- datanode (工作节点)

    存储数据（Block）

    启动DN线程时，会向NameNode汇报block位置信息

    通过向NameNode发送心跳保持与其联系（3秒一次），如果NameNode 10分钟没有收到DN心跳，则认为该节点已经丢失，并拷贝其上的block到其他的DataNode节点上，保证最小副本数（默认为3个）。


### HDFS命令行接口

    搭建hdfs配置两个重要的参数hdfs
    fs.defaultFS://localhost/;
    dfs.replication:n;//根据需要进行设置，数据块的备份数；

    [hadoop相关的命令](https://github.com/zhangymPerson/learning-notes/blob/master/BigData/Hadoop/hadoop-command.md)


### hdfs 原理

- 上传文件

- 下载文件

- 查看文件

    ![hdfs文件读取api](../../Picture/HDFS%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E8%BF%87%E7%A8%8B.png)
