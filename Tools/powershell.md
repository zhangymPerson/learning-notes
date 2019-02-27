# powershell常用命令

- 查看端口占用

    netstat -nao

- 查看进程 

    ps (cmd不行)
    
    使用最多的内存查找五个进程： 
    ps | sort –p ws | select –last 5

- 与cmd互相交互

    在cmd之中直接 powershell 
    在powershell中直接cmd即可互相交互

- 命令帮助

    get-help

    get-help 命令 //获取命令

    //获取命令的别名
    Get-Alias 

- powershell 查看环境变量

    $env:path

