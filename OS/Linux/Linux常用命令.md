# linux 的常用命令

- [返回](./README.md)

## 关机/重启/注销

| 常用命令          | 作用                      |
| ----------------- | ------------------------- |
| shutdown -h now   | 即刻关机                  |
| shutdown -h 10    | 10 分钟后关机             |
| shutdown -h 11:00 | 11：00 关机               |
| shutdown -h +10   | 预定时间关机（10 分钟后） |
| shutdown -c       | 取消指定时间关机          |
| shutdown -r now   | 重启                      |
| shutdown -r 10    | 10 分钟之后重启           |
| shutdown -r 11:00 | 定时重启                  |
| reboot            | 重启                      |
| init 6            | 重启                      |
| init 0            | ⽴刻关机                  |
| telinit 0         | 关机                      |
| poweroff          | ⽴刻关机                  |
| halt              | 关机                      |
| sync              | buff 数据同步到磁盘       |
| logout            | 退出登录 Shell            |

## 系统信息和性能查看

| 常用命令                    | 作用                                    |
| --------------------------- | --------------------------------------- |
| uname -a                    | 查看内核/OS/CPU 信息                    |
| uname -r                    | 查看内核版本                            |
| uname -m                    | 查看处理器架构                          |
| arch                        | 查看处理器架构                          |
| hostname                    | 查看计算机名                            |
| who                         | 显示当前登录系统的⽤户                  |
| who am i                    | 显示登录时的⽤户名                      |
| whoami                      | 显示当前⽤户名                          |
| cat /proc/version           | 查看 linux 版本信息                     |
| cat /proc/cpuinfo           | 查看 CPU 信息                           |
| cat /proc/interrupts        | 查看中断                                |
| cat /proc/loadavg           | 查看系统负载                            |
| uptime                      | 查看系统运⾏时间、⽤户数、负载          |
| env                         | 查看系统的环境变量                      |
| lsusb -tv                   | 查看系统 USB 设备信息                   |
| lspci -tv                   | 查看系统 PCI 设备信息                   |
| lsmod                       | 查看已加载的系统模块                    |
| grep MemTotal /proc/meminfo | 查看内存总量                            |
| grep MemFree /proc/meminfo  | 查看空闲内存量                          |
| free -m                     | 查看内存⽤量和交换区⽤量                |
| date                        | 显示系统⽇期时间                        |
| cal 2021                    | 显示 2021 ⽇历表                        |
| top                         | 动态显示 cpu/内存/进程等情况            |
| vmstat 1 20                 | 每 1 秒采⼀次系统状态，采 20 次         |
| iostat                      | 查看 io 读写/cpu 使⽤情况               |
| 查看 io 读写/cpu 使⽤情况   | 查询 cpu 使⽤情况（1 秒⼀次，共 10 次） |
| sar -d 1 10                 | 查询磁盘性能                            |

## 磁盘和分区

| 常用命令                            | 作用                            |
| ----------------------------------- | ------------------------------- |
| fdisk -l                            | 查看所有磁盘分区                |
| swapon -s                           | 查看所有交换分区                |
| df -h                               | 查看磁盘使⽤情况及挂载点        |
| df -hl                              | 同上                            |
| du -sh /dir                         | 查看指定某个⽬录的⼤⼩          |
| du -sk \* \| sort -rn               | 从⾼到低依次显示⽂件和⽬录⼤⼩  |
| mount /dev/hda2 /mnt/hda2           | 挂载 hda2 盘                    |
| mount -t ntfs /dev/sdc1 /mnt/usbhd1 | 指定⽂件系统类型挂载（如 ntfs） |
| mount -o loop xxx.iso /mnt/cdrom    | 挂 载 iso ⽂ 件                 |
| umount -v /dev/sda1                 | 通过设备名卸载                  |
| umount -v /mnt/mymnt                | 通过挂载点卸载                  |
| fuser -km /mnt/hda1                 | 强制卸载(慎⽤)                  |

## ⽤户和⽤户组

