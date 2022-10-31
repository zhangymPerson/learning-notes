#!/bin/env bash

###########################################################
# @file : deploy.sh
# @desc : 脚本执行方式 [bash deploy.sh]
#         脚本说明: 部署自定义的env
# @date : 2022-07-11 16:25:00
# @auth : test
# @version : 1.0
###########################################################

# 部署到 home 目录下
cp dev.sh ~/.dev.sh
cp env.sh ~/.env.sh

# 只执行一次
# echo "source ~/.env.sh" >> ~/.bash_profile
# echo "source ~/.dev.sh" >> ~/.bash_profile

source ~/.bash_profile
