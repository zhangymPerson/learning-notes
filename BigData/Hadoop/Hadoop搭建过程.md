# Hadoop系统搭建

### 前提 

- 系统 先确定 主 - 从 服务器

- 服务器之间做时间同步

- 服务器之间做免密登陆 - 对自己也要免密登陆

- 需要提前安装好jdk环境


- 下载Hadoop 

- 配置

    主要的配置文件  core-site.xml  hdfs-site.xml  yarn-site.xml

- core-site.xml

    集群核心配置

- hdfs-site.xml

    hdfs系统的相关参数的配置

- yarn-site.xml

    yarn相关的配置

- 启动后需要注意 

    Hadoop本地库校验

        hadoop  checknative  -a
    如果返回 -1 则说明集群无法正常的使用本地库

    编译64位的系统库

    配置在 hadoop-env .sh 文件中
        
        export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
        export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib" 

- 启用debug模式进行调试

    -配置环境变量，重启集群即可

        export HADOOP_ROOT_LOGGER=DEBUG,console
 
