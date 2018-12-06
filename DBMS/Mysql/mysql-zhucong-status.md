# 主从状态参数说明

- 从库上执行 

    show slave status\G;

- 参数说明

|参数|参数值|参数说明|备注|
|-|-|-|-|
Slave_IO_State|Waiting for master to send event|这个是指Slave连接到Master的状态，就是当前IO线程的状态，MySQL主从复制线程状态转变。|
Master_Host|具体ip|主库的IP地址||
Master_User|username|从库读取主库的用户名||
Master_Port|3306|主库的数据库端口号||
Connect_Retry|60|连接尝试次数，使用change master时可以使用master-connect-retry选项指定当前值。||
Master_Log_File|mysql-bin.000*** |显示当前I<br>O线程当前正在读取的主服务器二进制日志文件的名称<br>一般显示是mysql-bin.000*** |
Read_Master_Log_Pos|一串数字|显示当前同步到主服务器上二进制日志的偏移量，I<br>O线程已经读取的位置，单位是字节，上述的示例显示当前同步到mysql-bin.010362的555176471偏移量位置，即已经同步了mysql-bin.010362这个二进制日志中529MB（555176471<br>1024<br>1024）的内容。|
Relay_Log_File|mysql-slave-relay-bin.000762|显示Slave的SQL线程当前正在读取和执行的中继日志文件的名称|
Relay_Log_Pos||显示在当前的中继日志中，Slave的SQL线程已读取和执行的中继日志的偏移量。
|
Relay_Master_Log_File|mysql-bin.000***|显示Slave中继日志同步到Master的二进制日志文件|
Slave_IO_Running|Yes|显示I<br>O线程是否被启动并成功地连接到主服务器上，成功为Yes，否则为No。
Slave_SQL_Running|Yes|显示SQL线程是否被启动，启动为Yes，否则为No。|
Replicate_Do_DB<br>Replicate_Ignore_DB<br>Replicate_Do_Table<br>Replicate_Ignore_Table<br>Replicate_Wild_Do_Table<br>Replicate_Wild_Ignore_Table||这些参数都是为了用来指明哪些库或者表在复制的时候不要同步到备库，但是这些参数用的时候要小心，因为当跨库使用的时候可能会出现问题。另外当仅忽略或仅允许多个库或表时，要多次使用忽略语句才可以。||
Last_Errno<br>Last_Error||显示Slave的SQL线程读取日志参数的的错误数量和错误消息，错误数量为0并且消息为空字符串表示没有错误；如果Last_Error值不是空值，它也会在从属服务器的错误日志中作为消息显示。|
Skip_Counter||显示最近被使用的用于SQL_SLAVE_SKIP_COUNTER的值，就是用于跳过Slave错误的。|
Exec_Master_Log_Pos||表示SQL线程已经执行的Relay log相对于主库二进制日志偏移量的位置。|
Relay_Log_Space||表示所有原有的中继日志结合起来的总大小，在START SLAVE语句的UNTIL子句中指定的值，Until_Condition具有以下值：Until_Condition、Until_Log_File、Until_Log_Pos。|
Until_Log_File<br>Until_Log_Pos||Until_Log_File和Until_Log_Pos用于指示日志文件名和位置值，日志文件名和位置值定义了SQL线程在哪个点中止执行。|
Master_SSL_Allowed||显示了从服务器是否使用SSL连接到主服务器。如果允许对主服务器进行SSL连接，则值为Yes；如果不允许对主服务器进行SSL连接，则值为No；如果允许SSL连接，但是从服务器没有让SSL支持被启用，则值为Ignored。
Master_SSL_CA_File<br>Master_SSL_CA_Path<br>Master_SSL_Cert<br>Master_SSL_Cipher<br>Master_SSL_Key||如果Slave使用SSL连接Master服务器，这里就会显示对应的证书和私钥信息。使用CHANGE MASTER与SSL相关的选项有：–master-ca,–master-capath,–master-cert,–master-cipher和–master-key等。|
Seconds_Behind_Master||表示主从之间延迟的时间，单位是秒。就是SQL线程当前执行的binlog（实际上是relay log）中的timestamp和IO线程最新的timestamp的差值。|实质上，此字段计算Slave SQL线程和Slave i/o线程之间的时间差 (以秒为单位)。如果主节点和从服务器之间的网络连接速度较快，则Slave i/o线程非常接近主服务器，因此此字段是对从SQL线程与主服务器进行比较的后的一个很好的近似值。如果网络很慢，这不是一个好的近似；从SQL线程可能经常被从i/o线程所捕获，因此Seconds_Behind_Master通常显示值为0，即使i/o线程比主服务器慢很多。换言之，此列仅适用于快速网络。|
Master_SSL_Verify_Server_Cert||显示是否认证Master证书。|
Master_Server_Id||显示主服务器的Server_id。|
Using_Gtid||表示是否开启了基于Gtid的复制，开启为Yes，否则为No。|
Gtid_IO_Pos||如果开启了基于Gtid的复制，这里会显示当前执行到的事物ID。|