| 常用命令                                              | 作用                                              |
| ----------------------------------------------------- | ------------------------------------------------- |
| useradd codesheep                                     | 创建⽤户                                          |
| userdel -r codesheep                                  | 删除⽤户                                          |
| usermod -g group_name user_name                       | 修改⽤户的组                                      |
| usermod -aG group_name user_name                      | 将⽤户添加到组                                    |
| usermod -s /bin/ksh -d /home/codepig –g dev codesheep | 修改⽤户 codesheep 的登录 Shell、主⽬录以及⽤户组 |
| groups test                                           | 查看 test ⽤户所在的组                            |
| groupadd group_name                                   | 创建⽤户组                                        |
| groupdel group_name                                   | 删除⽤户组                                        |
| groupmod -n new_name old_name                         | 重命名⽤户组                                      |
| su - user_name                                        | su - user_name                                    |
| passwd                                                | 修改⼝令                                          |
| passwd codesheep                                      | 修改某⽤户的⼝令                                  |
| w                                                     | 查看活动⽤户                                      |
| id codesheep                                          | 查看指定⽤户 codesheep 信息                       |
| last                                                  | 查看⽤户登录⽇志                                  |
| crontab -l                                            | 查看当前⽤户的计划任务                            |
| cut -d: -f1 /etc/passwd                               | 查看系统所有⽤户                                  |
| cut -d: -f1 /etc/group                                | 查看系统所有组                                    |

## ⽹络和进程管理

