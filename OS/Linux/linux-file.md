# linux 中文件相关

## 文件传输方式 服务器端文件上传方式

### scp 需要 ssh 支持

- scp 需要 ssh 支持

### lrzsz

- windows 下 xshell 支持

- mac 下 需要各种配置

### nc 服务

- 接收端

  `nc -l port > file`

- 发送端

  `nc ip port < file`

- 多文件可配合压缩命令

- 示例

  接收端

  `nc -l port | tar -xzvf -C /home/username/filepath`

  发送端

  `tar -czvf - file1 file2 dir1 dir2 | nc ip port`
