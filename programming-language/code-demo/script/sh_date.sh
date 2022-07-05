#!/bin/env bash

###########################################################
# @file : sh_date.sh
# @desc : 脚本执行方式 [bash sh_date.sh]
#         脚本说明: 日期格式
# @date : 2022-07-05 10:18:20
# @auth : test
# @version : 1.0
###########################################################

# set -o xtrace debug模式需开启
# set -x

# set -o errexit 有错误退出
set -e
# set -o nounset
set -u
#管道执行过程中有错误退出
set -o pipefail
# 输出脚本中相关内容 到脚本文件名对应的log文件中
# debug时 可以开启
# exec >>${0}.log

# 打印各种时间格式
echo "显示星期简称(如:Sun)"
date +%a
echo "显示星期全称(如:Sunday)"
date +%A
echo "显示月份简称(如:Jan)"
date +%b
echo "显示月份全称(如:January)"
date +%B
echo "显示数字月份(如:12)"
date +%m
echo "显示数字日期(如:01 号)"
date +%d
echo "显示数字年(如:01 号)"
date +%Y echo "显示年‐月‐日"
date +%F
echo "显示小时(24 小时制)"
date +%H
echo "显示分钟(00..59)"
date +%M
echo "显示秒"
date +%S
echo "显示纳秒"
date +%N
echo "组合显示"
date +"%Y%m%d %H:%M:%S"
