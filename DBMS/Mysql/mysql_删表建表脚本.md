# mysql 删除表 建表 语句生成的脚本

```sql

#!/usr/bin/bash
# 先保留建表语句，在删除 在建表
url=127.0.0.1
user=root
pw=

#文件夹需提前建立
filepath=/data/tmp/
sqlfile=drop_create.sql

if [ $# -eq 1 ];then
        tablefile=$1
else
        echo "需要表文件参数"
        exit
fi


#将删除表与建表语句写入sql文件
showCreate(){
    db=$1
    table=$2
    sql='show create table '$db.$table
    echo $sql  
    echo "drop table if exists "$db.$table";" >> $filepath$sqlfile
    echo `mysql -u$user -p$pw -e"${sql}"` ";" >  $filepath$db.$table".sql"
    awk '{$1 = "";$2="";$3="";$4="";print}' $filepath$db.$table".sql" | sed 's/\\n/ /g'  >> $filepath$sqlfile
}

echo "" > $filepath$sqlfile
for line in `cat $tablefile`
do
        showCreate boyi_data $line
done

```