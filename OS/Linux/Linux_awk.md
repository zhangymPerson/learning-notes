# awk 使用

- [返回](./README.md)
- [AWK 工作原理](http://www.runoob.com/w3cnote/awk-work-principle.html)

常用的 awk 命令

- awk '代码' 文件名

eg: `awk '{print $1}' 文件名 awk 'BEGIN{print "BEGIN"} {print $1} END{print "END"}' /etc/passwd`

-F 参数：指定分隔符，可指定一个或多个

eg

```shell
awk -F":" '{print $1}' /etc/passwd
```

查看指定行的数据 (NR 表示行数)

```sh
awk '{if (NR > 1 && NR < 3) print $1}' /etc/passwd
```

- [awk 实用简单教程](https://www.cnblogs.com/ginvip/p/6352157.html)
