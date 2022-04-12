#!/bin/bash

###########################################################
# @file : demo.sh
# @desc : 脚本执行方式 [bash demo.sh]
#         脚本说明: demo 脚本
# @date : 2022-04-12 15:11:33
# @auth : test
# @version : 1.0
###########################################################

# set -o xtrace debug模式需开启
# set -x

# set -o errexit 有错误退出
set -e
# set -o nounset
set -u
#管道执行过程中有错误退出
set -o pipefail

# 输出脚本中相关内容 到脚本文件名对应的log文件中
# debug时，可以开启
# exec >>${0}.log
now=$(date +"%Y-%m-%d %H:%M:%S")
now=$(date +"%F %T")
echo "script start" ${now}

# 获取当前脚本所在目录
# 获取当前 shell 执行的相对目录  和 绝对目录
# 如 sh demo.sh  sh命令所在文件 和 demo.sh所在位置的相对目录
WD=$(dirname "$0")
WD=$(
    cd "$WD"
    pwd
)
echo ${WD}

# 创建一个环境变量文件 调用
# source ${WD}/setup_env.sh
# echo ${LOCAL_ARCH}

# 获取脚本名称
SHELL_NAME=$(basename "$0")
echo ${SHELL_NAME}

# 2. 环境变量
#PATH=/home/abc/bin:$PATH
#export PATH

# 3. source文件
#source lib/a.sh
# 使用打印日志
source ./logUtil.sh

# 4. 常量
#readonly PI=3.14

# 5. 变量
#var=1

# 6. 函数
# 函数注释
# 函数内不能为空
function run() {
    echo "run args is" "$@"
    log_debug "test"
    log_err "执行错误"
    return
}

function main() {
    #函数调用
    run "$@"
}

# 7. 主函数/主逻辑
main "$@"
