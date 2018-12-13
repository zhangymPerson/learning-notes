# 简单例子

- 接收参数并且打印
```sh
#!/bin/bash
################################################################
# 测试接收参数的脚本 1
################################################################

echo $0" is begining"

# 循环判断参数是否存在
# -n是判断是否有参数，参数是否为空， $1 需要加"" ,
while [ -n "$1" ]
do
    case "$1" in
        -a) echo "Found the -a option" ;;
        -b) echo "Found the -b option" ;;
        -c) echo "Found the -c option" ;;
        *) echo "$1 is not an option" ;;
    esac
    shift
done

echo $0" is end"
```

### 关键函数介绍

- getopt
```sh
Usage:
 getopt <optstring> <parameters>
 getopt [options] [--] <optstring> <parameters>
 getopt [options] -o|--options <optstring> [options] [--] <parameters>

Parse command options.

Options:
 -a, --alternative             allow long options starting with single -
 -l, --longoptions <longopts>  the long options to be recognized
 -n, --name <progname>         the name under which errors are reported
 -o, --options <optstring>     the short options to be recognized
 -q, --quiet                   disable error reporting by getopt(3)
 -Q, --quiet-output            no normal output
 -s, --shell <shell>           set quoting conventions to those of <shell>
 -T, --test                    test for getopt(1) version
 -u, --unquoted                do not quote the output

 -h, --help     display this help and exit
 -V, --version  output version information and exit

For more details see getopt(1).
```
- 完整的参数脚本demo

```sh

#!/bin/bash
################################################################################################################################################
# 脚本主要用来编写带参数的脚本
#使用到 getopt函数  getopt --help(获取帮助)
#-o或--options选项后面接可接受的短选项，如ab:c::，表示可接受的短选项为-a -b -c，其中-a选项不接参数，-b选项后必须接参数，-c选项的参数为可选的
#其中可选值在传值时注意: -c test 不能传入值， 需写成-ctest ;--arg3 test不行，需写成 --arg3=test
#-l或--long选项后面接可接受的长选项，用逗号分开，冒号的意义同短选项。
#-n选项后接选项解析错误时提示的脚本名字
#shift 表示参数右移
################################################################################################################################################

#自定义版本号
VERSION=0.1
#处理参数对 
ARGS=`getopt -o hva:b:c:: --long help,version,arg1:,arg2:,arg3:: -n $0 -- "$@"`

#初步校验参数的合法性
if [ $? != 0 ]; then
    echo "Terminating..."
    exit 1
fi
 
#echo $ARGS
#将规范化后的命令行参数分配至位置参数（$1,$2,...)
eval set -- "${ARGS}"

#解析参数 
# 如 -h -v 
while true
do
    case "$1" in
        -h|--help) 
            echo "$0的作用是:";
			echo "   能接收的参数有: -a | --arg1";
			echo "   能接收的参数有: -b | --arg2";
			echo "   能接收的参数有: -c | --arg3";
            shift
            ;;
        -v|--version)
            echo "$0的版本是:" $VERSION;
            shift
            ;;
	-a|--arg1)
            echo "参数$1的值是:" $2;
            shift 2
            ;;
	-b|--arg2)
            echo "参数$1的值是:" $2;
            shift 2
            ;;
        -c|--arg3)
            case "$2" in
                "")
                    echo "参数$1的为空";
                    shift 2  
                    ;;
                *)
                    echo "Option c, argument $2";
                    shift 2;
                    ;;
            esac
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "Internal error!"
            exit 1
            ;;
    esac
done
 
#处理剩余的参数(不带斜杠的参数)
for arg in $@
do
    echo "processing $arg"
done



```



