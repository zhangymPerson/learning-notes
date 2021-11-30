#!/usr/bin/bash

# 导出数据库中的指定表数据
echo "导出数据库脚本开始执行"

# 导出的数据库配置
host=127.0.0.1
user=root
password=123456
db=danao

if [ $# -eq 1 ]; then
    table=$1
else
    echo "需要一个参数，指定备份表名"
    exit
fi

function exportTable() {
    echo "导出的表名为：${table}"
    mysqldump -h${host} -u${user} -p${password} ${db} ${table} >"${table}.sql"
    if [ $? -eq 0 ]; then
        echo "导出成功，文件是$(pwd)/${table}.sql"
    else
        echo "导出失败，检查数据连接参数，数据库和表名是否存在"
    fi
}

# 调用函数
exportTable
