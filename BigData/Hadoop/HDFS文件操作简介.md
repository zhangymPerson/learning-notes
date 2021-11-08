# hdfs 操作简介

    主要参考资料Hadoop权威指南

## 介绍

- 介绍

  Hadoop 分布式文件系统(HDFS)被设计成适合运行在通用硬件(commodity hardware)上的分布式文件系统。它和现有的分布式文件系统有很多共同点。但同时，它和其他的分布式文件系统的区别也是很明显的。HDFS 是一个高度容错性的系统，适合部署在廉价的机器上。HDFS 能提供高吞吐量的数据访问，非常适合大规模数据集上的应用。HDFS 放宽了一部分 POSIX 约束，来实现流式读取文件系统数据的目的。HDFS 在最开始是作为 Apache Nutch 搜索引擎项目的基础架构而开发的。HDFS 是 Apache Hadoop Core 项目的一部分。

  [中文文档](http://hadoop.apache.org/docs/r1.0.4/cn/hdfs_design.html)

## HDFS 设计思想

- 超大文件

  指百 MB，百 G,百 T 的文件存储集群；

- 流式数据访问

  一次写入，多次读取的设计；
  为分析而生的文件存储系统，读取整个文件的延时比读取文件个别记录的延时更重要

- 商用硬件

  可以部署再廉价的服务器上，有自动恢复的功能；体会不到明显的故障；

- 低时间延迟的数据访问

  时间响应高的数据不适合存储再 hdfs 上，hdfs 是为了高吞吐量的应用优化的，牺牲了响应时间；

- 大量的小文件

  不适合存储太多的小文件

- 多用户写入，任意修改文件

## HDFS 中的概念

- 数据块

  hdfs 默认的数据块大小是 128MB,

  块比较大的原因是为了最小化寻址时间，

  命令

        hdfs fsck / -files -blocks

## NameNode 和 DataNode

- namenode (管理节点)

  namenode 是主节点，是 HDFS 主从结构中主节点上运行的主要进程，它指导主从结构中的从节点，数据节点(DataNode)执行底层的 I/O 任务。

  主要记录 hdfs 上的文件元数据

  文件拥有者和权限

  文件包含哪些块

  每个块保存在哪个 DataNode 上（由 DataNode 启动时上报）

  **每个块保存在哪个 DataNode 上，这个信息不会保存在 NameNode 磁盘上，而是当 HDFS 系统启动时，DataNode 会将此信息上报给 NameNode，由 NameNode 保存在内存中，并且每隔一段时间都会重新上报一次。**

  重要：如果 namenode 的服务器损坏，则会丢失所有的文件，无法找到 datanode 中的数据块；

- SecondaryNameNode（SNN）

  它不是 NameNode 的备份（但可以做一部分备份），它的主要工作是帮助 NameNode 合并 edits 日志，减少 NameNode 的启动时间。

  由于对文件的操作不会直接修改 fsimage，而是在 edits 文件中记录相应操作，所以需要将 edits 与 fsimage 合并，而在合并时需要频繁的 I/O 操作。如果该操作有 NameNode 自己完成，则计算机需要分配大量资源支持它完成合并，但是 NameNode 的主要任务是接受客户端读写服务，若大量资源都去支持 edits 与 fsimage 合并，那么读写服务就会变得很慢，所以 NameNode 不做合并，而是由 SecondaryNameNode 完成，并且 HDFS 配置时，这两个节点一般配置在不同的电脑上，因此不会相互占用资源。在合并完之后，会得到一个新的 fsimage 文件，将其传送给 NameNode，并替换原始的 fsimage 文件。

- datanode (工作节点)

  存储数据（Block）

  启动 DN 线程时，会向 NameNode 汇报 block 位置信息

  通过向 NameNode 发送心跳保持与其联系（3 秒一次），如果 NameNode 10 分钟没有收到 DN 心跳，则认为该节点已经丢失，并拷贝其上的 block 到其他的 DataNode 节点上，保证最小副本数（默认为 3 个）。

### HDFS 命令行接口

    搭建hdfs配置两个重要的参数hdfs
    fs.defaultFS://localhost/;
    dfs.replication:n;//根据需要进行设置，数据块的备份数；

    [hadoop相关的命令](https://github.com/zhangymPerson/learning-notes/blob/master/BigData/Hadoop/hadoop-command.md)

### hdfs 原理

- 上传文件

- 下载文件

- 查看文件

  ![hdfs文件读取api](../../Picture/HDFS%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E8%BF%87%E7%A8%8B.png)
