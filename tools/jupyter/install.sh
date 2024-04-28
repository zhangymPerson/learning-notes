#!/bin/env bash

###########################################################
# @file : install.sh
# @desc : 脚本执行方式 [bash install.sh]
#         脚本说明:
# @date : 2024-04-28 18:31:19
# @auth : test
# @version : 1.0
###########################################################

# 安装 jupyter
pip install jupyter

# 查看 jupyter 版本
jupyter --version

# 启动 jupyter
jupyter notebook
