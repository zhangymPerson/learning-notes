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
# set -e
# set -o nounset
# set -u
# 管道执行过程中有错误退出
# set -o pipefail
# 输出脚本中相关内容 到脚本文件名对应的log文件中
# debug时 可以开启
# exec >>${0}.log

#######################################
# 函数的作用是: 后台创建一个 tmux 聊天
# Globals:
#   无全局参数说明
# Arguments:
#   name 创建的 session name
# Returns:
#   返回值为空
#######################################
function create_session() {
    session_name=$1
    close_session ${session_name}
    echo "# 创建 [${session_name}] 的 tmux 中 ..."
    echo "tmux new -s ${session_name} -d"
    # 后台创建会话
    tmux new -s ${session_name} -d
    echo ""
}

function close_session() {
    session_name=$1
    echo "# 关闭 tmux 中的 session[${session_name}]"
    echo "tmux kill-session -t ${session_name}"
    tmux kill-session -t ${session_name}
    echo ""
}

function create_window() {
    session_name=$1
    window_name=$2
    echo "# 创建 session[${session_name}] 窗口名[${window_name}]"
    echo "tmux neww -n ${window_name} -t ${session_name}"
    tmux neww -n ${window_name} -t ${session_name}
    echo ""
}

function split_window() {
    session_name=$1
    window_name=$2
    echo "# session[${session_name}] 窗口名[${window_name}] 上下分屏"
    echo "tmux split-window -t ${session_name}:${window_name}"
    tmux split-window -t ${session_name}:${window_name}
    echo ""
}

function split_window_h() {
    session_name=$1
    window_name=$2
    echo "# session[${session_name}] 窗口名[${window_name}] 左右分屏"
    echo "tmux split-window -h -t ${session_name}:${window_name}"
    tmux split-window -h -t ${session_name}:${window_name}
    echo ""
}

function exec_command() {
    session_name=$1
    window_name=$2
    command=$3
    split_window ${session_name} ${window_name}
    echo "# session[${session_name}] 窗口名[${window_name}] 执行[${command}]"
    echo "tmux send -t ${session_name}:${window_name} \"${command}\" Enter"
    tmux send -t ${session_name}:${window_name} "${command}" Enter
    echo ""
}

function list_tmux() {
    echo "创建成功，tmux ls 列表如下:"
    tmux ls
    echo "使用 [tmux a -t $1]"
}

function exec_test() {
    # 传入一个 session 名称 创建
    session_name=$1
    create_session ${session_name}
    window_name="tool"
    create_window ${session_name} ${window_name}

    command="cd ~"
    exec_command ${session_name} ${window_name} ${command}
    exec_command ${session_name} ${window_name} "ls -al"

    window_name="info"
    create_window ${session_name} ${window_name}
    command="cd ~"
    exec_command ${session_name} ${window_name} ${command}
    exec_command ${session_name} ${window_name} "cd~;echo -e "test""

    window_name="dev"
    create_window ${session_name} ${window_name}
    command="cd ~"
    exec_command ${session_name} ${window_name} ${command}
    exec_command ${session_name} ${window_name} 'cd /;echo -e "hello world"'
}

main() {
    exec_test $1
    list_tmux $1
    exit 0
}
main "$@"
