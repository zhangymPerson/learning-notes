# Hadoop系统搭建

### 前提 

- 系统 先确定 主 - 从 服务器

- 服务器之间做时间同步

- 服务器之间做免密登陆 - 对自己也要免密登陆

- 需要提前安装好jdk环境


- 下载Hadoop 

- 最简单的配置


    ```xml
    <!-- core-site.xml -->
    <configuration>
            <property>
                <name>fs.defaultFS</name>
                <value>hdfs://master:9000</value>
            </property>
            <property>
                <name>hadoop.tmp.dir</name>
                <value>/data/hadoop/tmp</value>
            </property>
    </configuration>

    <!-- hdfs-site.xml -->
    <configuration>
            <property>
                <name>dfs.namenode.name.dir</name>
                <value>file:/usr/local/src/hadoop/hdfs/name</value>
            </property>
            <property>
                <name>dfs.datanode.data.dir</name>
                <value>file:/usr/local/src/hadoop/hdfs/data</value>
            </property>
            <property>
                <name>dfs.replication</name>
                <value>1</value>
            </property>
    </configuration>

    <!-- maprdu-site.xml -->
    <configuration>
            <property>
                <name>mapreduce.framework.name</name>
                <value>yarn</value>
            </property>
    </configuration>
    <!-- yarn-site.xml -->
    <configuration>
            <property>
                <name>yarn.nodemanager.aux-services</name>
                <value>mapreduce_shuffle</value>
            </property>
            <property>
                <name>yarn.resourcemanager.hostname</name>
                <value>master</value>
            </property>
    </configuration>

    vi slaves

    配置从节点

    ```















### 配置 (重要 反复调整调优)

    主要的配置文件  core-site.xml  hdfs-site.xml  yarn-site.xml

- core-site.xml

    集群核心配置

    ```xml
    <configuration>
        <property>
            <name>fs.defaultFS</name>
            <value>hdfs://192.168.1.100:900</value>
            <description>192.168.1.100为服务器IP地址，其实也可以使用主机名</description>
        </property>
        <property>
            <name>io.file.buffer.size</name>
            <value>131072</value>
            <description>该属性值单位为KB，131072KB即为默认的128M</description>
        </property>
    </configuration>
    ```




- hdfs-site.xml

    hdfs系统的相关参数的配置
    ```xml
    <configuration>
        <property>
            <name>dfs.replication</name>
            <value>1</value>
            <description>分片数量，伪分布式将其配置成1即可</description>
        </property>
        <property>
            <name>dfs.namenode.name.dir</name>
            <value>file:/usr/local/hadoop/tmp/namenode</value>
            <description>命名空间和事务在本地文件系统永久存储的路径</description>
        </property>
        <property>
            <name>dfs.namenode.hosts</name>
            <value>datanode1, datanode2</value>
            <description>datanode1, datanode2分别对应DataNode所在服务器主机名</description>
        </property>
        <property>
            <name>dfs.blocksize</name>
            <value>268435456</value>
            <description>大文件系统HDFS块大小为256M，默认值为64M</description>
        </property>
        <property>
            <name>dfs.namenode.handler.count</name>
            <value>100</value>
            <description>更多的NameNode服务器线程处理来自DataNodes的RPCS</description>
        </property>
        <property>
            <name>dfs.datanode.data.dir</name>
            <value>file:/usr/local/hadoop/tmp/datanode</value>
            <description>DataNode在本地文件系统中存放块的路径</description>
        </property>
    </configuration>
    ```
