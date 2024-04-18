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

# 备份数据的文件名
BACK_FILE="mysql_backup_$(date +%Y%m%d%H%M%S).sql"

# 查询所有表名
SQL="select table_name from information_schema.tables where table_schema = '${MYSQL_DATABASE}' and table_rows > 0 order by table_rows;"
echo "mysql -h $MYSQL_HOST -P $MYSQL_PORT -u $MYSQL_USER -p$MYSQL_PASSWORD -Nse '$SQL' "
# 使用mysql命令获取所有表名和数据量
Tables=$(mysql -h $MYSQL_HOST -P $MYSQL_PORT -u $MYSQL_USER -p$MYSQL_PASSWORD -Nse "$SQL")
# 循环读取 tables 中的值

# 定义一个不要处理的表的数组
no_export_tables=('')

for Table in $Tables; do
    if [[ ! " ${no_export_tables[*]} " =~ ${Table} ]]; then
        echo "Table: $Table backup start"
        # 只备份表结构
        # 参数说明 --compact 压缩输出 --add-drop-table 添加删除表语句 --no-data 只导出表结构
        mysqldump -h $MYSQL_HOST -P $MYSQL_PORT -u $MYSQL_USER -p$MYSQL_PASSWORD --compact --add-drop-table --no-data $MYSQL_DATABASE "${Table}" >>"${BACK_FILE}"
        # 只备份数据
        # 参数说明 --no-create-info 只导出数据 --skip-extended-insert 批量插入语句改成单条插入
        mysqldump -h $MYSQL_HOST -P $MYSQL_PORT -u $MYSQL_USER -p$MYSQL_PASSWORD --compact --no-create-info --skip-extended-insert $MYSQL_DATABASE "${Table}" >>"${BACK_FILE}"
        echo "Table: $Table backup start"
    fi
done

# 备份完成
echo "Backup completed!"

# 批量修改备份中的 排序字符集
sed -i 's/utf8mb4_0900_ai_ci/utf8mb4_general_ci/g' "${BACK_FILE}"
