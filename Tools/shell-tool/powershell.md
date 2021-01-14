# powershell 常用命令

- [返回](./README.md)
- 查看端口占用

  `netstat -nao`

- 查看进程

  `ps` (cmd 不行)

  使用最多的内存查找五个进程： `ps | sort –p ws | select –last 5`

- 与 cmd 互相交互

  在 cmd 之中直接 powershell 在 powershell 中直接 cmd 即可互相交互

- 命令帮助

  `get-help`

  `get-help` 命令 //获取命令

  //获取命令的别名 Get-Alias

- powershell 查看环境变量

  `$env:path`
