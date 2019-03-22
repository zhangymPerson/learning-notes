# shell 读取输入

- shell获取脚本名

    ```sh
    #!/bin/bash      
    #脚本名 调用方式不一样,名称不一样
    #  $0  表示脚本名

    echo "脚本名练习"
    #脚本名和启动命令相关 可能是全路径 ./*.sh *.sh
    echo "脚本名:"$0

    # 不管怎么启动，脚本名为 *.sh
    name=$(basename $0)
    echo "脚本名:"$name

    #去掉以.sh 结尾的内容
    echo "脚本名:"${name%.sh}
    ```

- 含义介绍

    ```sh
    # $0	当前脚本的文件名
    # $n	传递给脚本或函数的参数。n 是一个数字，表示第几个参数。例如，第一个参数是$1，第二个参数是$2。
    # $#	传递给脚本或函数的参数个数。
    # $*	传递给脚本或函数的所有参数。
    # $@	传递给脚本或函数的所有参数。被双引号(" ")包含时，与 $* 稍有不同，下面将会讲到。
    # $?	上个命令的退出状态，或函数的返回值。
    # $$	当前Shell进程ID。对于 Shell 脚本，就是这些脚本所在的进程ID
    ```
    [测试地址](https://github.com/zhangymPerson/Script_Test/blob/master/Shell/base/special-var.sh)


- 直接读取

    ```sh
    sh test.sh a bc def

    #代表第一个参数
    $1 
    #代表第n个参数
    #整个参数组
    $*   =   a bc def
    ```

- 用户输入参数

    ```sh
    #使用read
    echo "请您输入参数:"
    read var1
    echo "您输入的是" $var1
    ```

