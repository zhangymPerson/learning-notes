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
