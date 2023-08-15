#!/bin/env bash

###########################################################
# @file : work.sh
# @desc : 脚本执行方式 [bash work.sh]
#         脚本说明:启动 tmux 项目窗口 默认创建一个 tmux 分屏的窗口
# @date : 2023-08-15 09:57:09
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

function create_tmux() {
    name=$1
    echo "创建 [$name] 的 tmux 中 ..."
    # 后台创建会话
    tmux new -s ${name} -d
    # 重命名会话的第一个窗口名称为service
    tmux rename-window -t "${name}:1" service
    # 切换到指定目录并运行命令
    tmux send -t "${name}:service" "cd ~/;ls" Enter

    # 默认上下分屏
    tmux split-window -t "${name}:service"
    # 切换到指定目录并运行命令
    tmux send -t "${name}:service" 'cd ~/;date' Enter

    # 新建一个名称为tool的窗口
    # neww等同于new window
    tmux neww -a -n tool -t ${name}
    # 运行命令测试
    tmux send -t "${name}:tool" "cd ~/;echo 'test'" Enter
    # 水平分屏
    tmux split-window -h -t "${name}:tool"
    # 切换到指定目录并执行命令
    tmux send -t "${name}:tool" "cd ~/;uname" Enter
}

function list_tmux() {
    echo "创建成功，tmux ls 列表如下:"
    tmux ls
}

main() {
    echo "创建一个 tmux session"
    WORKNAME=$1
    echo "创建项目 [${WORKNAME}] 的 session"
    create_tmux ${WORKNAME}
    list_tmux
    exit 0
}
main "$@"
