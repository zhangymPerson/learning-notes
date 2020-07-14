#jar包名
function logs() {
    date=$(date +'%Y-%m-%d %H:%M:%S')
    echo "${date}" $*
}

# 打印日志 调用方式 log info
function log() {
    logs INFO $*
}

jarName=
stop() {
    PID=$(ps -ef | grep $1 | grep -v grep | awk '{ print $2 }')
    if [ -z "$PID" ]; then
        log Application is already stopped (项目未运行)
    else
        log Application stoping...
        echo kill $PID
        kill $PID
        log Application stop success (以关闭项目)
    fi
}
stop ${jarName}
