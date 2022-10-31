# 清理主从日志

- 查看自动清理日志时间

  show variables like 'expire_logs_days';

- 删除指定日期以前的日志索引中 binlog 日志文件

  purge master logs before'2016-09-01 17:20:00';

- 删除指定日志文件的日志索引中 binlog 日志文件

  purge master logs to'mysql-bin.000022';

- **注意**：

  时间和文件名一定不可以写错，尤其是时间中的年和文件名中的序号，以防不小心将正在使用的 binlog 删除！！！

  切勿删除正在使用的 binlog！！！

  mysql> show variables like 'expire_logs_days';
  +------------------+-------+
  | Variable_name | Value |
  +------------------+-------+
  | expire_logs_days | 0 |
  +------------------+-------+

- 设置 不需要重启 需要在数据库中设置 3 天/7 天/30 天 看情况配置

  mysql> set global expire_logs_days = 30; #设置 binlog 多少天过期

- 清除指定天数之前的日志

  PURGE MASTER LOGS BEFORE DATE_SUB(CURRENT_DATE, INTERVAL 5 DAY);
