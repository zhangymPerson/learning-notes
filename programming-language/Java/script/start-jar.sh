#!/bin/bash

function logs() {
    date=$(date +'%Y-%m-%d %H:%M:%S')
    echo "${date}" $*
}

# 打印日志 调用方式 log info
function log() {
    logs INFO $*
}

# 启动
start() {
    nohup java -jar $1 &
    log start success
}

# 编辑测试代码
# 输出日志
jarName=
rm ./nohup.out 
log "start jar name (启动的jar包) :" ${jarName}
start ${jarName}
