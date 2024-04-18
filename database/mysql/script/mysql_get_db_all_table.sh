#!/bin/env bash

###########################################################
# @file : mysql_get_db_all_table.sh
# @desc : 脚本执行方式 [bash mysql_get_db_all_table.sh]
#         脚本说明:获取数据库中所有表
# @date : 2024-04-18 11:25:55
# @auth : test
# @version : 1.0
###########################################################

# set -o xtrace debug模式需开启
# set -x

# set -o errexit 有错误退出
set -e
# set -o nounset
set -u
# 管道执行过程中有错误退出
set -o pipefail
# 输出脚本中相关内容 到脚本文件名对应的log文件中
# debug时 可以开启
# exec >>${0}.log

# MySQL连接信息  
MYSQL_USER="root"  
MYSQL_PASSWORD="123456"  
MYSQL_HOST="127.0.0.1"  
MYSQL_DATABASE="database_name"  
MYSQL_PORT="3306"

# 查询所有表名
SQL="select table_name from information_schema.tables where table_schema = '${MYSQL_DATABASE}' and table_rows > 0 order by table_rows desc;"
  
# sql 查询表和数据量
# SQL="select table_name, table_rows from information_schema.tables where table_schema = '${MYSQL_DATABASE}' and table_rows > 0 order by table_rows desc ; "
echo "SQL:"
echo "==================="
echo "$SQL"
echo "==================="
echo "mysql -h $MYSQL_HOST -P $MYSQL_PORT -u $MYSQL_USER -p$MYSQL_PASSWORD -Nse '$SQL' "
# 使用mysql命令获取所有表名和数据量  
mysql -h $MYSQL_HOST -P $MYSQL_PORT -u $MYSQL_USER -p$MYSQL_PASSWORD -Nse "$SQL" 
