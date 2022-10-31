# Hive 配置

- 说明
 
    这里面列出了hive几乎所有的配置项，下面问题只是说出了几种配置项目的作用。更多内容，可以查看内容

- 问题导读：

    1.hive输出格式的配置项是哪个？

    2.hive被各种语言调用如何配置？
    
    3.hive提交作业是在hive中还是hadoop中？
    
    4.一个查询的最后一个map/reduce任务输出是否被压缩的标志，通过哪个配置项？
    
    5.当用户自定义了UDF或者SerDe，这些插件的jar都要放到这个目录下，通过那个配置项？
    
    6.每个reducer的大小，默认是1G，输入文件如果是10G，那么就会起10个reducer；通过那个配置项可以配置？
    
    7.group by操作是否允许数据倾斜，通过那个配置项配置？
    
    8.本地模式时，map/reduce的内存使用量该如何配置？
    
    9.在做表join时缓存在内存中的行数，默认25000；通过那个配置项可以修改？
    
    10.是否开启数据倾斜的join优化，通过那个配置项可以优化？
    
    11.并行运算开启时，允许多少作业同时计算，默认是8；该如何修改这个配置项？


- hive的配置说明：

    ```
    hive.ddl.output.format：hive的ddl语句的输出格式，默认是text，纯文本，还有json格式，这个是0.90以后才出的新配置；

    hive.exec.script.wrapper：hive调用脚本时的包装器，默认是null，如果设置为python的话，那么在做脚本调用操作时语句会变为python <script command>，null的话就是直接执行<script command>；

    hive.exec.plan：hive执行计划的文件路径，默认是null，会在运行时自动设置，形如hdfs://xxxx/xxx/xx；

    hive.exec.scratchdir：hive用来存储不同阶段的map/reduce的执行计划的目录，同时也存储中间输出结果，默认是/tmp/<user.name>/hive，我们实际一般会按组区分，然后组内自建一个tmp目录存储；

    hive.exec.submitviachild：在非local模式下，决定hive是否要在独立的jvm中执行map/reduce；默认是false，也就是说默认map/reduce的作业是在hive的jvm上去提交的；

    hive.exec.script.maxerrsize：当用户调用transform或者map或者reduce执行脚本时，最大的序列化错误数，默认100000，一般也不用修改；

    hive.exec.compress.output：一个查询的最后一个map/reduce任务输出是否被压缩的标志，默认为false，但是一般会开启为true，好处的话，节省空间不说，在不考虑cpu压力的时候会提高io；

    hive.exec.compress.intermediate：类似上个，在一个查询的中间的map/reduce任务输出是否要被压缩，默认false，

    hive.jar.path：当使用独立的jvm提交作业时，hive_cli.jar所在的位置，无默认值；

    hive.aux.jars.path：当用户自定义了UDF或者SerDe，这些插件的jar都要放到这个目录下，无默认值；

    hive.partition.pruning：在编译器发现一个query语句中使用分区表然而未提供任何分区谓词做查询时，抛出一个错误从而保护分区表，默认是nonstrict；（待读源码后细化，网上资料极少）

    hive.map.aggr：map端聚合是否开启，默认开启；

    hive.join.emit.interval：在发出join结果之前对join最右操作缓存多少行的设定，默认1000；hive jira里有个对该值设置太小的bugfix；

    hive.map.aggr.hash.percentmemory：map端聚合时hash表所占用的内存比例，默认0.5，这个在map端聚合开启后使用，

    hive.default.fileformat：CREATE TABLE语句的默认文件格式，默认TextFile，其他可选的有SequenceFile、RCFile还有Orc；

    hive.merge.mapfiles：在只有map的作业结束时合并小文件，默认开启true；

    hive.merge.mapredfiles：在一个map/reduce作业结束后合并小文件，默认不开启false；

    hive.merge.size.per.task：作业结束时合并文件的大小，默认256MB；

    hive.merge.smallfiles.avgsize：在作业输出文件小于该值时，起一个额外的map/reduce作业将小文件合并为大文件，小文件的基本阈值，设置大点可以减少小文件个数，需要mapfiles和mapredfiles为true，默认值是16MB；



    mapred.reduce.tasks：每个作业的reduce任务数，默认是hadoop client的配置1个；


    hive.exec.reducers.bytes.per.reducer：每个reducer的大小，默认是1G，输入文件如果是10G，那么就会起10个reducer；


    hive.exec.reducers.max：reducer的最大个数，如果在mapred.reduce.tasks设置为负值，那么hive将取该值作为reducers的最大可能值。当然还要依赖（输入文件大小/hive.exec.reducers.bytes.per.reducer）所得出的大小，取其小值作为reducer的个数，hive默认是999；


    hive.fileformat.check：加载数据文件时是否校验文件格式，默认是true；


    hive.groupby.skewindata：group by操作是否允许数据倾斜，默认是false，当设置为true时，执行计划会生成两个map/reduce作业，第一个MR中会将map的结果随机分布到reduce中，达到负载均衡的目的来解决数据倾斜，


    hive.groupby.mapaggr.checkinterval：map端做聚合时，group by 的key所允许的数据行数，超过该值则进行分拆，默认是100000；


    hive.mapred.local.mem：本地模式时，map/reduce的内存使用量，默认是0，就是无限制；


    hive.mapjoin.followby.map.aggr.hash.percentmemory：map端聚合时hash表的内存占比，该设置约束group by在map join后进行，否则使用hive.map.aggr.hash.percentmemory来确认内存占比，默认值0.3；


    hive.map.aggr.hash.force.flush.memeory.threshold：map端聚合时hash表的最大可用内存，如果超过该值则进行flush数据，默认是0.9；


    hive.map.aggr.hash.min.reduction：如果hash表的容量与输入行数之比超过这个数，那么map端的hash聚合将被关闭，默认是0.5，设置为1可以保证hash聚合永不被关闭；


    hive.optimize.groupby：在做分区和表查询时是否做分桶group by，默认开启true；


    hive.multigroupby.singlemr：将多个group by产出为一个单一map/reduce任务计划，当然约束前提是group by有相同的key，默认是false；


    hive.optimize.cp：列裁剪，默认开启true，在做查询时只读取用到的列，这个是个有用的优化；


    hive.optimize.index.filter：自动使用索引，默认不开启false；


    hive.optimize.index.groupby：是否使用聚集索引优化group-by查询，默认关闭false；


    hive.optimize.ppd：是否支持谓词下推，默认开启；所谓谓词下推，将外层查询块的 WHERE 子句中的谓词移入所包含的较低层查询块（例如视图），从而能够提早进行数据过滤以及有可能更好地利用索引。


    hive.optimize.ppd.storage：谓词下推开启时，谓词是否下推到存储handler，默认开启，在谓词下推关闭时不起作用；


    hive.ppd.recognizetransivity：在等值join条件下是否产地重复的谓词过滤器，默认开启；


    hive.join.cache.size：在做表join时缓存在内存中的行数，默认25000；


    hive.mapjoin.bucket.cache.size：mapjoin时内存cache的每个key要存储多少个value，默认100；


    hive.optimize.skewjoin：是否开启数据倾斜的join优化，默认不开启false；


    hive.skewjoin.key：判断数据倾斜的阈值，如果在join中发现同样的key超过该值则认为是该key是倾斜的join key，默认是100000；


    hive.skewjoin.mapjoin.map.tasks：在数据倾斜join时map join的map数控制，默认是10000；


    hive.skewjoin.mapjoin.min.split：数据倾斜join时map join的map任务的最小split大小，默认是33554432，该参数要结合上面的参数共同使用来进行细粒度的控制；


    hive.mapred.mode：hive操作执行时的模式，默认是nonstrict非严格模式，如果是strict模式，很多有风险的查询会被禁止运行，比如笛卡尔积的join和动态分区；



    hive.exec.script.maxerrsize：一个map/reduce任务允许打印到标准错误里的最大字节数，为了防止脚本把分区日志填满，默认是100000；


    hive.exec.script.allow.partial.consumption：hive是否允许脚本不从标准输入中读取任何内容就成功退出，默认关闭false；


    hive.script.operator.id.env.var：在用户使用transform函数做自定义map/reduce时，存储唯一的脚本标识的环境变量的名字，默认HIVE_SCRIPT_OPERATOR_ID；


    hive.exec.compress.output：控制hive的查询结果输出是否进行压缩，压缩方式在hadoop的mapred.output.compress中配置，默认不压缩false；


    hive.exec.compress.intermediate：控制hive的查询中间结果是否进行压缩，同上条配置，默认不压缩false；


    hive.exec.parallel：hive的执行job是否并行执行，默认不开启false，在很多操作如join时，子查询之间并无关联可独立运行，这种情况下开启并行运算可以大大加速；


    hvie.exec.parallel.thread.number：并行运算开启时，允许多少作业同时计算，默认是8；


    hive.exec.rowoffset：是否提供行偏移量的虚拟列，默认是false不提供，Hive有两个虚拟列:一个是INPUT__FILE__NAME,表示输入文件的路径，另外一个是BLOCK__OFFSET__INSIDE__FILE，表示记录在文件中的块偏移量，这对排查出现不符合预期或者null结果的查询是很有帮助的；


    hive.task.progress：控制hive是否在执行过程中周期性的更新任务进度计数器，开启这个配置可以帮助job tracker更好的监控任务的执行情况，但是会带来一定的性能损耗，当动态分区标志hive.exec.dynamic.partition开启时，本配置自动开启；


    hive.exec.pre.hooks：执行前置条件，一个用逗号分隔开的实现了org.apache.hadoop.hive.ql.hooks.ExecuteWithHookContext接口的java class列表，配置了该配置后，每个hive任务执行前都要执行这个执行前钩子，默认是空；


    hive.exec.post.hooks：同上，执行后钩子，默认是空；


    hive.exec.failure.hooks：同上，异常时钩子，在程序发生异常时执行，默认是空；


    hive.mergejob.maponly：试图生成一个只有map的任务去做merge，前提是支持CombineHiveInputFormat，默认开启true；


    hive.mapjoin.smalltable.filesize：输入表文件的mapjoin阈值，如果输入文件的大小小于该值，则试图将普通join转化为mapjoin，默认25MB；


    hive.mapjoin.localtask.max.memory.usage：mapjoin本地任务执行时hash表容纳key/value的最大量，超过这个值的话本地任务会自动退出，默认是0.9；


    hive.mapjoin.followby.gby.localtask.max.memory.usage：类似上面，只不过是如果mapjoin后有一个group by的话，该配置控制类似这样的query的本地内存容量上限，默认是0.55；


    hive.mapjoin.check.memory.rows：在运算了多少行后执行内存使用量检查，默认100000；


    hive.heartbeat.interval：发送心跳的时间间隔，在mapjoin和filter操作中使用，默认1000；


    hive.auto.convert.join：根据输入文件的大小决定是否将普通join转换为mapjoin的一种优化，默认不开启false；


    hive.script.auto.progress：hive的transform/map/reduce脚本执行时是否自动的将进度信息发送给TaskTracker来避免任务没有响应被误杀，本来是当脚本输出到标准错误时，发送进度信息，但是开启该项后，输出到标准错误也不会导致信息发送，因此有可能会造成脚本有死循环产生，但是TaskTracker却没有检查到从而一直循环下去；


    hive.script.serde：用户脚本转换输入到输出时的SerDe约束，默认是org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe；


    hive.script.recordreader：从脚本读数据的时候的默认reader，默认是org.apache.hadoop.hive.ql.exec.TextRecordReader；


    hive.script.recordwriter：写数据到脚本时的默认writer，默认org.apache.hadoop.hive.ql.exec.TextRecordWriter；


    hive.input.format：输入格式，默认是org.apache.hadoop.hive.ql.io.CombineHiveInputFormat，如果出现问题，可以改用org.apache.hadoop.hive.ql.io.HiveInputFormat；


    hive.udtf.auto.progress：UDTF执行时hive是否发送进度信息到TaskTracker，默认是false；


    hive.mapred.reduce.tasks.speculative.execution：reduce任务推测执行是否开启，默认是true；


    hive.exec.counters.pull.interval：运行中job轮询JobTracker的时间间隔，设置小会影响JobTracker的load，设置大可能看不出运行任务的信息，要去平衡，默认是1000；


    hive.enforce.bucketing：数据分桶是否被强制执行，默认false，如果开启，则写入table数据时会启动分桶，


    hive.enforce.sorting：开启强制排序时，插数据到表中会进行强制排序，默认false；


    hive.optimize.reducededuplication：如果数据已经根据相同的key做好聚合，那么去除掉多余的map/reduce作业，此配置是文档的推荐配置，建议打开，默认是true；


    hive.exec.dynamic.partition：在DML/DDL中是否支持动态分区，默认false；


    hive.exec.dynamic.partition.mode：默认strict，在strict模式下，动态分区的使用必须在一个静态分区确认的情况下，其他分区可以是动态；


    hive.exec.max.dynamic.partitions：动态分区的上限，默认1000；


    hive.exec.max.dynamic.partitions.pernode：每个mapper/reducer节点可以创建的最大动态分区数，默认100；


    hive.exec.max.created.files：一个mapreduce作业能创建的HDFS文件最大数，默认是100000；


    hive.exec.default.partition.name：当动态分区启用时，如果数据列里包含null或者空字符串的话，数据会被插入到这个分区，默认名字是__HIVE_DEFAULT_PARTITION__；


    hive.fetch.output.serde：FetchTask序列化fetch输出时需要的SerDe，默认是org.apache.hadoop.hive.serde2.DelimitedJSONSerDe;


    hive.exec.mode.local.auto：是否由hive决定自动在local模式下运行，默认是false，

    hive.exec.drop.ignorenoneexistent：在drop表或者视图时如果发现表或视图不存在，是否报错，默认是true；


    hive.exec.show.job.failure.debug.info：在作业失败时是否提供一个任务debug信息，默认true；


    hive.auto.progress.timeout：运行自动progressor的时间间隔，默认是0等价于forever；


    hive.table.parameters.default：新建表的属性字段默认值，默认是empty空；


    hive.variable.substitute：是否支持变量替换，如果开启的话，支持语法如${var} ${system:var}和${env.var}，默认是true；


    hive.error.on.empty.partition：在遇到结果为空的动态分区时是否报错，默认是false；


    hive.exim.uri.scheme.whitelist：在导入导出数据时提供的一个白名单列表，列表项之间由逗号分隔，默认hdfs,pfile；


    hive.limit.row.max.size：字面意思理解就是在使用limit做数据的子集查询时保证的最小行数据量，默认是100000；


    hive.limit.optimize.limit.file：使用简单limit查询数据子集时，可抽样的最大文件数，默认是10；


    hive.limit.optimize.enable：使用简单limit抽样数据时是否开启优化选项，默认是false，关于limit的优化问题，在hive programming书中解释的是这个feature有drawback，对于抽样的不确定性给出了风险提示；


    hive.limit.optimize.fetch.max：使用简单limit抽样数据允许的最大行数，默认50000，查询query受限，insert不受影响；


    hive.rework.mapredwork：是否重做mapreduce，默认是false；


    hive.sample.seednumber：用来区分抽样的数字，默认是0；


    hive.io.exception.handlers：io异常处理handler类列表，默认是空，当record reader发生io异常时，由这些handler来处理异常；


    hive.autogen.columnalias.prefix.label：当在执行中自动产生列别名的前缀，当类似count这样的聚合函数起作用时，如果不明确指出count(a) as xxx的话，那么默认会从列的位置的数字开始算起添加，比如第一个count的结果会冠以列名_c0，接下来依次类推，默认值是_c，数据开发过程中应该很多人都看到过这个别名；


    hive.autogen.columnalias.prefix.includefuncname：在自动生成列别名时是否带函数的名字，默认是false；


    hive.exec.perf.logger：负责记录客户端性能指标的日志类名，必须是org.apache.hadoop.hive.ql.log.PerfLogger的子类，默认是org.apache.hadoop.hive.ql.log.PerfLogger；


    hive.start.cleanup.scratchdir：当启动hive服务时是否清空hive的scratch目录，默认是false；


    hive.output.file.extension：输出文件扩展名，默认是空；


    hive.insert.into.multilevel.dirs：是否插入到多级目录，默认是false；


    hive.files.umask.value：hive创建文件夹时的dfs.umask值，默认是0002；

    hive.metastore.local：控制hive是否连接一个远程metastore服务器还是开启一个本地客户端jvm，默认是true，Hive0.10已经取消了该配置项；


    javax.jdo.option.ConnectionURL：JDBC连接字符串，默认jdbc:derby:;databaseName=metastore_db;create=true；


    javax.jdo.option.ConnectionDriverName：JDBC的driver，默认org.apache.derby.jdbc.EmbeddedDriver；


    javax.jdo.PersisteneManagerFactoryClass：实现JDO PersistenceManagerFactory的类名，默认org.datanucleus.jdo.JDOPersistenceManagerFactory；


    javax.jdo.option.DetachAllOnCommit：事务提交后detach所有提交的对象，默认是true；


    javax.jdo.option.NonTransactionalRead：是否允许非事务的读，默认是true；


    javax.jdo.option.ConnectionUserName：username，默认APP；


    javax.jdo.option.ConnectionPassword：password，默认mine；


    javax.jdo.option.Multithreaded：是否支持并发访问metastore，默认是true；


    datanucleus.connectionPoolingType：使用连接池来访问JDBC metastore，默认是DBCP；


    datanucleus.validateTables：检查是否存在表的schema，默认是false；


    datanucleus.validateColumns：检查是否存在列的schema，默认false；


    datanucleus.validateConstraints：检查是否存在constraint的schema，默认false；


    datanucleus.stroeManagerType：元数据存储类型，默认rdbms；


    datanucleus.autoCreateSchema：在不存在时是否自动创建必要的schema，默认是true；


    datanucleus.aotuStartMechanismMode：如果元数据表不正确，抛出异常，默认是checked；


    datanucleus.transactionIsolation：默认的事务隔离级别，默认是read-committed；


    datanucleus.cache.level2：使用二级缓存，默认是false；


    datanucleus.cache.level2.type：二级缓存的类型，有两种，SOFT:软引用，WEAK:弱引用，默认是SOFT；


    datanucleus.identifierFactory：id工厂生产表和列名的名字，默认是datanucleus；


    datanucleus.plugin.pluginRegistryBundleCheck：当plugin被发现并且重复时的行为，默认是LOG；


    hive.metastroe.warehouse.dir：数据仓库的位置，默认是/user/hive/warehouse；


    hive.metastore.execute.setugi：非安全模式，设置为true会令metastore以客户端的用户和组权限执行DFS操作，默认是false，这个属性需要服务端和客户端同时设置；


    hive.metastore.event.listeners：metastore的事件监听器列表，逗号隔开，默认是空；


    hive.metastore.partition.inherit.table.properties：当新建分区时自动继承的key列表，默认是空；


    hive.metastore.end.function.listeners：metastore函数执行结束时的监听器列表，默认是空；


    hive.metastore.event.expiry.duration：事件表中事件的过期时间，默认是0；


    hive.metastore.event.clean.freq：metastore中清理过期事件的定时器的运行周期，默认是0；


    hive.metastore.connect.retries：创建metastore连接时的重试次数，默认是5；


    hive.metastore.client.connect.retry.delay：客户端在连续的重试连接等待的时间，默认1；


    hive.metastore.client.socket.timeout：客户端socket超时时间，默认20秒；


    hive.metastore.rawstore.impl：原始metastore的存储实现类，默认是org.apache.hadoop.hive.metastore.ObjectStore；


    hive.metastore.batch.retrieve.max：在一个batch获取中，能从metastore里取出的最大记录数，默认是300；


    hive.metastore.ds.connection.url.hook：查找JDO连接url时hook的名字，默认是javax.jdo.option.ConnectionURL；


    hive.metastore.ds.retry.attempts：当出现连接错误时重试连接的次数，默认是1次；


    hive.metastore.ds.retry.interval：metastore重试连接的间隔时间，默认1000毫秒；


    hive.metastore.server.min.threads：在thrift服务池中最小的工作线程数，默认是200；


    hive.metastore.server.max.threads：最大线程数，默认是100000；


    hive.metastore.server.tcp.keepalive：metastore的server是否开启长连接，长连可以预防半连接的积累，默认是true；


    hive.metastore.sasl.enabled：metastore thrift接口的安全策略，开启则用SASL加密接口，客户端必须要用Kerberos机制鉴权，默认是不开启false；


    hive.metastore.kerberos.keytab.file：在开启sasl后kerberos的keytab文件存放路径，默认是空；


    hive.metastore.kerberos.principal：kerberos的principal，_HOST部分会动态替换，默认是hive-metastore/_HOST@EXAMPLE.COM；


    hive.metastore.cache.pinobjtypes：在cache中支持的metastore的对象类型，由逗号分隔，默认是Table,StorageDescriptor,SerDeInfo,Partition,Database,Type,FieldSchema,Order；


    hive.metastore.authorization.storage.checks：在做类似drop partition操作时，metastore是否要认证权限，默认是false；


    hive.metastore.schema.verification：强制metastore的schema一致性，开启的话会校验在metastore中存储的信息的版本和hive的jar包中的版本一致性，并且关闭自动schema迁移，用户必须手动的升级hive并且迁移schema，关闭的话只会在版本不一致时给出警告，默认是false不开启；



    hive.index.compact.file.ignore.hdfs：在索引文件中存储的hdfs地址将在运行时被忽略，如果开启的话；如果数据被迁移，那么索引文件依然可用，默认是false；


    hive.optimize.index.filter.compact.minsize：压缩索引自动应用的最小输入大小，默认是5368709120；


    hive.optimize.index.filter.compact.maxsize：同上，相反含义，如果是负值代表正无穷，默认是-1；


    hive.index.compact.query.max.size：一个使用压缩索引做的查询能取到的最大数据量，默认是10737418240 个byte；负值代表无穷大；


    hive.index.compact.query.max.entries：使用压缩索引查询时能读到的最大索引项数，默认是10000000；负值代表无穷大；


    hive.index.compact.binary.search：在索引表中是否开启二分搜索进行索引项查询，默认是true；


    hive.exec.concatenate.check.index：如果设置为true，那么在做ALTER TABLE tbl_name CONCATENATE on a table/partition（有索引） 操作时，抛出错误；可以帮助用户避免index的删除和重建；


    hive.stats.dbclass：存储hive临时统计信息的数据库，默认是jdbc:derby；


    hive.stats.autogather：在insert overwrite命令时自动收集统计信息，默认开启true；


    hive.stats.jdbcdriver：数据库临时存储hive统计信息的jdbc驱动；


    hive.stats.dbconnectionstring：临时统计信息数据库连接串，默认jdbc:derby:databaseName=TempStatsStore;create=true；


    hive.stats.defaults.publisher：如果dbclass不是jdbc或者hbase，那么使用这个作为默认发布，必须实现StatsPublisher接口，默认是空；


    hive.stats.defaults.aggregator：如果dbclass不是jdbc或者hbase，那么使用该类做聚集，要求实现StatsAggregator接口，默认是空；


    hive.stats.jdbc.timeout：jdbc连接超时配置，默认30秒；


    hive.stats.retries.max：当统计发布合聚集在更新数据库时出现异常时最大的重试次数，默认是0，不重试；


    hive.stats.retries.wait：重试次数之间的等待窗口，默认是3000毫秒；


    hive.client.stats.publishers：做count的job的统计发布类列表，由逗号隔开，默认是空；必须实现org.apache.hadoop.hive.ql.stats.ClientStatsPublisher接口；


    hive.client.stats.counters：没什么用~~~


    hive.security.authorization.enabled：hive客户端是否认证，默认是false；


    hive.security.authorization.manager：hive客户端认证的管理类，默认是org.apache.hadoop.hive.ql.security.authorization.DefaultHiveAuthorizationProvider；用户定义的要实现org.apache.hadoop.hive.ql.security.authorization.HiveAuthorizationProvider；


    hive.security.authenticator.manager：hive客户端授权的管理类，默认是org.apache.hadoop.hive.ql.security.HadoopDefaultAuthenticator；用户定义的需要实现org.apache.hadoop.hive.ql.security.HiveAuthenticatorProvider；


    hive.security.authorization.createtable.user.grants：当表创建时自动授权给用户，默认是空；


    hive.security.authorization.createtable.group.grants：同上，自动授权给组，默认是空；


    hive.security.authorization.createtable.role.grants：同上，自动授权给角色，默认是空；


    hive.security.authorization.createtable.owner.grants：同上，自动授权给owner，默认是空；


    hive.security.metastore.authorization.manager：metastore的认证管理类，默认是org.apache.hadoop.hive.ql.security.authorization.DefaultHiveMetastoreAuthorizationProvider；用户定义的必须实现org.apache.hadoop.hive.ql.security.authorization.HiveMetastoreAuthorizationProvider接口；接口参数要包含org.apache.hadoop.hive.ql.security.authorization.StorageBasedAuthorizationProvider接口；使用HDFS的权限控制认证而不是hive的基于grant的方式；


    hive.security.metastore.authenticator.manager：metastore端的授权管理类，默认是org.apache.hadoop.hive.ql.security.HadoopDefaultMetastoreAuthenticator，自定义的必须实现org.apache.hadoop.hive.ql.security.HiveAuthenticatorProvider接口；


    hive.metastore.pre.event.listeners：在metastore做数据库任何操作前执行的事件监听类列表；



    fs.har.impl：访问Hadoop Archives的实现类，低于hadoop 0.20版本的都不兼容，默认是org.apache.hadoop.hive.shims.HiveHarFileSystem；


    hive.archive.enabled：是否允许归档操作，默认是false；


    hive.archive.har.parentdir.settable：在创建HAR文件时必须要有父目录，需要手动设置，在新的hadoop版本会支持，默认是false；


    hive.support.concurrency：hive是否支持并发，默认是false，支持读写锁的话，必须要起zookeeper；


    hive.lock.mapred.only.operation：控制是否在查询时加锁，默认是false；


    hive.lock.numretries：获取锁时尝试的重试次数，默认是100；


    hive.lock.sleep.between.retries：在重试间隔的睡眠时间，默认60秒；


    hive.zookeeper.quorum：zk地址列表，默认是空；


    hive.zookeeper.client.port：zk服务器的连接端口，默认是2181；


    hive.zookeeper.session.timeout：zk客户端的session超时时间，默认是600000；


    hive.zookeeper.namespace：在所有zk节点创建后的父节点，默认是hive_zookeeper_namespace；


    hive.zookeeper.clean.extra.nodes：在session结束时清除所有额外node；


    hive.cluster.delegation.token.store.class：代理token的存储实现类，默认是org.apache.hadoop.hive.thrift.MemoryTokenStore，可以设置为org.apache.hadoop.hive.thrift.ZooKeeperTokenStore来做负载均衡集群；


    hive.cluster.delegation.token.store.zookeeper.connectString：zk的token存储连接串，默认是localhost:2181；


    hive.cluster.delegation.token.store.zookeeper.znode：token存储的节点跟路径，默认是/hive/cluster/delegation；


    hive.cluster.delegation.token.store.zookeeper.acl：token存储的ACL，默认是sasl:hive/host1@example.com:cdrwa,sasl:hive/host2@example.com:cdrwa；


    hive.use.input.primary.region：从一张input表创建表时，创建这个表到input表的主region，默认是true；


    hive.default.region.name：默认region的名字，默认是default；


    hive.region.properties：region的默认的文件系统和jobtracker，默认是空；


    hive.cli.print.header：查询输出时是否打印名字和列，默认是false；


    hive.cli.print.current.db：hive的提示里是否包含当前的db，默认是false；


    hive.hbase.wal.enabled：写入hbase时是否强制写wal日志，默认是true；


    hive.hwi.war.file：hive在web接口是的war文件的路径，默认是lib/hive-hwi-xxxx(version).war；


    hive.hwi.listen.host：hwi监听的host地址，默认是0.0.0.0；


    hive.hwi.listen.port：hwi监听的端口，默认是9999；


    hive.test.mode：hive是否运行在测试模式，默认是false；


    hive.test.mode.prefix：在测试模式运行时，表的前缀字符串，默认是test_；


    hive.test.mode.samplefreq：如果hive在测试模式运行，并且表未分桶，抽样频率是多少，默认是32；


    hive.test.mode.nosamplelist：在测试模式运行时不进行抽样的表列表，默认是空；
    ```