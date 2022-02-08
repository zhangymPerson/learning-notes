#!/usr/bin
# 给服务器设置环境变量
# 使用 source 命令使当前环境生效
# 配置自己开发的环境变量

# 查看系统变量 set

# 当前路径 ${PWD}
# 当前登录用户 ${LOGNAME}

# alias 不支持参数，function 才支持。
# 以快速运行 "grep --help" 为例, 有了以下alias运行“h grep”就可以了：
alias h='help_fun(){ $@ --help | head -n 5 ;}; help_fun '

# 查看文件前5行
alias cat-file='aFun(){ cat $1 | head -n 5 ;}; aFun '

# 获取host
host=$(hostname -i)

# 目录
work=/home/work

# nginx和应用的目录
nginx=/home/work/nginx

# 各个语言的目录
java=/home/work/sdk/java

# 自定义命令

# 指定python执行的编码格式
# python3 乱码问题 编码问题
alias python3='PYTHONIOENCODING=utf-8 python3'

# cd类的 cd- 开头
alias cd-work='cd ${work}'
alias cd-nginx='cd ${nginx}'

# tail 类的 tail开头
alias tail-test='tail ${work}/log.log'

# mysql mycli 命令的 mysql- 开头
alias mysql-test='mysql -h127.0.0.1 -uroot -p123456'

# 文件上传服务
alias nc-file='ncFunc(){ echo -e "客户端复制此命令 \nfile为要上传的文件 \nnc ${host} 8889 < $1" && nc -l 8889 > $1 ;}; ncFunc '

# 文件下载服务
alias download-file='echo "浏览器打开 http://${HOSTNAME}:8889/" && python3 -m http.server  8889'

# scp / ftp 等其他服务
alias pwdftp='echo "ftp://${HOSTNAME}:${PWD}"'
alias pwdscp='echo "${LOGNAME}@${HOSTNAME}:${PWD}"'
alias pwdscp='echo "${LOGNAME}@$(hostname -i):${PWD}"'

# 查询当前目录下 文件中的某个字符
alias fword='findWord(){ find ./ -type f | xargs grep -n "$1" --color=auto ;}; findWord'

# grep递归查询
alias fwordgrep='findWordGrep(){ grep "$1" . -r -n --color=auto ;}; findWordGrep'

# 查询当前目录下 是否有某个文件
alias ffile='findFile(){ find ./ -type f -iname \*$1\* ;}; findFile'

# 查询指定文件名的文件是否包含某个字段
# 查询 shell 文件中包含 haed 内容的文件
# fwordfile sh head
alias fwordfile='findWordFromFile(){ find ./ -type f -iname \*$1\* | xargs grep -n --color=auto "$2" ;}; findWordFromFile'

echo "配置完成"
# alias

# 取消别名
# unalias name
