# alias
# 获取host
# host=$(hostname -i)
host=${HOSTNAME}

# 目录
work=/home/work

# nginx和应用的目录
nginx=/home/work/nginx

# 各个语言的目录
java=/home/work/sdk/java

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

# cd类的 cd- 开头
alias cd-work='cd ${work}'
alias cd-nginx='cd ${nginx}'

# tail 类的 tail开头
alias tail-test='tail ${work}/log.log'

# 自定义命令
# mysql mycli 命令的 mysql- 开头
alias mysql-test='mysql -h127.0.0.1 -uroot -p123456'

# 各个语言代码查询
alias greppy="find . -name '*.py' | xargs grep -n --color"
alias grepjava="find . -name '*.java' | xargs grep -n --color"
alias grepphp="find . -name '*.php' | xargs grep -n --color"
alias grepshell="find . -name '*.sh' | xargs grep -n --color"

# git
alias git_config="git config --list"
alias git_alias="git config --list |grep alias"

# kubectl
# 命令网站 - https://kubernetes.io/zh-cn/docs/reference/kubectl/quick-reference/
# source <(kubectl completion bash)
alias kubectl_grep_pod="kubectl get pods | grep "
alias kubectl_delete_pod="kubectl delete pod "
alias kubectl_exec="kubectl exec -it"
alias kubectl_restart_server="kubectl rollout restart"
alias kubectl_log="kubectl logs -f "

# 配置常用的提示信息到 .user_info
alias echo_info="cat ~/.user_info"

# 删除命令
# github https://github.com/andreafrancia/trash-cli
alias rm='echo " rmr 删除 rml 查看所有删除的文件 rmd 删除几天内的文件 rm删除操作危险,使用trash-put进行删除"'
alias rmr='trash-put'
alias rml='trash-list'
alias rmd='trash-empty'
