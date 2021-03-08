# mongo 库使用中的常用脚本

## 备份

- 用于备份 mongod 指定数据库中的数据，服务器端关闭认证

  ```sh
  mongodump --host $1 --port $2 -d $6 -o $7
  ```

  说明:

  - 参数 -o

    备份的数据存放位置，例如：c:\data\dump，当然该目录需要提前建立，在备份完成后，系统自动在 dump 目录下建立一个 test 目录，这个目录里面存放该数据库实例的备份数据。

- 用于备份 mongod 指定数据库中的数据，服务器端开启认证

  ```sh
  mongodump --host $1 --port $2 -u $3 -p $4 --authenticationDatabase $5 -d $6 -o $7
  ```

  说明:

  - authenticationDatabase 权限授权所在库 一般为 admin

## 恢复

- 用于恢复 mongod 指定数据库中的数据，服务器端关闭认证

  ```sh
  mongorestore --host=$1 --port=$2  --db=$6 $7
  ```

- 用于恢复 mongod 指定数据库中的数据，服务器端开启认证

  ```sh
  mongorestore --host=$1 --port=$2  --username=$3  --password=$4  --authenticationDatabase=$5 --db=$6 $7
  ```

- 命令参数说明

- --db , -d ：

  需要恢复的数据库实例，例如：test，当然这个名称也可以和备份时候的不一样，比如 test2

- --drop：

  恢复的时候，先删除当前数据，然后恢复备份的数据。就是说，恢复后，备份后添加修改的数据都会被删除，慎用哦！

- \<path>：

  mongorestore 最后的一个参数，设置备份数据所在位置，例如：c:\data\dump\test。

  你不能同时指定 \<path> 和 --dir 选项，--dir 也可以设置备份目录。

- --dir：

  指定备份的目录

  你不能同时指定 \<path> 和 --dir 选项。
