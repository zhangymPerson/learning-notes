# mysql主从监控脚本

```sh
#!/usr/bin/bash
#################################################################
#监控主从的脚本
#创建专门的监控用户
#在从服务器上启动
#################################################################



url=127.0.0.1
user=
passwd=

sql="show slave status\G"

keyword="Seconds_Behind_Master"

date=`date +"%Y-%m-%d %H:%M:%S" `

times=`mysql -h$url -u$user -p$passwd -e "${sql}"|grep $keyword` 


filepath=/root/shell/mysql-cong.log

while true

do
        date=`date +"%Y-%m-%d %H:%M:%S" `
        times=`mysql -h$url -u$user -p$passwd -e "${sql}"|grep $keyword`
        time=${times:30}
        if [$time == "0" ];then
                sleep 10
                continue
        else
        	if [[ $time == "NULL" ]]; then
        		echo $date : `mysql -h$url -u$user -p$passwd -e "select * from performance_schema.replication_applier_status_by_worker;"` >> ${filepath}
                	break
            	else
			if [ $time -lt 60  ];then
				echo "延迟小于 1 min"
			else
				echo "延时大于 1min "
            			echo $date : `mysql -h$url -u$user -p$passwd -e "${sql}"|grep $keyword` >> ${filepath}
			fi
			sleep 60
            fi
        fi
done

echo $date : `mysql -h$url -u$user -p$passwd -e "${sql}"|grep $keyword` >> ${filepath}

```
