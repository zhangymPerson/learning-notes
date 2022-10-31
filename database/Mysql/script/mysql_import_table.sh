#!/usr/bin/env bash

function importTable {
    echo "要导入的文件为：${filename}"
    echo "mysql -h${host} -u${user} -p${password} ${db} < '${filename}'"
    # 执行过程测试时可以注释掉
    # mysql -h${host} -u${user} -p${password} ${db} <"${filename}"
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

    # 导入的数据库配置
    host=127.0.0.1
    user=root
    password=123456
    db=test

    if [ $# -eq 1 ]; then
        filename=$1
    else
        echo "需要一个参数，指定导入的 sql 文件"
        exit
    fi

    importTable
    exit 0
}
main "$@"
