### hive中使用的SQL笔记整理

1、创建一个表，字段之间用 \t 分隔；

    Hive>create  table  student (id  int,  name  string) row  format  delimited  fields  terminated  by '\t' ;



2、将本地一个数据提交到hive里去

    hive>load data local inpath '/home/student.txt' into  table  student ;

      2.1 增加分区表数据

      alter table ZHIYOUBAO.CHECK_RECORD add  partition (years='xxxx',months='xx',days='xx') location                         '/ZYB/CHECK_RECORD/yy=xxxx/mm=xx/dd=xx/';

3、查询表里的数据：

        hive>select  *  from  student ;



4、只查询前两条：

        hive>select  * from  student  limit  2 ;



5、统计一个表的行数：

        hive>select  count(*)  from student ;



6、求一个表id字段的id 之和：

        hive>select  sum(id)  from  student ;



7、创建外部表：

        hive>create  external  table  ext_student  (id int, name string) row format delimited  fields  terminated  by  ' \t  '  location  ' /data ' ;     //这样就不必将文件放到hive里去 就可以对其进行操作了   ，只需要将文件放到hdfs上的/data目录下面。



8、内部表先有表后有数据；外部表先有数据后有表。



9、创建分区表：

        hive>create external table beauties  (id bigint, name string,  size  double)  partitioned by (nation  string)  row  format  delimited fields  terminated  by  '\t'  location  '\beauty' ;
        hive>load  data  local  inpath  '/home/b.c'  into  table  beauties  partition(nation='China') ;
        hive>alter  table  beauties  add  partition  (nation='Japan') ;
        hive>select  *  from  beauties ;
        hive>select  *  from  beauties  where  nation='China' ;           //查找某一分区的数据内容；



10、多表关联：

    hive>select  t . account ,  u . name , t . income , t . expenses , t . surplus from  user_info  u  join  (select  account ,  sum(income)  as  income ,  sum(expenses) as  expenses ,  sum(income-expenses)  as  surplus  from 
    trade_detail  group  by  account)  t  on  u . account  =  t . account ;



11、存储过程没有返回值，函数有返回值



12、在linux环境下一次访问hive：
       
        [hh@master ~]$ hive  -e  "selcte  *  from  mytable   limit  3" ;



13、[hh@master ~]$ hive -f 1.hql



14、打印表的字段信息：
            
          hive>describe  yourtable ;



15、创建数据库：

        
        hive>create  database  financials ;
        hive>create  database  if  not  exists  financials ;



16、过滤数据库：
        
        hive>show  databases  like  " f . * " ;



17、添加描述信息：
        
        hive> create database test092302 with dbproperties ('creator'='Mark', 'date'='2015-09-23');
        hive> describe database extended test092302;



18、删除数据库：
        
        hive> drop database if exists human_resources;   或者
        hive> drop database human_resources;



19、删除存在表的数据库：
        
        hive> drop database test0923 cascade;      //在后面加上cascade关键字



20、创建数据库时添加描述信息：
        
        hive> create database test092302 comment 'Holds all test tables';     //使用comment，创建表时也可以用



21、去重查询：group   by的使用
        
        hive>select  *  from  mytable  group  by  uid ;



22、独立UID总数：
        
        hive>select  count(distinct(uid)) from  mytable ; （高效） 或者   hive>select  count(*) from(select  *  from mytable  group  by  uid)  a ;



23、查询频度排名（频度最高的前50）：
        
        hive> select keyword,count(*) as cnt from sogou_1w group by keyword order by cnt desc limit 50;



24、将查询的结果放入另一个表中：
        
        hive> create table uid_cnt (uid string, cnt int) row format delimited fields terminated by '\t';       //先创建临时表 uid_cnt
        hive> insert overwrite table sogou.uid_cnt select uid,count(*) from sogou_1w group by uid;     //再将查询的数据结果放入临时表中

