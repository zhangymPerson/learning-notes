# sqoop 使用过程中的密码提供的几种方式

我们可以看到在导入命令使用中关于密码使用的三种方式：


(1) --password


明文密码：
```sh
sqoop import \
	--connect jdbc:mysql://mdp5:3306/precmarket \
	--username sqoop \
	--password sqoop \
	--table d_area \
	--as-textfile \
	--target-dir /sqoop_training/d_area_1.textfile \
	--compress \
	--null-string '\\N' \
	--null-non-string '\\N' \
	--num-mappers 1 \
	--delete-target-dir \
	--direct

```
(2) -P

-P：这个参数指定命令执行通过交互式方式提示用户输入密码。

这种方式避免了数据库密码直接以明文的形式出现，因而防止了密码的泄露，但是它只能在终端状态下使用，一般也只用于命令行中提交一些简单的测试任务，无法应用于后台自动执行这样的应用场景下。


交互式输入密码：
```sh
sqoop import \
--connect jdbc:mysql://mdp5:3306/precmarket \
--username sqoop \
-P \
--table d_area \
--as-textfile \
--target-dir /sqoop_training/d_area_1.textfile \
--compress \
--null-string '\\N' \
--null-non-string '\\N' \
--num-mappers 1 \
--delete-target-dir \
--direct


```

(3) --password-file


读取存放明文的密码文件
--password-file：这个控制参数通过指定一个保存密码的文件路径来提供数据库数据访问密码。

这种方式是比较安全的密码提供方式之一，但是需要保证以下三点：
(1) 保存密码的文件创建并保存在当前用户的home目录下
(2) 保存密码的文件的访问权限设置成400，即只有当前用户自己可以访问，其他用户无任何访问权限
(3) 由于Sqoop将读取保存密码的文件中的全部内容作为密码。这将包括任何尾部的空白字符，比如换行或者其他编辑器默认添加的结尾字符。所以需要保证存入该文件中的字符完完整整是你的密码字符串。我们可以通过使用echo –n “secret” > password.file 方式来去除尾部多余的空白结束符。

这里需要强调一点的是，sqoop在执行命令过程中将读取密码文件传递到MapReduce 集群，这个保存密码的文件可以保存在本地也可以保存在HDFS上；如果是本地需要在指定—password-file参数时加file:/// 路径前缀；如果是保存在HDFS上，在指定—password-file参数值时需要指定hdfs://文件系统路径前缀。具体例子如下：

(1) 首先我们创建用于保存密码的文件password.file, 我们假设当前用户是mnt， 数据库密码是sqoop。
```
[mnt /home/mnt] echo –n “mnt_password” > /home/mnt/.password.file


sqoop import \
--connect jdbc:mysql://mdp5:3306/precmarket \
--username sqoop \
--password-file file:///home/mnt/.password.file \
--as-textfile \
--target-dir /sqoop_training/d_area_1_password_file.textfile \
--compress \
--null-string '\\N' \
--null-non-string '\\N' \
--num-mappers 4 \
--delete-target-dir \
--direct \
--query 'select * from d_area where id > 10000 and $CONDITIONS' \
--split-by 'id'


```

首先我们将步骤(1) 中创建的.password.file 上传到hfds的/usr/mnt目录下
```

[mnt /home/mnt] hadoop fs –copyFromLocal /home/mnt/.password.file /user/mnt


 基于HDFS文件系统指定密码文件的方式，命令如下：
sqoop import \
--connect jdbc:mysql://mdp5:3306/precmarket \
--username sqoop \
--password-file hdfs://user/mnt/.password.file \
--as-textfile \
--target-dir /sqoop_training/d_area_1_password_file.textfile \
--compress \
--null-string '\\N' \
--null-non-string '\\N' \
--num-mappers 4 \
--delete-target-dir \
--direct \
--query 'select * from d_area where id > 10000 and $CONDITIONS' \
--split-by 'id'

```

(4) –password-alias


从Hadoop2.6.0开始提供了单独的API用于将密码存储和应用分离。具体的API就是hadoop credential, 关于该命令在密码生成和存储上的使用，我们将在下文具体说明。从上面的英文介绍，我们得到第四种密码使用方式：

方式四：--password-alias [别名方式]

**Hadoop2.6.0 之后的版本提供了一个API用于将密码存储和应用程序分离。这个API被称为凭证提供的API，并提供了一个新的命令行工具来管理密码及其别名。密码及其别名一起被存储在密码保护的密钥库中。密钥库密码可以通过控制台交互提示输入提供给应用程序或者作为代码中的变量来提供。**

一旦在密钥库中存储了密码及其别名，在应用程序中便可以选择使用别名代替实际密码，并在运行时解析别名以使用密码。这样只有别名在配置文件或者命令中是可见的，这样可以防止密码的泄露。Sqoop基于Hadoop提供的这种功能丰富了密码管理功能，只要底层hadoop支持通过使用密钥库来管理密码及其别名，那么通过使用—password-alias 指定密码对应的别名即可。 

这里我们通过脚本来说明具体的步骤：
(1) 首先生成jceks文件，支持本地存储模式和HDFS文件系统存储模式：
本地密钥库模式：

```sh

hadoop credential create mydb.password.alias -provider localjceks://file/tmp/mysql.password.jceks
命令行提示输入密码：sqoop [Enter]
确认密码：sqoop [Enter]
完成。


```
HDFS密钥库模式：
  (i) 上传本地生成好的密钥库到HDFS指定目录：

hadoop fs -copyFromLocal /tmp/mysql.password.jceks  /user/sqoop/ 
 (ii)  命令直接生成基于HDFS存储的密钥库：
 ```sh
 hadoop credential create mysql.pwd.alias -provider jceks://hdfs/user/password/mysql.pwd.jceks
命令行提示输入密码：sqoop [Enter]
确认密码：sqoop [Enter]
完成。

```
2) 通过使用—password-alias参数指定密码对应的别名来指定sqoop import任务：
 本地密钥库模式：
 ```
sqoop import \
-Dhadoop.security.credential.provider.path=localjceks://file/tmp/mysql.password.jceks \
--connect 'jdbc:mysql://mdp5:3306/precmarket' \
--table d_area  \
--username sqoop \
--password-alias mydb.password.alias \
--delete-target-dir \
--target-dir /sqoop_training/2.textfile


 ```

 HDFS密钥库存储模式：
 ```

 sqoop import \
-Dhadoop.security.credential.provider.path=jceks://hdfs/user/sqoop/mysql.password.jceks \
--connect 'jdbc:mysql://mdp5:3306/precmarket' \
--table d_area  \
--username sqoop \
--password-alias mydb.password.alias \
--delete-target-dir \
--target-dir /sqoop_training/3.textfile


```

所以在使用密钥库提供密码的方式时，需要注意以下几点：
(1)基于HDFS存储密钥库的方式，需要在本地生成密钥库之后上传到hdfs指定目录，之后通过—password-alias指定具体的密码别名，使用-Dhadoop.security.credential.provider.path 控制参数来指定hdfs文件系统上的密钥库文件路径
(2)基于本地文件系统存储密钥库方式。
通过—password-alias 指定具体的密码别名，使用-Dhadoop.security.credential.provider.path 控制参数来指定本地文件系统上的密钥库文件路径
