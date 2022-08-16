#!/bin/env bash

###########################################################
# @file : check_server.sh
# @desc : 脚本执行方式 [bash check_server.sh > check_server.log&]
#         脚本说明: 探活脚本
# @date : 2022-07-04 10:28:31
# @auth : test
# @version : 1.0
###########################################################

# 服务名
serverName="test"
# 探活周期 单位为 s
cycle=3
# 日志
log="task.log"
# 服务启动命令 命令必须 & 结尾 创建子进程去执行 别阻塞监控进程
start_cmd="sh test.sh > ${log}"

#######################################
# 函数的作用是:
# 启动服务命令
#######################################
function startServr() {
    echo "${serverName} starting..."
    eval ${start_cmd} &
}

#######################################
# 函数的作用是:
# 监测app是否存活
#######################################
function checkServer() {
    echo "${serverName} 探活监测开启"
    while true; do
        # 获取服务进程ID
        # pgrep 
        pid=$(ps -ef | grep ${serverName} | grep -v grep | wc -l)
        #  如果进程ID不存在，则服务停止，打印必要日志，并重启服务
        time=$(date "+%Y-%m-%d %H:%M:%S")
        if [ "${pid}" -eq 0 ]; then
            echo "${time}:${serverName} is stop!"
            echo "${time}:restart the ${serverName}!"
            startServr
        else
            echo "${time}:${serverName} is running!"
        fi
        # 存活检查频率。这里是每分钟检查一次
        sleep ${cycle}
    done
}


#######################################
# 函数的作用是: 停止一个服务
# Globals:
#   无全局参数说明
# Arguments:
#   需要传入一个要停止的服务名
#   核心是 ps -ef | grep 'serverName' | grep -v grep | awk '{print $2}'
# Returns:
#   返回值为空
#######################################
function stopServer() {
    pid=$(ps -ef | grep $1 | grep -v grep | awk '{print $2}')
    if [ -z ${pid} ]; then
        echo "$1 服务未运行!"
    else
        echo "$1 进程号 ${pid} 停止运行!"
        $(kill -9 ${pid})
    fi
}

main() {
    echo "script start!"
    checkServer
    exit 0
}
main "$@"