25 修改列名：

  hive> alter table test
    > column ·stuname·  name string;“ · ”右上角的~键
  describe test;

26 增加列：

    hive> alter table test add columns(
    > height int);

    hive>describe test;

27替换列：
  
    hive> alter table test replace columns(
    > id int,
    > name string,
    > age int);

28 为表添加属性：

    hive> alter table test set tblproperties (
    > 'note'='hello welcome');

    show create table test;
========================================

29 创建带有分区的内部表：
    
    hive> create table testpar(
    > id int,
    > name string,age int) PARTITIONED BY (day string)
    > ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' 
    > location '/testpar';

30 为带有分区的内部表加载数据：

    hive> load data local inpath '/home/test' into table testpar 
    > partition (day='0925');

31 添加防止删除的保护：
hive> alter table testpar
    > partition (day='0925') enable no_drop;

32 测试：删除分区

    hive> alter table testpar drop if exists partition (day='0925');

33 删除添加的"删除"保护：

    hive> alter table testpar
    > partition (day='0925') disable no_drop;

34 添加防止查询的保护：


    hive> alter table testpar
    > partition (day='0925') enable offline;

35 删除防止查询的保护:

    hive> alter table testpar
    > partition (day='0925') disable offline;

    select * from testpar;
================================================


36 按条件向分区表插入数据
    hive>from test_1  ts  
    insert into table  testpart partition (day='0920') select * where ts.age>20   
    insert into table testpart partition (day='0919') select * where ts.name='xiaofang'; 

    注释:

    上面SQL语句分三部分
    第一部分 
    from test_1  ts  从rest_1表中查询并为其添加ts别名
    第二部分 
    insert into table  testpart partition (day='0920') select * where ts.age>20
    将test_1表中年龄大于20的数据添加到分区表testpart中新建的0920分区中.
    第三部分   
    insert into table testpart partition (day='0919') select * where ts.name='xiaofang'
    将test_1表中名字为xiaofang的数据添加到分区表testpart中新建的0919分区中

查询结果:

    hive>  select  * from  testpart;


37 向管理表中加载数据：
    
    hive> load data local inpath '/home/test' overwrite  into table testpar partition (day='0925');

38 通过查询语句向表中插入数据：

    hive> insert into table testpar
        > partition (day='0926')
        > select * from test;

    hive> select * from testpar;

    hive> insert into table testpar
        > partition (day='0922')
        > select * from test
        > where age >20;

    hive> from test
        > insert into table testpar
        > partition (day='0921')
        > select * where age>22;

    hive> from test ts
        > insert into table testpar
        > partition (day='0920')
        > select * where ts.age>20
        > insert into table testpar
        > partition (day='0919')
        > select * where ts.name='张三';


=========================

动态分区插入


=========================


39 在test表中添加一列day

    hive> alter table test add columns(day string);

    [hh@master ~]$ vi test
    [hh@master ~]$ cat test
    1    张三    20    0921
    2    李四    22    0922
    3    Jarrey    25    0923
40 加载数据：

    hive> load data local inpath '/home/test' overwrite into table test;
    动态分区（下面两种方式实现的效果是一样的）：
    hive>  set hive.exec.dynamic.partition=true;
    hive>  set hive.exec.dynamic.partition.mode=nonstrict;
    hive>  set hive.exec.max.dynamic.partitions.pernode=1000;

    hive> insert into table testpar
        > partition(day)
        > select * from test;

    hive> insert into table testpar
        > partition(day)
        > select id,name,age,day from test;

41单个查询语句中创建表并加载数据:(注意关键字as)

    hive> create table newtest
        > as select id,name,age from test
        > where name='李四';

    hive> select * from newtest;


=========================

导出数据


=========================

42 Hadoop fs –cp source_path target_path
    cp
    scp -r /jdk  slave://home/

    注释:

    scp =safety copy 即是安全模式下复制   r=recuresive 递归方式复制  即是从主目录到各个子目录依次复制

=========================

