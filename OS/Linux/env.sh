#!/usr/bin
# 给服务器设置环境变量
# 使用 source 命令使当前环境生效
# 配置自己开发的环境变量

# 获取host
host=$(hostname -i)

# 目录
work=/home/work

# nginx和应用的目录
nginx=/home/work/nginx

# 各个语言的目录
java=/home/work/sdk/java

# 自定义命令
# cd类的 cd- 开头
alias cd-work='cd ${work}'
alias cd-nginx='cd ${nginx}'

# tail 类的 tail开头
alias tail-test='tail ${work}/log.log'

# mysql mycli 命令的 mysql- 开头
alias mysql-test='mysql -h127.0.0.1 -uroot -p123456'

# 文件上传服务
alias nc-file='echo -e "客户端复制此命令\nfile为要上传的文件\nnc ${host} 8889 < file" && nc -l 8889 > file'

# 文件下载服务
alias download-file='echo "浏览器打开 http://${host}:8889/" && python3 -m http.server  8889'

# scp 等其他服务
alias scp-file='scp file work@127.0.0.1:/home/work'

echo "配置完成"
# alias

# 取消别名
# unalias name