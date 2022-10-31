#!/bin/env bash

###########################################################
# @file : check_file.sh
# @desc : 脚本执行方式 [bash check_file.sh]
#         脚本说明: 判断文件是否存在
# @date : 2022-07-05 10:13:54
# @auth : test
# @version : 1.0
###########################################################

# set -o xtrace debug模式需开启
# set -x

# set -o errexit 有错误退出
set -e
# 输出脚本中相关内容 到脚本文件名对应的log文件中
# debug时 可以开启
# exec >>${0}.log

# 判断文件或目录是否存在
if [ $# -eq 0 ]; then
    echo "未输入任何参数,请输入参数"
    echo "用法:$0 [文件名|目录名]"
fi
if [ -f "$1" ]; then
    echo "该文件,存在"
    ls -l "$1"
else
    echo "没有[$1]文件"
fi
if [ -d "$1" ]; then
    echo "该目录,存在"
    ls -ld "$2"
else
    echo "没有[$1]目录"
fi
