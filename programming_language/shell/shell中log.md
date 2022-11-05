# shell 中的日志

[返回](./README.md)

- 简单

```sh
#!/bin/bash
#########################################
#日志显示
#########################################
echo $0" begining ..."

# 日志函数
# 日志输出到文件
log(){
    #echo "参数个数:"$#
    #配置文件位置和文件名
    filePath=/root/
    fileName=test.log
    #日期格式 可修改
    date=`date +"%Y-%m-%d %H:%M:%S"`
    if [ $# -eq 1 ];then
    echo [$date]"[INFO]:脚本"$0"中:"$1 >> $filePath$fileName
    return
    fi
    echo [$date][$1]":脚本"$0"中:"$2 >> $filePath$fileName
}

#调用方式
log INFO info-message
log info-message
log ERROR error-message
log WARN warning-message

# 调用结果
#[18-12-27 16:50-04][INFO]:脚本log.sh中:info-message
#[18-12-27 16:50-04][INFO]:脚本log.sh中:info-message
#[18-12-27 16:50-04][ERROR]:脚本log.sh中:error-message
#[18-12-27 16:50-04][WARN]:脚本log.sh中:warning-message
```

- 错误日志输出

```shell
err() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2
}

if ! do_something; then
    err "Unable to do_something"
    exit "${E_DID_NOTHING}"
fi
```