Sqoop工具（T15）


=========================


43  从hdfs集群中加载数据

    hive>load  data  inpath 'hdfs目录文件'  into  table  student;

44 按id降序排序


    hive>select * from  student  order by id desc;



45   从hdfs集群中加载数据并为表设置指定分区

    hive>load  data  input  '本地文件路径' into  table  表名  partition (分区字段=' ');


46 从本地内存中加载数据

    hive>load data local inpath '本地目录文件' into  table  student;



47 按id降序排序

    hive>select * from  student  order by id desc;

48 表联合查询

    hive>select t.account u.name,t.income,t.expenses,t.surplus from user_info
    u join (select account, sum(income) as income,sum(expenses) as expenses,sm(income_expenses)
    as surplus from trade_detail group by account) on u.account=t.account;

=========================

数学函数

=========================


Hive语句运算:

49 int类型rank加运算

    hive>select rank+1 from  ext_sogou_20111230 limit 100;

50 对int字段平方
    
    hive> select pow(rank,2) from  ext_sogou_20111230;

51  取模:(如:2对三取模)
    
    hive>select pmod(2,3) from ext_sogou_20111230 limit 10;

=========================

聚合函数

=========================


52
    
    hive>select count(*) from  ext_sogou_20111230 limit 10;
    *表示表中所有字段也可以设置某些或某个字段 如

    hive>select count(uid,ts) from  ext_sogou_20111230 limit 10;

53. 

    hive>select  sum(uid) from ext_sogou_20111230;

54 最大值&最小值

    hive>select max(rank), min(rank) from ext_sogou_20111230;

55 .独立uid(去重行数)

    hive>select count(distinct uid) from ext_sogou_20111230;


56强转:
    
    hive> select cast(rank as DOUBLE) from ext_sogou_20111230 limit 10;

57  拼接:
    
    hive>select concat(uid,url) from ext_sogou_20111230 limit 10;



=========================

JSON


=========================

58  抽取JSON对象的某一属性值
    hive>select get_json_object('{"name":"xiaoming","age":"15"}','$.age') from ext_sogou_20111230 limit 5;
    结果:
    15

    59

    hive>select  get_json_object(channel,'$.age') from ext_sogou_20111230 limit 3;

=============================================

60 查找url字符串中的5位置之后字符串baidu第一次出现的位置

    hive> select locate("baidu",url,5) from ext_sogou_20111230 limit 100;

61 .抽取字符串baidu中符合正则表达式url的第5个部分的子字符串

    hive> select regexp_extract("baidu",url,5) from ext_sogou_20111230 limit 100; 

62  按照正则表达式"0"分割字符串uid,并将分割后的部分以字符串数组的方式返回

    hive> select split(uid,"0") from ext_sogou_20111230 limit 100;
    结果之一:["","875edc8a14a228","1bac1ddc","1fa18a1"]

63  对字符串url,从0处开截取长度为3的字符串,作为其子字符串

    hive> select substr(url,0,3) from ext_sogou_20111230 limit 3; 

64 .将字符串url中所有的字母转换成大写字母
、
    hive> select upper(url) from ext_sogou_20111230 limit 3;


=====================

别名 嵌套SQL语句

=====================

65  复杂HQL 如别名、嵌套等
   
    hive>select count(distinct e.uid) from (select * from ext_sogou_20111230 where
    rank <=3 and order =1) e;
    小括号中返回的也是一个表,它只是临时的 别名为e 

66  where  ..and  或者 where ....or   where的 两种条件查询 
    
    hive> select * from  ext_sogou_20111230  where rank<=3 and order =1 limit 3;
    hive> select * from  ext_sogou_20111230 where rank !=0 or order =1 limit 3;

where 
1 出现在表后  
2 可以有and  or  表达式的操作符
3 表示格式

67  浮点类型的比较 一定要强转

