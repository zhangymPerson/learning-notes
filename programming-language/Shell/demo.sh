#!/bin/bash
# user: danao
# date: 2021-08-27
# 作用: demo script

# debug模式需开启
# set -x # set -o xtrace

set -e          # set -o errexit 有错误退出
set -u          # set -o nounset
set -o pipefail #管道执行过程中有错误退出

# 2. 环境变量
#PATH=/home/abc/bin:$PATH
#export PATH

# 3. source文件
#source lib/a.sh

# 4. 常量
#readonly PI=3.14

# 5. 变量
#var=1

# 6. 函数
# 函数注释
# 函数内不能为空
function run() {
    echo "run args is" "$@"
    return
}

function main() {
    #函数调用
    run "$@"
}

# 7. 主函数/主逻辑
main "$@"
