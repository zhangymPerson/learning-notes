#!/usr/bin/env bash

# 脚本内容输出到文件
# 脚本输出到文件
# exec > $0".log"

function readFile {
    if [ $# -eq 0 ]; then
        echo "文件名不能为空"
        exit 1
    fi
    local name=$1
    echo "读取文件"${name}
    # 按行读取文件
    for key in $(cat ${name}); do
        echo "读取到 [${key}]"
    done
}

# 判断是否是文件
function isExist {
    if [ $# -eq 0 ]; then
        echo "文件名不能为空"
        exit 1
    fi
    fileName=$1
    if [ -e ${fileName} ]; then
        echo "文件[${fileName}]存在"
        for line in $(cat ${fileName}); do
            echo ${line}
        done
    else
        echo "文件[${fileName}]不存在"
    fi
}

# 创建文件
function createFile {
    if [ $# -eq 0 ]; then
        echo "文件名不能为空"
        exit 1
    fi
    # Shortest
    file=$1
    echo "要创建的文件是[${file}]".
    echo "test tste tetst" >${file}

    # Longer alternatives:
    # : >${file}
    # echo -n >${file}
    # printf '' >${file}
}

main() {

    set -o errexit
    set -o pipefail
    set -o nounset

    local -r __dirname="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    local -r __filename="${__dirname}/$(basename "${BASH_SOURCE[0]}")"

    fileName="test.log"
    createFile ${fileName}
    isExist ${fileName}
    readFile ${fileName}
    exit 0
}
main "$@"