68  like 过滤字符串 

      它是一个标准的SQL操作符
    hive> select *  from  ext_sogou_20111230  where url like '%http%' limit 10;
    '%http%'意为包含 http字符串
    '%http' 以http开头的字符串
    'http%'一http结束字符串

69  rlike 通过Java的正则表达式过滤  *与%功能一样 

      它是hive中扩展功能的操作符
    hive> select * from ext_sogou_20111230 where url rlike  ' .*http.* ' limit 3; 


=======================

group by

=======================

70 Group by 语句通常会和聚合函数一起使用,按照一个或者多个对结果进行分组,然后对每个组执行聚合操作

    hive>select year(ts), avg(rank) from ext_sogou_20111230 where ts like '%2011' group by year(ts);

71 对组过滤

    hive> select rank ,count(*) from ext_sogou_20111230  group by rank ,order having rank >3  limit 10;


==========================

join

==========================

72 join 使用join时要选择具有独立的字段作为条件字段,否则会出现不必要的数据量

    hive> select m.uid,m.keyword from ext_sogou_20111230 m join ext_sogou_20111230_limit3 n on m.uid =n.uid;


73 查搜索过"仙剑奇侠传" 的用户所搜过的关键字

    hive>select  m.uid,m.keyword  from (select  distinct n.uid from
    ext_sogou_20111230 where keyword like '%仙剑奇侠传%' n ) m  
    where m.uid=n.uid;


74 查搜索过"仙剑奇侠传" 的用户所搜过的不包含"仙剑奇侠传"本身的关键字

    hive>select m.uid,m.keyword from sogou_20111230 m join (select distinct uid from sogou_20111230 where keyword like '%仙剑奇侠传%') n on m.uid=n.uid where m.keyword not like '%仙剑奇侠传%';


75  left semi-join 左半表 semi 半挂的 半独立的

    hive>select * from be where rank in(1,2,5);
    hive>select  * from  ext_sogou_20111230 m left semi join  ext_sogou_20111230_limit3  n on m.rank=n.rank;

 76笛卡尔积
 
    如5w  1w  join  结果:5w*1w   一般不常用

77 map-side JOIN当两张表很小时使用(系统默认25MB)
    
    功能:其中一张表为小表  即是将小表数据JOIN到大表中
    hive>select /*+MAPJOIN(n)*/ m.uid,m.keyword,n.keyword 
    from ext_sogou_20111230 m join ext_sogou_20111230_limint3 n on m.uid=n.uid;



=====================

排序

=====================

78 全局排序(order by ) 和局部排序 (sort by)

    hive>select * from ext_sogou_20111230 order by rank desc limit 100;

79 对sogou500w中降序排列uid次数 

    hive>select uid, count(*)  as nct from ext_sogou_20111230   group by uid order by nct desc ;

80 cast()类型转换函数 

    hive>select  cast(ts as bigint) from 
    ext_sogou_20111230_limit3;
 
81 UNION ALL可以将2个或多个表进行合并。

    hive> select count(distinct e.uid)from(
    select * from ext_sogou_20111230 where rank<11 
    union all 
    select * from ext_sogou_20111230_limit3 where rank < 11) e;

82

    hive>select count(*) from ext_sogou_20111230_limit where keyword like '%www%';
  
83

    hive> select e.url,e.keyword,count(*) from (
    select * from ext_sogou_20111230 where keyword like '%www%'
    )e  group by  e.url,e.keyword where instr(url,keyword) >0;

84搜索过'%仙剑奇侠传%'(模糊匹配),并且查询次数大于3的UID

    hive>select uid, count(uid) as nct from 
    ext_sogou_20111230  where keyword like '%仙剑奇侠传%'
    group by uid having nct>3 ;

================================
        
          视图
          
================================

85视图 hive只支持逻辑视图 作用降低查询复杂度
  
      创建视图
    hive>create view sogou_view  as 
    select * from ext_sogou_20111230 where rank <=3;

