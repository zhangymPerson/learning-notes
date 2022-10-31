#!/usr/bin/bash

echo "清空数据表脚本执行"

# 数据库配置
host=127.0.0.1
user=root
password=123456
db=test

# 要清空的表由 脚本输入 sh demo.sh tableName
if [ $# -eq 1 ]; then
    table=$1
else
    echo "需要一个参数，指定要清空的表名"
    exit
fi

date=$(date +"%Y%m%d-%H%M%S")

# 清空一张表
function truncateTable() {
    mysql -u${user} -p${password} ${db} -e "truncate ${table}"
    if [ $? -eq 0 ]; then
        echo "清空表${table}成功"
    else
        echo "清空表${table}失败"
        exit
    fi
}

# 导出备份一张表
function exportTable() {
    echo "需要清空的表名为：${table}"
    fileName="${table}-${date}.sql"
    mysqldump -h${host} -u${user} -p${password} ${db} ${table} >${fileName}
    if [ $? -eq 0 ]; then
        echo "备份成功，文件是$(pwd)/${fileName}"
        truncateTable
    else
        echo "导出失败，检查数据连接参数，数据库和表名是否存在"
        echo "清空表数据失败"
        exit
    fi
}

exportTable
