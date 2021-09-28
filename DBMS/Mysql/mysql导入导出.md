# mysql 自带导入导出命令

- mysql 命令

  ```sh
  # 导出整个数据库结构和数据
  mysqldump -h localhost -uroot -p123456 database > dump.sql

  # 导出单个数据表结构和数据
  mysqldump -h localhost -uroot -p123456  database table > dump.sql

  # 导出整个数据库结构（不包含数据）
  # --default-character-set=utf8 防止导出乱码
  mysqldump -h localhost -uroot -p123456  -d database --default-character-set=utf8> dump.sql

  # 导出单个数据表结构（不包含数据）
  mysqldump -h localhost -uroot -p123456  -d database table > dump.sql

  #导出单表的sql文件
  mysqldump -h$fromurl -u$fromuser -p$frompassword $fromdb $fromtable > $sqlfile
  #导入单表文件
  mysql -h$tourl -u$touser -p$topassword $todb < $sqlfile
  ```

## mysql8.0 中错误

- 错误提示

  mysqldump: Couldn't execute 'SELECT COLUMN_NAME, JSON_EXTRACT(HISTOGRAM, '$."number-of-buckets-specified"') FROM information_schema.COLUMN_STATISTICS

  解决办法:

  ```sql
  mysqldump --skip-column-statistics   -h x.x.x.x -u root -p dbname > db.sql;
  ```