86 索引 
   
      Hive的索引需要单独创建表实现
      创建索引
    hive>CREATE INDEX employees_index ON TABLE employees (name) AS 
    'org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler'
    WITH DEFERRED REBUILD IDXPROPERTIES('creator' = 'me','
    created_at '='some  time') IN TABLE employees_index_table;


87 视图

    hive>create view sogou_filter as select uid,count(*) from 
    ext_sogou_20111230 where keyword like '%仙剑奇侠传%'

    复杂问题解题思路:
    1)分步骤,使用临时表
    2)分步骤,多个视图实现
    create view
    3)一个复杂的SQL
    create table insert overwrite table...select * from ...



=======================================

Sogou 500w数据
88

    搜索长度大于256（不区分中英文），并且点击次数<3的UID
    老师:
    hive>select m.uid,count(*) as cnt from(select * from sogou_view  where  length(
    keyword) >256) m group by m.uid having cnt<3;
    自己:
    select uid from sogou_view  where rank<3 and length(
    keyword) >256;
    hive> create view sogou_view as select * from
        ext_sogou_20111230;

89

    上午7-9点之间，搜索过“赶集网”的用户，哪些用户直接点击了赶集网的URL
    老师:
    hive> select distinct n.uid from (select * from sogou_view where keyword ='赶集网')
    and  substr(ts,9,2) in ('07','08','09')) n where n.url like '%ganjin.com%';
    自己:
    hive> select uid  from sogou_view where (cast(substr(ts,9,2) 
    as int)>7  or cast(substr(ts,9,2) as int)<9) and url 
    like '%www.ganji.com%' or keyword like '%赶集网%' ;
    或者
    hive>select uid  from sogou_view where substr(ts,9,2) in ('07','08','09') and url
    like '%www.ganji.com%' and  keyword like '%赶集网%' ;

90

    rank<3的搜索中，多少用户的点击次数>2
    老师:
    hive>select a.uid from (select uid,count(*) as cnt from (select * from sogou_view where
    rank<3) e group by e.uid having cnt>2) a;
    自己:
    hive>select  uid,count(uid) as nct from sogou_view 
    where rank<3  group by uid having nct>2;




=======================

hive设计模式

=======================

    1.表的划分方式:按天划分如table_2011_01_01
    2.分区:hive中的分区功能很有用,
    3 最原始的数据尽量少使用分区,
      经过加工后的数据可以用分区.
    4 表与分区的字段不能重复
    5 分区有级别 根据实际的业务自定义分区
      create table supply () partitioned by();

91  同一份数据多种处理

    hive>insert overwrite table sogou_20111230_rank
    select * from sogou_20111230 where rank=3;



92

    hive>insert overwrite table sogou_20111230_order
    select * from sogou_20111230 where order=3;

    上面两句(91  92)合并成一句(93)如下

93

    hive>from sogou_20111230  
    insert overwrite table sogou_20111230_rank 
    select * where  rank =3 
    insert overwrite table sogou_20111230_order 
    select * where order=3;

94 为表增加列 (只能末尾追加)

    ALTER TABLE sogou_20111230 ADD COLUMNS (user_id string) ;

    列的存储有两种格式ORC和RCFile

========================================
    
    Hive内置函数和UDF(用户自定义函数)

========================================


95 查看内置函数

hive> show functions; 

96 查看某一函数具体描述

    hive>describe function 函数名;

    一般聚合函数与group by 组合使用
    分3种:
    1 UDF(标准函数):普通函数
    2 UDAF(用户自定义聚合函数):多行多列变一行
    3 UDTF(用户自定义表生成函数):多行多列变多行

==UDF操作过程==

91 在eclipse中创建java类 如UDFZodiacSign

92 添加UDFZodiacSign的jar包

    hive>add jar /home/udf.jar 

93 创建外部表如little_bigdata

    hive>create external table if not exists 
    little_bigdata(name string,email string,bday 
    string,ip string, gender string, anum int) 
    row format delimited fields terminated by ',';

