# linux 中文件相关

## 文件查找技巧

### 文件树形化 

- tree

- ranger 像vim一样查看文件列表

### 文件检索方式

- find 

  `find ./ -name '*list*'`
## 文件传输方式 服务器端文件上传方式

### scp 需要 ssh 支持

- scp 需要 ssh 支持

### lrzsz

- windows 下 xshell 支持

- mac 下 需要各种配置

### nc 服务

- nc 通信测试

  服务器端 查看 ip `hostname -i`

  然后启动 nc 服务 `nc -l 8889`

  客户端 先 ping `ping 远程ip`

  然后 nc 连接 `nc host port`

  就建立起双端的沟通信号

- 接收端

  `nc -l port > file`

- 发送端

  `nc ip port < file`

- 快速生成文件传输通道 文件传输

  `echo -e "客户端复制此命令\nfile为要上传的文件\nnc $(hostname -i) 8889 < file" && nc -l 8889 > file`

- 多文件可配合压缩命令

- 示例

  接收端

  `nc -l port | tar -xzvf -C /home/username/filepath`

  发送端

  `tar -czvf - file1 file2 dir1 dir2 | nc ip port`

### python 服务的方式 文件传输下载

- python 自带的 http 服务，在要下载的文件目录内

  执行 `python -m SimpleHTTPServer port` port 可以自己指定

  如 `python -m SimpleHTTPServer 8888`

  然后请求 <http://host:port> 即可访问当前命令所在的文件夹并下载相关内容
