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

mkdir -p "${PROJECT_PATH}"

# 判断是否已经创建tmux会话
if tmux has-session -t "${NAME}"; then
    echo "Tmux session ${NAME} already exists."
else
    # 创建 tmux 会话
    tmux new-session -s "${NAME}" -n default -d
fi

# 创建 tmux 中的窗口并执行命令
# 参数1: window_name 窗口名
# 参数2: command 要执行的命令
function create_window() {
    local window_name=$1
    local command=$2
    # 创建窗口
    tmux new-window -n "${window_name}" -t "${NAME}" -c "${PROJECT_PATH}"
    # 在窗口中执行命令
    tmux send-keys -t "${NAME}:${window_name}" "${command}" C-m
}

# 分屏
# 参数1: window_name 窗口名
function split_pane() {
    local window_name=$1
    # 左右分屏
    # tmux split-window -h -t "${NAME}:${window_name}"
    # 上下分屏
    tmux split-window -v -t "${NAME}:${window_name}"
}

# 创建窗口并执行命令
create_window code "echo '执行打开项目命令 如: code . 或 vim .'"
split_pane code
create_window database "echo '执行数据库连接命令'"
create_window log "echo '执行日志查看命令'"
create_window test "echo '执行测试命令'"

# 选择项目代码所在的窗口
tmux select-window -t "${NAME}:code"

# 连接到tmux会话
tmux attach -t "${NAME}"
