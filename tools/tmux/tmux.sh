#!/bin/env bash

###########################################################
# @file : dev.sh
# @desc : 脚本执行方式 [bash dev.sh]
#         脚本说明: 创建 tmux 脚本
# @date : 2023-12-12 10:16:01
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

# 工作目录配置
path="/home/work"
cd ${path}

# tmux session name
name="dev"

# 判断 name 是否存在  
if tmux ls | grep -q ${name}; then  
  # 如果存在，则附加到 dev 会话  
  tmux a -t ${name} 
else  
  # 如果不存在，则创建新的会话并命名为 dev  
  tmux new -s ${name} 
fi