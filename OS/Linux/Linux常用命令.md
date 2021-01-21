# 不打开文件追加配置

- [返回](./README.md)

```sh
# 查看环境变量的命令
printenv

# 文件类型 查看命令
file filename

# cat 使用行号
cat -n filename

# cat 不使用行号
cat -b filename

# less命令
less filename

# f 向后翻页
# b 向前翻页
# j 向下一行
# k 向上一行
# -N  + enter键 显示行数/不现实行数

# sort 命令
# 默认按字母顺序排序
# 默认数字是按开头的数字排序
# 不指定数字的排序 1 11 11 2 21 22 ...
sort filename

#数字按大小排序，需要使用 -n

# shell中命令别名

#查看命令别名
alias -p

#自定义别名 不能有空格
# 修改只在当前shell窗口中有效
alias li='ls -li'

#新建/覆盖 添加文件内容到文件中
cat > test.log <<EOF
192.168.0.103 master
192.168.0.104 slave1
192.168.0.106 slave3
EOF

#追加信息到文件中
cat >> test.log <<EOF
asfsakfj
asdfk;logassdfd
;lksdjf
asddfklj

EOF
```
