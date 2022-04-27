#!/bin/env bash

###########################################################
# @file : sh-log.sh
# @desc : 脚本执行方式 [bash sh-log.sh]
#         脚本说明: log 日志函数模板
# @date : 2022-04-27 11:22:29
# @auth : test
# @version : 1.0
###########################################################

# set -o xtrace debug模式需开启
# set -x

# set -o errexit 有错误退出
# set -e
# set -o nounset
set -u
#管道执行过程中有错误退出
set -o pipefail
# 输出脚本中相关内容 到脚本文件名对应的log文件中
# debug时 可以开启
# exec >>${0}.log

#################################################
# shell 日志
#################################################
#日志级别 debug-1, info-2, warn-3, error-4, always-5
LOG_LEVEL=0
#日志文件
LOG_FILE=./debug.log
# 当前脚本位置
SHELL_PATH=$(
    cd "$(dirname $0)"
    pwd
)
SHELL_NAME=${0}
SHELL_INFO="脚本所在路径[${SHELL_PATH}],脚本名[${SHELL_NAME}]"
echo ${SHELL_INFO} >>$LOG_FILE && echo -e"\033[32m" ${SHELL_INFO} "\033[0m"
#调试日志
function log_debug() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[${SHELL_NAME}][DEBUG]:$@"
    [ $LOG_LEVEL -le 1 ] && echo $content >>$LOG_FILE && echo -e"\033[32m" ${content} "\033[0m"
}
#信息日志
function log_info() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[INFO][$0]:$@"
    [ $LOG_LEVEL -le 2 ] && echo $content >>$LOG_FILE && echo -e"\033[32m" ${content} "\033[0m"
}
#警告日志
function log_warn() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[WARN]:$@"
    [ $LOG_LEVEL -le 3 ] && echo $content >>$LOG_FILE && echo -e"\033[33m" ${content} "\033[0m"
}
#错误日志
function log_err() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[ERROR][$0]:$@"
    [ $LOG_LEVEL -le 4 ] && echo $content >>$LOG_FILE && echo -e"\033[31m" ${content} "\033[0m"
}
#一直都会打印的日志
function log_always() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[ALWAYS][$0]:$@"
    [ $LOG_LEVEL -le 5 ] && echo $content >>$LOG_FILE && echo -e"\033[32m" ${content} "\033[0m"
}

# 测试
# 其他包使用方式 source logUtil.sh
# log_debug "this is debug log..."
# log_info "this is info log..."
# log_warn "this is warn log..."
# log_err "this is error log..."
# log_always "this is always log.."
