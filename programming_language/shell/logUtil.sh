#!/bin/bash

#日志级别 debug-1, info-2, warn-3, error-4, always-5
LOG_LEVEL=1

#日志文件
LOG_FILE=./log.log

#调试日志
function log_debug() {
    content="[DEBUG]$(date '+%Y-%m-%d %H:%M:%S') $*"
    [ $LOG_LEVEL -le 1 ] && echo "${content}" >>$LOG_FILE && echo -e "\033[32m" "${content}" "\033[0m"
}
#信息日志
function log_info() {
    content="[INFOS]$(date '+%Y-%m-%d %H:%M:%S') $*"
    [ $LOG_LEVEL -le 2 ] && echo "${content}" >>$LOG_FILE && echo -e "\033[32m" "${content}" "\033[0m"
}
function log() {
    content="[INFOS]$(date '+%Y-%m-%d %H:%M:%S') $*"
    [ $LOG_LEVEL -le 2 ] && echo "${content}" >>$LOG_FILE && echo -e "\033[32m" "${content}" "\033[0m"
}
#警告日志
function log_warn() {
    content="[WARNS]$(date '+%Y-%m-%d %H:%M:%S') $*"
    [ $LOG_LEVEL -le 3 ] && echo "${content}" >>$LOG_FILE && echo -e "\033[33m" "${content}" "\033[0m"
}
#错误日志
function log_err() {
    content="[ERROR]$(date '+%Y-%m-%d %H:%M:%S') $*"
    [ $LOG_LEVEL -le 4 ] && echo "${content}" >>$LOG_FILE && echo -e "\033[31m" "${content}" "\033[0m"
}

# 测试
# 其他包使用方式 source logUtil.sh
log_debug "this is debug log..."
log_info "this is info log..."
log_warn "this is warn log..."
log_err "this is error log..."
log "test"
