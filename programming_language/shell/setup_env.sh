#!/bin/bash
# user: danao
# date: 2021-08-27
# 作用: demo script

# debug模式需开启
# set -x # set -o xtrace

set -e          # set -o errexit 有错误退出
set -u          # set -o nounset
set -o pipefail #管道执行过程中有错误退出

# 专门设置要用到的环境变量
LOCAL_ARCH=$(uname -m)
export LOCAL_ARCH
