# 主从表数据量校验

```sh

#!/usr/bin/bash 

#配置日志文件位置
logfile=/root/zhucong/
#配置日志文件名
logname=mysql_sum.log
#日志文件路径整合
log=$logfile/$logname

#主库配置
masterurl=
masteruser=
masterpw=

#从库配置
slaveurl=
slaveuser=
slavepw=



if  [ $# -eq 1 ];then
	echo ""	 
else
	echo "参数1:来源数据表文件"
	exit
fi

function diff(){
    #来源库表
    fromdb=boyi_data
    fromtable=$1
    #目标库表
    echo $1
    mastersql="select count(1) from "$fromdb"."$fromtable
    slavesql="select count(1) from "$fromdb"."$fromtable
    
    #查询数据
    master=`mysql -h$masterurl -u$masteruser -p$masterpw -e "${mastersql}"`
    slave=`mysql -h$slaveurl -u$slaveuser -p$slavepw -e "${slavesql}"`
    
    #求差值
    echo "表${fromtable} |${master:9}|${slave:9}"   >> $log
    
    ss=$((10#${master:9}-${slave:9}))
    
    if [ $ss -eq 0 ];then
    	#echo "表${fromtable}数据相差${s}"	
    	printf "表名:%50s|%20d|%20d|差额%20d| \n" $fromtable ${master:9} ${slave:9}  $ss
    else
    	printf "表名:%50s|%20d|%20d|差额%20d| \n" $fromtable  ${master:9} ${slave:9} $ss
    	echo "表${fromtable} 数据差额 $ss"   >> $log
    fi

}

for line in `cat $1`
do
	diff $line
done



```