| 常用命令                                                      | 作用                                    |
| ------------------------------------------------------------- | --------------------------------------- |
| ifconfig                                                      | 查看⽹络接⼝属性                        |
| ifconfig eth0                                                 | 查看某⽹卡的配置                        |
| route -n                                                      | 查看路由表                              |
| netstat -lntp                                                 | 查看所有监听端⼝                        |
| netstat -antp                                                 | 查看已经建⽴的 TCP 连接                 |
| netstat -lutp                                                 | 查看 TCP/UDP 的状态信息                 |
| ifup eth0                                                     | 启⽤ eth0 ⽹络设备                      |
| ifdown eth0                                                   | 禁⽤ eth0 ⽹络设备                      |
| iptables -L                                                   | 查看 iptables 规则                      |
| ifconfig eth0 192.168.1.1 netmask 255.255.255.0               | 配置 ip 地址                            |
| dhclient eth0                                                 | 以 dhcp 模式启⽤ eth0                   |
| route add -net 0/0 gw Gateway_IP                              | 配置默认⽹关                            |
| route add -net 192.168.0.0 netmask 255.255.0.0 gw 192.168.1.1 | 配置静态路由到达⽹络'192.168.0.0/16'    |
| route del 0/0 gw Gateway_IP                                   | 删除静态路由                            |
| hostname                                                      | 查看主机名                              |
| host [www.baidu.com](http://www.baidu.com)                    | 解析主机名                              |
| nslookup [www.baidu.com](http://www.baidu.com)                | 查询 DNS 记录，查看域名解析是否正常     |
| ps -ef                                                        | 查看所有进程                            |
| ps -ef \| grep codesheep                                      | 过滤出你需要的进程                      |
| kill -s name                                                  | kill 指定名称的进程                     |
| kill -s pid                                                   | kill 指定 pid 的进程                    |
| top                                                           | 实时显示进程状态                        |
| vmstat 1 20                                                   | 每 1 秒采⼀次系统状态，采 20 次         |
| iostat                                                        | iostat                                  |
| sar -u 1 10                                                   | 查询 cpu 使⽤情况（1 秒⼀次，共 10 次） |
| sar -d 1 10                                                   | 查询磁盘性能                            |

## 常⻅系统服务命令

| 常用命令                   | 作用         |
| -------------------------- | ------------ |
| chkconfig --list           | 列出系统服务 |
| service <服务名> status    | 查看某个服务 |
| service <服务名> start     | 启动某个服务 |
| service <服务名> stop      | 终⽌某个服务 |
| service <服务名> restart   | 重启某个服务 |
| systemctl status <服务名>  | 查看某个服务 |
| systemctl start <服务名>   | 启动某个服务 |
| systemctl stop <服务名>    | 终⽌某个服务 |
| systemctl restart <服务名> | 重启某个服务 |
| systemctl enable <服务名>  | 关闭⾃启动   |
| systemctl disable <服务名> | 关闭⾃启动   |

## ⽂件和⽬录操作

| 常用命令                 | 作用                                                           |
| ------------------------ | -------------------------------------------------------------- |
| cd <⽬录名>              | 进⼊某个⽬录                                                   |
| cd ..                    | 回上级⽬录                                                     |
| cd ../..                 | 回上两级⽬录                                                   |
| cd                       | 进个⼈主⽬录                                                   |
| cd -                     | 回上⼀步所在⽬录                                               |
| pwd                      | 显示当前路径                                                   |
| ls                       | 查看⽂件⽬录列表                                               |
| ls -F                    | 查看⽬录中内容（显示是⽂件还是⽬录）                           |
| ls -l                    | 查看⽂件和⽬录的详情列表                                       |
| ls -a                    | 查看隐藏⽂件                                                   |
| ls -lh                   | 查看⽂件和⽬录的详情列表（增强⽂件⼤⼩易读性）                 |
| ls -lSr                  | 查看⽂件和⽬录列表（以⽂件⼤⼩升序查看）                       |
| tree                     | 查看⽂件和⽬录的树形结构                                       |
| mkdir <⽬录名>           | 创建⽬录                                                       |
| mkdir dir1 dir2          | 同时创建两个⽬录                                               |
| mkdir -p /tmp/dir1/dir2  | 创建⽬录树                                                     |
| rm -f file1              | 删除'file1'⽂件                                                |
| rmdir dir1               | 删除'dir1'⽬录                                                 |
| rm -rf dir1              | 删除'dir1'⽬录和其内容                                         |
| rm -rf dir1 dir2         | 同时删除两个⽬录及其内容                                       |
| mv old_dir new_dir       | 重命名/移动⽬录                                                |
| cp file1 file2           | 复制⽂件                                                       |
| cp dir/\* .              | 复制某⽬录下的所有⽂件⾄当前⽬录                               |
| cp -a dir1 dir2          | 复制⽬录                                                       |
| cp -a /tmp/dir1 .        | 复制⼀个⽬录⾄当前⽬录                                         |
| ln -s file1 link1        | 创建指向⽂件/⽬录的软链接                                      |
| ln file1 lnk1            | 创建指向⽂件/⽬录的物理链接                                    |
| find / -name file1       | 从跟⽬录开始搜索⽂件/⽬录                                      |
| find / -user user1       | 搜索⽤户 user1 的⽂件/⽬录                                     |
| find /dir -name \*.bin   | 在⽬录/dir 中搜带有.bin 后缀的⽂件                             |
| locate <关键词>          | 快速定位⽂件                                                   |
| locate \*.mp4            | 寻找.mp4 结尾的⽂件                                            |
| whereis <关键词>         | 显示某⼆进制⽂件/可执⾏⽂件的路径                              |
| which <关键词>           | 查找系统⽬录下某的⼆进制⽂件                                   |
| chmod ugo+rwx dir1       | 设置⽬录所有者(u)、群组(g)及其他⼈(o)的读（r）写(w)执⾏(x)权限 |
| chmod go-rwx dir1        | 移除群组(g)与其他⼈(o)对⽬录的读写执⾏权限                     |
| chown user1 file1        | 改变⽂件的所有者属性                                           |
| chown -R user1 dir1      | 改变⽬录的所有者属性                                           |
| chgrp group1 file1       | 改变⽂件群组                                                   |
| chown user1:group1 file1 | 改变⽂件的所有⼈和群组                                         |

## ⽂件查看和处理

| 常用命令                       | 作用                                       |
| ------------------------------ | ------------------------------------------ |
| cat file1                      | 查看⽂件内容                               |
| cat -n file1                   | 查看内容并标示⾏数                         |
| tac file1                      | 从最后⼀⾏开始反看⽂件内容                 |
| more file1                     | more file1                                 |
| less file1                     | 类似 more 命令，但允许反向操作             |
| head -2 file1                  | 查看⽂件前两⾏                             |
| tail -2 file1                  | 查看⽂件后两⾏                             |
| tail -f /log/msg               | 实时查看添加到⽂件中的内容                 |
| grep codesheep hello.txt       | 在⽂件 hello.txt 中查找关键词 codesheep    |
| grep ^sheep hello.txt          | 在⽂件 hello.txt 中查找以 sheep 开头的内容 |
| grep [0-9] hello.txt           | 选择 hello.txt ⽂件中所有包含数字的⾏      |
| sed 's/s1/s2/g' hello.txt      | 将 hello.txt ⽂件中的 s1 替换成 s2         |
| sed '/^$/d' hello.txt          | 从 hello.txt ⽂件中删除所有空⽩⾏          |
| sed '/ \*#/d; /^$/d' hello.txt | 从 hello.txt ⽂件中删除所有注释和空⽩⾏    |
| sed -e '1d' hello.txt          | 从⽂件 hello.txt 中排除第⼀⾏              |
| sed -n '/s1/p' hello.txt       | 查看只包含关键词"s1"的⾏                   |
| sed -e 's/ \*$//' hello.txt    | 删除每⼀⾏最后的空⽩字符                   |
| sed -e 's/s1//g' hello.txt     | 从⽂档中只删除词汇 s1 并保留剩余全部       |
| sed -n '1,5p;5q' hello.txt     | 查看从第⼀⾏到第 5 ⾏内容                  |
| sed -n '5p;5q' hello.txt       | 查看第 5 ⾏                                |
| paste file1 file2              | 合并两个⽂件或两栏的内容                   |
| paste -d '+' file1 file2       | 合并两个⽂件或两栏的内容，中间⽤"+"区分    |
| sort file1 file2               | 排序两个⽂件的内容                         |
| comm -1 file1 file2            | ⽐较两个⽂件的内容(去除'file1'所含内容)    |
| comm -2 file1 file2            | ⽐较两个⽂件的内容(去除'file2'所含内容     |
| comm -3 file1 file2            | ⽐较两个⽂件的内容(去除两⽂件共有部分)     |

## 打包和解压

| 常用命令                          | 作用                       |
| --------------------------------- | -------------------------- |
| zip xxx.zip file                  | 压缩⾄ zip 包              |
| zip -r xxx.zip file1 file2 dir1   | 将多个⽂件+⽬录压成 zip 包 |
| unzip xxx.zip                     | 解压 zip 包                |
| tar -cvf xxx.tar file             | 创建⾮压缩 tar 包          |
| tar -cvf xxx.tar file1 file2 dir1 | 将多个⽂件+⽬录打 tar 包   |
| tar -tf xxx.tar                   | 查看 tar 包的内容          |
| tar -xvf xxx.tar                  | 解压 tar 包                |
| tar -xvf xxx.tar -C /dir          | 将 tar 包解压⾄指定⽬录    |
| tar -cvfj xxx.tar.bz2 dir         | 创建 bz2 压缩包            |
| tar -jxvf xxx.tar.bz2             | 解压 bz2 压缩包            |
| tar -cvfz xxx.tar.gz dir          | 创建 gzip 压缩包           |
| tar -zxvf xxx.tar.gz              | 解压 gzip 压缩包           |
| bunzip2 xxx.bz2                   | 解压 bz2 压缩包            |
| bzip2 filename                    | 压缩⽂件                   |
| gunzip xxx.gz                     | 解压 gzip 压缩包           |
| gzip filename                     | 压缩⽂件                   |
| gzip -9 filename                  | 最⼤程度压缩               |

## RPM 包管理命令

| 常用命令                  | 作用                            |
| ------------------------- | ------------------------------- |
| rpm -qa                   | 查看已安装的 rpm 包             |
| rpm -q pkg_name           | 查询某个 rpm 包                 |
| rpm -q --whatprovides xxx | 显示 xxx 功能是由哪个包提供的   |
| rpm -q --whatrequires xxx | 显示 xxx 功能被哪个程序包依赖的 |
| rpm -q --changelog xxx    | 显示 xxx 包的更改记录           |
| rpm -qi pkg_name          | 查看⼀个包的详细信息            |
| rpm -qd pkg_name          | 查询⼀个包所提供的⽂档          |
| rpm -qc pkg_name          | 查看已安装 rpm 包提供的配置⽂件 |
| rpm -ql pkg_name          | 查看⼀个包安装了哪些⽂件        |
| rpm -qf filename          | 查看某个⽂件属于哪个包          |
| rpm -qR pkg_name          | 查询包的依赖关系                |
| rpm -ivh xxx.rpm          | 安装 rpm 包                     |
| rpm -ivh --test xxx.rpm   | 测试安装 rpm 包                 |
| rpm -ivh --nodeps xxx.rpm | 安装 rpm 包时忽略依赖关系       |
| rpm -e xxx                | 卸载程序包                      |
| rpm -Fvh pkg_name         | 升级确定已安装的 rpm 包         |
| rpm -Uvh pkg_name         | 升级 rpm 包(若未安装则会安装)   |
| rpm -V pkg_name           | RPM 包详细信息校验              |

## YUM 包管理命令

| 常用命令                            | 作用                 |
| ----------------------------------- | -------------------- |
| yum repolist enabled                | 显示可⽤的源仓库     |
| yum search pkg_name                 | 搜索软件包           |
| yum install pkg_name                | 下载并安装软件包     |
| yum install --downloadonly pkg_name | 只 下 载 不 安 装    |
| yum list                            | 显示所有程序包       |
| yum list installed                  | 查看当前系统已安装包 |
| yum list updates                    | 查看可以更新的包列表 |
| yum check-update                    | 查看可升级的软件包   |
| yum update                          | 更新所有软件包       |
| yum update pkg_name                 | 升级指定软件包       |
| yum deplist pkg_name                | 列出软件包依赖关系   |
| yum remove pkg_name                 | 删除软件包           |
| yum clean all                       | 清除缓存             |
| yum clean packages                  | 清除缓存的软件包     |
| yum clean headers                   | 清除缓存的 header    |

## DPKG 包管理命令

| 常用命令             | 作用                    |
| -------------------- | ----------------------- |
| dpkg -c xxx.deb      | 列出 deb 包的内容       |
| dpkg -i xxx.deb      | 安装/更新 deb 包        |
| dpkg -r pkg_name     | 移除 deb 包             |
| dpkg -P pkg_name     | 移除 deb 包(不保留配置) |
| dpkg -l              | 查看系统中已安装 deb 包 |
| dpkg -l pkg_name     | 显示包的⼤致信息        |
| dpkg -L pkg_name     | 查看 deb 包安装的⽂件   |
| dpkg -s pkg_name     | 查看包的详细信息        |
| dpkg –unpack xxx.deb | 解开 deb 包的内容       |

## APT 软件⼯具

| 常用命令                  | 作用                   |
| ------------------------- | ---------------------- |
| apt-cache search pkg_name | 搜索程序包             |
| apt-cache show pkg_name   | 获取包的概览信息       |
| apt-get install pkg_name  | 安装/升级软件包        |
| apt-get purge pkg_name    | 卸载软件（包括配置）   |
| apt-get remove pkg_name   | 卸载软件（不包括配置） |
| apt-get update            | 更新包索引信息         |
| apt-get upgrade           | 更新已安装软件包       |
| apt-get clean             | 清理缓存               |

#### sshpass 的使用

- sshpass 主要是 使用 ssh 和 scp 时能直接使用密码进行执行命令

  ```sh
  ## 可以把密码写在脚本中
  sshpass -p password scp /home/test/test.txt user@127.0.0.1:/home/test/
  ```

#### 其他常用命令

- 开发常用命令

  ```sh
  ## 查看环境变量的命令
  printenv

  ## 文件类型 查看命令
  file filename

  ## cat 使用行号
  cat -n filename

  ## cat 不使用行号
  cat -b filename

  ## less命令
  less filename

  ## f 向后翻页
  ## b 向前翻页
  ## j 向下一行
  ## k 向上一行
  ## -N  + enter键 显示行数/不现实行数

  ## sort 命令
  ## 默认按字母顺序排序
  ## 默认数字是按开头的数字排序
  ## 不指定数字的排序 1 11 11 2 21 22 ...
  sort filename

  #数字按大小排序，需要使用 -n

  ## shell中命令别名

  #查看命令别名
  alias -p

  #自定义别名 不能有空格
  ## 修改只在当前shell窗口中有效
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
