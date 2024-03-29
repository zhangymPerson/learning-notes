#!/bin/env bash

###########################################################
# @file : file_md5.sh
# @desc : 脚本执行方式 [bash file_md5.sh]
#         脚本说明: 统计文件夹下的文件md5
# @date : 2022-07-05 10:39:47
# @auth : test
# @version : 1.0
###########################################################

# 输出脚本中相关内容 到脚本文件名对应的log文件中
# debug时 可以开启
# exec >>${0}.log

# 根据 md5 校验码,检测文件是否被修改
# 本示例脚本检测的是/etc 目录下所有的 conf 结尾的文件,根据实际情况,您可以修改为其他目录或文件
# 本脚本在目标数据没有被修改时执行一次,当怀疑数据被人篡改,再执行一次
# 将两次执行的结果做对比,MD5 码发生改变的文件,就是被人篡改的文件
path=$1
logFile=md5.info
for i in $(ls $1); do
    md5sum "$i" >>"${logFile}"
done
