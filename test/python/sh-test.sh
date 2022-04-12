#!/bin/bash

###########################################################
# @file : sh-test.sh
# @desc : 脚本执行方式 [bash sh-test.sh]
#         脚本说明:test
# @date : 2022-04-12 15:15:39
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
# debug时，可以开启
exec >>${0}.log

main() {
    echo "hello world"
    now=$(date +"%F %T")
    echo "script start" ${now}
    exit 0
}
main "$@"
