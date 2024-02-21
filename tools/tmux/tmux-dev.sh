#!/bin/env bash

###########################################################
# @file : tmux-dev.sh
# @desc : 脚本执行方式 [bash tmux-dev.sh]
#         脚本说明: 创建一个开发的 tmux 环境
# @date : 2024-02-21 11:09:35
# @auth : test
# @version : 1.0
###########################################################

# 项目名
NAME=dev
# 项目目录
PROJECT_PATH=~/dev
# 判断是否已经创建
tmux has-session -t ${NAME}
if [ $? != 0 ]; then
	tmux new-session -s ${NAME} -n code -d
	tmux new-window -n database -t ${NAME}
	tmux new-window -n log -t ${NAME}
	tmux new-window -n test -t ${NAME}
	tmux send-keys -t ${NAME}:code "cd ${PROJECT_PATH}; echo '执行打开项目命令 如: code . vim 等' " C-m
	tmux send-keys -t ${NAME}:database "cd ${PROJECT_PATH}; echo '执行数据库连接命令'" C-m
	tmux send-keys -t ${NAME}:log "cd ${PROJECT_PATH}; echo '执行日志查看命令'" C-m
	tmux send-keys -t ${NAME}:test "cd ${PROJECT_PATH}; echo '执行测试命令' " C-m
	tmux select-window -t development:code
fi
tmux a -t ${NAME}