# 不打开文件追加配置


```sh
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