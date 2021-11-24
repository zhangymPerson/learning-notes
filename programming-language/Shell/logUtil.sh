#!/bin/bash

# 输出shell日志到指定文件
# shell 日志简单记录
exec >>${0}.exec.log

# 日志函数
# 日志写入当前目录下 脚本名.log
# 日志输出到文件
function Log() {
    # echo "参数个数:"$#
    path=${pwd}
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
Log INFO info-message
Log info-message-test
Log ERROR error-message
Log WARN warning-message
