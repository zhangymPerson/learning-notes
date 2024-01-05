#!/bin/env bash

###########################################################
# @file : bash_pg.sh
# @desc : 脚本执行方式 [bash bash_pg.sh]
#         脚本说明: pgsql 导入导出脚本
# @date : 2023-12-28 17:44:33
# @auth : test
# @version : 1.0
###########################################################

# set -o xtrace debug模式需开启
# set -x

# set -o errexit 有错误退出
set -e
# set -o nounset
set -u
# 管道执行过程中有错误退出
set -o pipefail
# 输出脚本中相关内容 到脚本文件名对应的log文件中
# debug时 可以开启
# exec >>${0}.log

USER=username
DATABASE=database
HOST=localhost
PORT=5432
BACKUP=backup.sql

# 指定密码，不需要输入
export PASSWORD=123456

# 只导出表结构
echo "只导出表结构"
echo "pg_dump -U ${USER} -h ${HOST} -d ${DATABASE} -p ${PORT} -s -f ${BACKUP}"

# 只导出表数据
echo "只导出表数据"
echo "pg_dump -U ${USER} -h ${HOST} -d ${DATABASE} -p ${PORT} --data-only -f ${BACKUP}"
