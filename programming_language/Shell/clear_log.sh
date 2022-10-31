#!/bin/bash

# 清理日志
logPath=/home/work/log
for file in $(find ${logPath} -name "*.log"); do
    #第一种 不删除，清空文件
    cat /dev/null >${file}
    #删除文件
    # rm ${file}
    #删除成功
    echo "日志[${file}]清理成功!"
done