- yarn-site.xml

    yarn相关的配置
    
    配置ResourceManager 和 NodeManager:
    ```xml
    <configuration>
        <property>
            <name>yarn.resourcemanager.address</name>
            <value>192.168.1.100:8081</value>
            <description>IP地址192.168.1.100也可替换为主机名</description>
        </property>
        <property>
            <name>yarn.resourcemanager.scheduler.address</name>
            <value>192.168.1.100:8082</value>
            <description>IP地址192.168.1.100也可替换为主机名</description>
        </property>
        <property>
            <name>yarn.resourcemanager.resource-tracker.address</name>
            <value>192.168.1.100:8083</value>
            <description>IP地址192.168.1.100也可替换为主机名</description>
        </property>
        <property>
            <name>yarn.resourcemanager.admin.address</name>
            <value>192.168.1.100:8084</value>
            <description>IP地址192.168.1.100也可替换为主机名</description>
        </property>
        <property>
            <name>yarn.resourcemanager.webapp.address</name>
            <value>192.168.1.100:8085</value>
            <description>IP地址192.168.1.100也可替换为主机名</description>
        </property>
        <property>
            <name>yarn.resourcemanager.scheduler.class</name>
            <value>FairScheduler</value>
            <description>常用类：CapacityScheduler、FairScheduler、orFifoScheduler</description>
        </property>
        <property>
            <name>yarn.scheduler.minimum</name>
            <value>100</value>
            <description>单位：MB</description>
        </property>
        <property>
            <name>yarn.scheduler.maximum</name>
            <value>256</value>
            <description>单位：MB</description>
        </property>
        <property>
            <name>yarn.resourcemanager.nodes.include-path</name>
            <value>nodeManager1, nodeManager2</value>
            <description>nodeManager1, nodeManager2分别对应服务器主机名</description>
        </property>
    </configuration>
    ```


配置NodeManager

    ```xml
    <configuration>
        <property>
            <name>yarn.nodemanager.resource.memory-mb</name>
            <value>256</value>
            <description>单位为MB</description>
        </property>
        <property>
            <name>yarn.nodemanager.vmem-pmem-ratio</name>
            <value>90</value>
            <description>百分比</description>
        </property>
        <property>
            <name>yarn.nodemanager.local-dirs</name>
            <value>/usr/local/hadoop/tmp/nodemanager</value>
            <description>列表用逗号分隔</description>
        </property>
        <property>
            <name>yarn.nodemanager.log-dirs</name>
            <value>/usr/local/hadoop/tmp/nodemanager/logs</value>
            <description>列表用逗号分隔</description>
        </property>
        <property>
            <name>yarn.nodemanager.log.retain-seconds</name>
            <value>10800</value>
            <description>单位为S</description>
        </property>
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce-shuffle</value>
            <description>Shuffle service 需要加以设置的MapReduce的应用程序服务</description>
        </property>
    </configuration>
    ```

- mapred-site.xml

    配置mapreduce
    ```xml
    <configuration>
        <property>
            <name> mapreduce.framework.name</name>
            <value>yarn</value>
            <description>执行框架设置为Hadoop YARN</description>
        </property>
        <property>
            <name>mapreduce.map.memory.mb</name>
            <value>1536</value>
            <description>对maps更大的资源限制的</description>
        </property>
        <property>
            <name>mapreduce.map.java.opts</name>
            <value>-Xmx2014M</value>
            <description>maps中对jvm child设置更大的堆大小</description>
        </property>
        <property>
            <name>mapreduce.reduce.memory.mb</name>
            <value>3072</value>
            <description>设置 reduces对于较大的资源限制</description>
        </property>
        <property>
            <name>mapreduce.reduce.java.opts</name>
            <value>-Xmx2560M</value>
            <description>reduces对 jvm child设置更大的堆大小</description>
        </property>
        <property>
            <name>mapreduce.task.io.sort</name>
            <value>512</value>
            <description>更高的内存限制，而对数据进行排序的效率</description>
        </property>
        <property>
            <name>mapreduce.task.io.sort.factor</name>
            <value>100</value>
            <description>在文件排序中更多的流合并为一次</description>
        </property>
        <property>
            <name>mapreduce.reduce.shuffle.parallelcopies</name>
            <value>50</value>
            <description>通过reduces从很多的map中读取较多的平行副本</description>
        </property>
    </configuration>
    ```

配置mapreduce的JobHistory服务器

    ```xml
    <configuration>
        <property>
            <name> mapreduce.jobhistory.address</name>
            <value>192.168.1.100:10200</value>
            <description>IP地址192.168.1.100可替换为主机名</description>
        </property>
        <property>
            <name>mapreduce.jobhistory.webapp.address</name>
            <value>192.168.1.100:19888</value>
            <description>IP地址192.168.1.100可替换为主机名</description>
        </property>
        <property>
            <name>mapreduce.jobhistory.intermediate-done-dir</name>
            <value>/usr/local/hadoop/mr­history/tmp</value>
            <description>在历史文件被写入由MapReduce作业</description>
        </property>
        <property>
            <name>mapreduce.jobhistory.done-dir</name>
            <value>/usr/local/hadoop/mr­history/done</value>
            <description>目录中的历史文件是由MR JobHistoryServer管理</description>
        </property>
    </configuration>
    ```

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
 
