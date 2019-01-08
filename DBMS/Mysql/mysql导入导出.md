# mysql 自带导入导出命令

- mysql 命令
```sh
#导出sql文件
mysqldump -h$fromurl -u$fromuser -p$frompassword $fromdb $fromtable > $sqlfile
#导入文件
mysql -h$tourl -u$touser -p$topassword $todb < $sqlfile
```

