#!/usr/bin
# 给服务器设置环境变量
# 使用 source 命令使当前环境生效
# 配置自己开发的环境变
# 查看系统变量 set

# 设置中文
export LANG=zh_CN.UTF-8

# 当前路径 ${PWD}
# 当前登录用户 ${LOGNAME}
# 更新自己
alias updateenv='source ~/.env.sh'
# alias 不支持参数，function 才支持。
# 以快速运行 "grep --help" 为例, 有了以下alias运行“h grep”就可以了：
alias h='help_fun(){ $@ --help | head -n 5 ;}; help_fun '

alias ll='ls -alh'
alias llg='ls -alh | grep'
# ls命令按文件大小排序
alias ll_sort_size='ls -Slh'
alias ll_sort_size_r='ls -Slrh'

# ls按时间排序
alias ll_sort_time='ls -lth'
alias ll_sort_time_r='ls -lrth'

# Linux 下修改 .bashrc 或者 .profile , ls 日期格式展示修改
export TIME_STYLE='+%Y-%m-%d %H:%M:%S'
# mac 下 安装 brew install coreutils  使用 gls 命令代替 ls
# alias ls="ls -l --time-style '+%Y-%m-%d %H:%M:%S'"
#### 终端 Bash 命令提示符样式 只能在 bash 下设置
SCHEME1="\[\e[01;35m\]\u\[\e[01;31m\]\$\[\e[01;36m\][\W]\[\e[01;35m\] >>\[\e[00m\] "
SCHEME2="\[\e[01;32m\]\u\[\e[01;31m\]\$\[\e[01;36m\][\W]\[\e[01;32m\] =>\[\e[00m\] "
SCHEME3="\[\e[01;36m\][\[\e[01;35m\]\u\[\e[01;31m\]@\[\e[01;35m\]\h \[\e[01;36m\]\W]\[\e[01;35m\]\$\[\e[00m\] "
SCHEME4="\[\e[01;36m\][\[\e[01;32m\]\u\[\e[01;31m\]@\[\e[01;32m\]\h \[\e[01;36m\]\W]\[\e[01;32m\]\$\[\e[00m\] "

# 设置自定义的终端命令提示符样式
# export PS1=$SCHEME4

# 让history在存储时忽略指定指令
export HISTIGNORE="pwd:ls:ll:ls –ltr:history:h1:h2:h3"
# export HISTCONTROL=ignoredups# 使用HISTCONTROL来消除命令历史中的连续重复条目
# export HISTCONTROL=erasedups # 使用HISTCONTROL在整个历史中去除重复命令
# export HISTCONTROL=ignorespace # 使用HISTCONTROL强制history忽略某条特定命令(这里是空格)
export HISTCONTROL=erasedups
# 多个终端同时操作时，避免命令覆盖，采用追加方式
# shopt -s histappend
# 设置历史命令记录数
export HISTSIZE=5000
# 记录历史文件大小 ~/.bash_history 中保存命令的记录总数.
export HISTFILESIZE=5000

# 让 grep 彩色输出
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# sudo 命令 /root/.bashrc 文件不生效的问题
alias sudo='sudo env PATH=$PATH'

# 查看命令位置
alias type="type -a"
alias which="which -a"

# 搜索历史命令
alias hisg="history 1000 | grep $1 | uniq"

# 搜索进程
alias psg="ps aux | grep -v grep | grep"

# 查看文件前5行
alias cat-file='aFun(){ cat $1 | head -n 5 ;}; aFun '

# tailf
alias tailf='tail -f -n 200'

# 指定python执行的编码格式
# python3 乱码问题 编码问题
alias python3='PYTHONIOENCODING=utf-8 python3'

ncFunc() {
    echo -e "客户端复制此命令"
    echo -e "file为要上传的文件"
    echo -e "nc $(hostname -i) 8889 < $1"
    nc -l 8889 >$1
}

# 文件上传服务
alias nc-file='ncFunc '

# 文件下载服务
alias py_httpserver='echo "浏览器打开 http://${HOSTNAME}:8889/" && python3 -m http.server  8889'

# 文件传输 python3
# 60s后关闭,防止忘记关闭
function fileserver {
    host=$(hostname -i)
    port=8889
    now=$(date +"%F %T")
    num=60
    echo "${now}=>服务启动,${num} 秒后结束"
    for file in $(ls); do
        echo "wget -N http://${host}:${port}/${file}"
    done
    $(
        python3 -m http.server ${port} &
        sleep ${num}
        kill $! &
    )
}
alias fileserver=fileserver