94 创建zodiac作为UDFZodiacSign类的临时函数 as'包名.类名' 

    hive>create temporary function zodiac as 'day1008.UDFZodiacSign';

95 查看zodiac是否OK

    hive> describe function zodiac;

96 将little_bigdata表中name字段中数据传入临时函数zodiac中
    
    hive> select zodiac(name) from little_bigdata; 

============================================

97 统计没有农产品市场的省份有哪些

    马:
    hive> select e.name from (
    select distinct prov from product
    ) a right outer join province e on a.prov = e.name
    where a.prov is null

98统计排名前 3 的省份共同拥有的农产品类型

    1计算前三省份的名称
    2计算前三省份的所有去重产品名称
    3计算共同拥有的产品
    数据按A  B  C  D  E 步骤计算
    hive>select c.name,count(*) as ct from 
    E 列出前三省相同的熟菜,并计数
    (select a.prov,a.name from 
    D 从A数据中比较与B中前三个相同列 的省份及其熟菜
    (select prov,name from product group by prov,name
    A 分组列出所有省,及其所在省的熟菜(分组就是去重)
    ) a 
      left semi join
    (select p.prov,count(*) as cnt from 
    C 对不同省份计数 省1  number1  省2  number2
    并按降序排列列出前三个省
    (select prov,name from product group by prov,name
    B 分组列出所有省,及其所在省的熟菜(分组就是去重)
    ) p 
      group by p.prov order by cnt desc limit 3
    ) b
      on a.prov = b.prov
    
    ) c group by c.name having ct > 2


-------------------------------------------------------------------------------------
    hive> select (2015-age)as ag  ,sex  from car_1  where age !=null or sex !="";

    hive> select m.ag,count(*) as nct from
        (select (2015-age) as ag ,sex  from car_1  where age !=null or sex !="") 
        m  group by m.ag;
--------------------------------------------------------------------------------------


=============================
  
  自定义Hive文件和记录格式
  
=============================

hive三种文件格式:textfile sequencefile  rcfile
前两种一行存储  rcfile以列存储
他们影响整个文件格式

sequencefile  与 textfile  文件格式在读取效率上
testfile更高些

默认分隔符格式/001 即是Ctr+A
stored  as  textfile 表文件的存储格式

99 创建sequencefile格式的表

    hive>create  external  table sogou_20111230_seq(ts string,
    uid string,keyword string,rank int,order int
    ,url string) row format delimited fields 
    terminated by '\t' stored as sequencefile;

100 向该表中插入数据

    hive>insert table sogou_20111230_seq select 
    ts,uid,keyword,rank,order,url from 
    sogou_20111230 limit 50000;

101 创建rcfile格式的表:基于列式存储
  
    hive>create table sogou_20111230_rc(ts string,
    uid string, keyword string,rank int, order 
    int, url string) row format delimited fields
    terminated by '\t' stored as rcfile;

102 向该表中插入数据

    hive>insert overwrite table sogou_20111230_rc 
    select ts, uid,keyword,rank,order,url
    from ext_sogou_20111230 limit 50000;

103 记录格式 SerDe是序列化/反序列化的简写

104 CSV和TSV SerDe(csv内部实现各式逗号分割\n换行)

    hive 记录格式:影响文件内部数据存储格式
