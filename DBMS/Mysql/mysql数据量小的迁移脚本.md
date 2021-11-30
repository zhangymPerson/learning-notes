# 数据量小的迁移脚本

- 数据文件迁移

```sh
#!/usr/bin/bash

echo $0“脚本开始”

#来源库配置
fromurl=
fromuser=
frompassword=
#目标库配置
tourl=
touser=
topassword=

#迁移数据库
fromdb=
#迁移后数据库
todb=

tablefile=""

#日志文件位置
logfile=/var/log/
#日志文件名
logname=mysql-qianyi.log
log=$logfile/$logname

if [ $# -eq 1 ]; then
    echo "导出的表名文件为："$1
    tablefile=$1
else
    echo "需要一个参数，指定表文件位置"
    exit
fi

function transport() {
    if [ $# -eq 3 ]; then
        echo ""
    else
        echo "参数必须为为3个"
        echo "参数1:来源数据库"
        echo "参数2:来源数据表"
        echo "参数3:目标数据库(自动创建同名数据表)"
        exit
    fi
    fromdb=$1
    fromtable=$2
    todb=$3
    echo "导出的表名为:"$1
    sqlfile=/data/tmp/${fromdb}_${fromtable}.sql
    echo "导出的文件位置："$sqlfile

    onedate=$(date +"%Y-%m-%d %H-%M-%S")
    echo "${onedate} $0 begin" >>${log}
    #导出sql文件
    mysqldump -h$fromurl -u$fromuser -p$frompassword $fromdb $fromtable >$sqlfile

    if [ -f $sqlfile ]; then
        echo $formtable".sql是一个文件"
    else
        echo $fromtable".sql不是一个文件"
        exit
    fi

    #导入文件
    mysql -h$tourl -u$touser -p$topassword $todb <$sqlfile

    if [ $? -eq 0 ]; then
        #如需保存导出数据文件，将下面注释掉
        rm -rf $sqlfile
        echo "${sqlfile} 表迁移成功" >>${log}
        twodate=$(date +"%Y-%m-%d %H-%M-%S")
        echo "${twodate} $0 end" >>${log}
        exit
    else
        echo "${sqlfile} 表迁移失败" >>${log}
        twodate=date +"%Y-%m-%d %H-%M-%S"
        echo "${twodate} $0 error" >>${log}
        exit

    fi

}
# 调用迁移
for line in $(cat $tablefile); do
    transport $fromdb $line $todb
done

```