# 文件传输 python2
function fileserver2 {
    host=$(hostname -i)
    port=8889
    num=60
    echo "wget -N http://${host}:${port}/$1"
    $(
        python -m SimpleHTTPServer ${port} &
        sleep ${num}
        kill $! &
    )
}
alias fileserver2=fileserver2

# scp / ftp 等其他服务
alias pwdftp='echo "ftp://${HOSTNAME}:${PWD}"'
alias pwdscp='echo "${LOGNAME}@${HOSTNAME}:${PWD}"'
alias pwdscp='echo "${LOGNAME}@$(hostname -i):${PWD}"'

# 查询当前目录下 文件中的某个字符
# ack 命令可替代 查找命令
alias fword='findWord(){ find ./ -type f | xargs grep -n "$1" --color=auto ;}; findWord'

# grep递归查询
alias fword='findWordGrep(){ grep "$1" . -r -n --color=auto ;}; findWordGrep'

# 查询当前目录下 是否有某个文件
# 2>/dev/null  不输出没权限查看的目录
alias ffile='findFile(){ find ./ -type f -iname \*$1\* 2>/dev/null;}; findFile'

# 查询指定文件名的文件是否包含某个字段
# 查询 shell 文件中包含 haed 内容的文件
# fwordfile sh head
alias fwordfile='findWordFromFile(){ find ./ -type f -iname \*$1\* | xargs grep -n --color=auto "$2" ;}; findWordFromFile'

# 以树形结构递归地显示目录结构
alias lsr="ls -R | grep :$ | sed -e 's/:$//' -e 's/[^-][^\/]*\//--/g' -e 's/^/   /' -e 's/-/|/'"

# 获取操作系统位数
alias osbit="getconf LONG_BIT"

#### Python 相关设置
export PYTHONIOENCODING="UTF-8" # 标准流的编码
export PYTHONUNBUFFERED=1       # 不缓冲标准流
# export PYTHONOPTIMIZE=1    # 优化字节码

# 进入目录并列出目录下的文件
cdl() {
    cd "$1"
    ls
}
# 复杂的命令可以先自定义一个函数，然后起别名
alias cdll='cdl'
# 查看进程打开的文件描述符
pfds() { ls -l /proc/$1/fd; }

# 获取所有用户和组
alias alluser="cut -d : -f 1 /etc/passwd | sort | xargs"
alias allgroup="cut -d : -f 1 /etc/group | sort | xargs"
alias bashusers="cat /etc/passwd | grep /bin/bash | cut -d : -f 1 | sort | xargs"
alias loginusers="cat /etc/passwd | grep -v /sbin/nologin | cut -d : -f 1 | sort | xargs"

# 获取占用CPU最高的前十个进程
alias topcpu="ps aux | grep -v PID | sort -nrk +3 | head"
#alias topcpu="ps -aux --sort -pcpu | head"

# 获取占用内存最高的前十个进程
alias topmem="ps aux | grep -v PID | sort -nrk +4 | head"
#alias topmem="ps -aux --sort -pmem | head"

# 监控进程 CPU，MEM 占用，Mac 不兼容
alias watch-ps="watch -d -n1 'ps aux --sort -pmem,-pcpu | head -25'"

# 监控最占用的 CPU 的进程，Mac 兼容
alias watch-cpu="watch -n1 'ps aux | grep -v PID | sort -nrk +3 | head -25'"

# 监控最占用的 MEM 的进程，Mac 兼容
alias watch-mem="watch -d -n1 'ps aux | grep -v PID | sort -nrk +4 | head -25'"

# 文件夹大小排序
alias ll_sort_file="du -sh * |sort -rh"
# 隐藏文件排序
alias ll_sort_file_hidden="du -hl --max-depth=1 |sort -rh"


alias help='tldr -c'
alias help_update='tldr -u'

# echo "配置完成"
# alias

#  查找命令别名
alias aliasg='alias | grep'

# 删除命令
# github https://github.com/andreafrancia/trash-cli 
alias rm='echo " rmr 删除 rml 查看所有删除的文件 rmd 删除几天内的文件 rm删除操作危险,使用trash-put进行删除"'
alias rmr='trash-put'
alias rml='trash-list'
alias rmd='trash-empty '

# 取消别名
# unalias name