105 XPath相关的函数

    hive>SELECT xpath ('
          <a><b id="foo">bl</b>
          <b id="bar">b2</b></a>','//@id' )
          FROM car_1 LIMIT 1;


106 计算北京市的每种农产品的价格波动趋势，即计算每天价格均值，并按照时间先后顺序排列该值。
  
    某种农产品的价格均值计算公式：
    PAVG = (PM1+PM2+...+PMn-max(P)-min(P))/(N-2)
    其中， P 表示价格， Mn 表示 market，即农产品市场。 PM1 表示 M1 农产品市场的该产品价
    格， max(P)表示价格最大值， min(P)价格最小值。

    思路:

    第一步:筛选出1-5天内 时间 熟菜名称  两个字段 
    第二步:用if三目运算,判断各种熟菜波动次数是否大于2次,
    第三步:求平均值

    hive>select m.date,m.name,if(count(*)>2,
    round((sum(m.price)-max(m.price)-min(m.price))/(count(*)-2),2),
    round(sum(m.price)/count(*),2))
    from ( 
    select * from product_20140101 where province='北京'
    union all
    select * from product_20140102 where province='北京'
    union all
    select * from product_20140103 where province='北京'
    union all
    select * from product_20140104 where province='北京'
    union all
    select * from product_20140105 where province='北京'
    ) m  
    group by m.date,m.name;

107  使用简单时间序列算法， 设置 N=3，预测 1.4、 1.5 日的平均价格
    
    hive>create table price_hg_pre0104(ptime TIMESTAMP,name STRING,price FLOAT);

    hive>insert overwrite table price_hg_pre0104
    select * from price_hg where day(cast(ptime as string)) < 4
    union all
    select cast('2014-01-04 00:00:00' as timestamp) as ptime,'黄瓜' as name,sum(price)/3 as price from price_hg where day(cast(ptime as string)) < 4

108  并计算与实际数据的平方误差和
  
    hive>create table price_hg_pre0105(ptime TIMESTAMP,name STRING,price FLOAT);

    hive>insert overwrite table price_hg_pre0105
    select cast('2014-01-05 00:00:00' as timestamp) as ptime,'黄瓜' 
    as name,sum(price)/3 as price from price_hg_pre where day(cast(ptime as string)) < 5
    and day(cast(ptime as string)) > 1



109 表添加一列 ：

    hive> ALTER TABLE pokes ADD COLUMNS (new_col INT);



110 添加一列并增加列字段注释

    hive> ALTER TABLE invites ADD COLUMNS (new_col2 INT COMMENT 'a comment');

111 更改表名：

    hive> ALTER TABLE events RENAME TO 3koobecaf;
112 删除列：hive> DROP TABLE pokes;

113增加、删除分区

    •增加

    ALTER TABLE table_name ADD [IF NOT EXISTS] partition_spec [ LOCATION 'location1' ] partition_spec [ LOCATION 'location2' ] ...
      partition_spec:
    : PARTITION (partition_col = partition_col_value, partition_col = partiton_col_value, ...)

    •删除
    ALTER TABLE table_name DROP partition_spec, partition_spec,...
        REPLACE则是表示替换表中所有字段。

114 重命名表•

    ALTER TABLE table_name RENAME TO new_table_name

115 修改列的名字、类型、位置、注释：
    
    ALTER TABLE table_name CHANGE [COLUMN] col_old_name col_new_name column_type [COMMENT col_comment] [FIRST|AFTER column_name]

    •这个命令可以允许改变列名、数据类型、注释、列位置或者它们的任意组合

116 表添加一列 ：

    hive> ALTER TABLE pokes ADD COLUMNS (new_col INT);

117 添加一列并增加列字段注释

    hive> ALTER TABLE invites ADD COLUMNS (new_col2 INT COMMENT 'a comment');

118增加/更新列
   
    ALTER TABLE table_name ADD|REPLACE COLUMNS (col_name data_type [COMMENT col_comment], ...)  
    复制代码

    • ADD是代表新增一字段，字段位置在所有列后面(partition列前)

119   

    create external table logs (ip string ,name1 string,name2 string,name3 string ,name4 string ,name5  string, name6 string, name7 string, name8 string,name9 string,name10 string,name11 string) row format delimited fields  terminated by ' ';

    select name1 from (select  as c  from  logs where ip ='58.214.255.146';

    数据格式：

    183.166.128.178 -       -       [09/Apr/2016:07:58:33   +0800]  "POST   /boss/service/newCode.htm      HTTP/1.1"       200     227     "-"     "-"
120正序：

    select ip ,sum(name9) as c from logs where name3 like '[09/Apr/2016:07:55%' group by ip order by c desc;

121 逆序：
    
    select  name6,count(1) as b from logs where name3  like '[09/Apr/2016:07:5%' group by name6 order by b asc;
122 逆序：

    select  name6,count(1) as b from logs where name3  like '[09/Apr/2016:07:5%' group by name6 sort by b asc;

123取前一千行放到一个新表里

    hive> insert into table hivecontain_small            
    > select * from hivecontain limit 1000;

124 更新表字段

    hive>insert overwrite table province_city_scenic_per_nums select spot_name, spot_city, substring(round(per,4),0,6) ,nums from province_city_scenic_per_nums ;

125 截取表字段部分值并插入新表

    hive> insert table province_city_scenic_per_nums select spot_name, spot_city, substring(round(per,4),0,6) ,nums from province_city_scenic_per_nums ;
126.tourist_consume_details 用户消费信息（金额、订单数、游玩人次）

    select link_name, sex, city ,tel, certificate_no ,sum(close_total_price) as total_price ,sum(popnum) as popnum,count(tourname) as  tournum from order_raw_info 
    group by link_name,sex,city ,tel,certificate_no;

127.bucketed_user 分桶查询随机id

    select * from bucketed_user  TABLESAMPLE(BUCKET 1 OUT OF 4 ON rand())

128.bucketed_user 创建带桶的外部表

    create external  table if not exists  bucketed_user2(id int,name string) clustered by (id) sorted by(name) into 4 
    buckets row format delimited fields terminated by ',' stored as textfile location  '/kafka/' ;

129.province_city_scenic_per_nums 表字段的截取

    select spot_name, spot_city, substring(round(per,4),0,6) ,nums from   province_city_scenic_per_nums ;

130.province_city_scenic_per_nums 表字段更新(如0.001242更新为0.001)

    insert overwrite table province_city_scenic_per_nums select spot_name, spot_city, substring(round(per,4),0,6) ,nums from province_city_scenic_per_nums ;

131.改表字段

    alter table scenic_tour_info  change `spotname` spot_name string;

132.split使用

    select split("13901888346","1390188")[1] from quyu_visit_info limit 10;

133.quyu_visit_info 按条件插入表数据

    insert into table quyu_visit_info  select u.visitor_id, u.tel, u.city from solo_mobile_quyu u limit 100;

134.tourt_ype_date_total (new) 景区类型（按时间分组）游客量统计

    select * from(
    select  p.date, p.tour_type,count(p.date) total
    from (
          select tour_type, substr(occ_date, 0,4) as date  
          from scenic_tour_info ) p 
    where p.date like '201%' 
    group by p.tour_type, p.date 
    order by p.date desc ) t 
          where t.date='2013' or t.date='2014' or t.date='2015' or t.date='2016';

135.date_spotprovince_type_total 按省份统计 景区类型（按时间分组）游客量统计

    select * from(
      select  p.date, p.spot_province, p.tour_type as scenic_type,count(p.date) total
      from (
              select spot_province,  tour_type, substr(occ_date, 0,4) as date  
              from scenic_tour_info ) p 
      where p.date like '201%' 
      group by  p.spot_province,p.tour_type, p.date 
      order by p.date desc ) t 
              where t.date='2013' or t.date='2014' or t.date='2015' or t.date='2016' ;
136.scenic_city_province_per_nums 统计某省各景区客流量的比重（占该省比重）及其客流量

    select distinct p.spot_name, p.spot_city, (p.nums/5358582) per  ,p.nums
    from province_city_scenic_nums p join province_tour_nums  c 
    on  p.spot_province='浙江省' 
    order by per desc 
137.表重命名

    ALTER TABLE tour_info_detail RENAME TO new_name;  scenic_info_detail  ;
138.rename_ziduan 重命名表字段名

    alter table scenic_info_detail  change  `proname` spotprovince string;
