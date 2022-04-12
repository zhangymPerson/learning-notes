#!/bin/bash

# 输出shell日志到指定文件
# shell 日志简单记录
# exec >>${0}.exec.log

# 日志函数
# 日志写入当前目录下 脚本名.log
# 日志输出到文件
function Log() {
    # echo "参数个数:"$#
    path=$(pwd)
    fileName=${0}.log
    # 日期格式 可修改
    date=$(date +"%Y-%m-%d %H:%M:%S")
    if [ $# -eq 1 ]; then
        info=[$date]"[INFO]:脚本"$0"中:"$1
    else
        info=[$date][$1]":脚本"$0"中:"$2
    fi
    # 写文件
    echo $info >>$path$fileName
    # 直接打印
    # echo $info
}

# 调用方式
# Log INFO info-message
# Log info-message-test
# Log ERROR error-message
# Log WARN warning-message

#################################################
# shell 日志
#################################################
#日志级别 debug-1, info-2, warn-3, error-4, always-5
LOG_LEVEL=0
#日志文件
LOG_FILE=./debug.log
#调试日志
function log_debug() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[$0][DEBUG]:$@"
    [ $LOG_LEVEL -le 1 ] && echo $content >>$LOG_FILE && echo -e "\033[32m" ${content} "\033[0m"
}
#信息日志
function log_info() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[INFO]:$@"
    [ $LOG_LEVEL -le 2 ] && echo $content >>$LOG_FILE && echo -e "\033[32m" ${content} "\033[0m"
}
#警告日志
function log_warn() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[WARN]:$@"
    [ $LOG_LEVEL -le 3 ] && echo $content >>$LOG_FILE && echo -e "\033[33m" ${content} "\033[0m"
}
#错误日志
function log_err() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[ERROR]:$@"
    [ $LOG_LEVEL -le 4 ] && echo $content >>$LOG_FILE && echo -e "\033[31m" ${content} "\033[0m"
}
#一直都会打印的日志
function log_always() {
    content="$(date '+%Y-%m-%d %H:%M:%S')[ALWAYS]:$@"
    [ $LOG_LEVEL -le 5 ] && echo $content >>$LOG_FILE && echo -e "\033[32m" ${content} "\033[0m"
}

# 测试
# 其他包使用方式 source logUtil.sh
# log_debug "this is debug log..."
# log_info "this is info log..."
# log_warn "this is warn log..."
# log_err "this is error log..."
# log_always "this is always log.."
