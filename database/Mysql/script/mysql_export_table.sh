#!/usr/bin/bash

function exportTable() {
    echo "导出的库[$db]的表名[${table}]"
    date=$(date +"%Y%m%d%H%M%S")
    echo "mysqldump -h${host} -u${user} -p${password} ${db} ${table} > '${table}-${date}.sql'"
    # 执行行测试时 可以注释掉
    mysqldump -h${host} -u${user} -p${password} ${db} ${table} >"${table}-${date}.sql"
    if [ $? -eq 0 ]; then
        echo "导出成功，文件是$(pwd)/${table}.sql"
    else
        echo "导出失败，检查数据连接参数，数据库和表名是否存在"
    fi
}

main() {

    set -o errexit
    set -o pipefail
    set -o nounset

    local -r __dirname="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local -r __filename="${__dirname}/$(basename "${BASH_SOURCE[0]}")"

    # 导出数据库中的指定表数据
    echo "导出数据库 单张表的脚本开始执行"

    # 导出的数据库配置
    host=127.0.0.1
    user=root
    password=123456
    db=test

    if [ $# -eq 1 ]; then
        table=$1
    else
        echo "需要一个参数，指定备份表名"
        exit
    fi

    # 调用函数
    exportTable

    exit 0
}
main "$@"
