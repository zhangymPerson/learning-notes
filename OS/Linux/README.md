# Linux 服务器相关笔记

- [返回](../README.md)

## 目录

- [Linux 磁盘相关.md](./Linux磁盘相关.md)
- [Linux-firewall.md](./Linux-firewall.md)
- [linux-ip.md](./linux-ip.md)
- [Linux-namespace.md](./Linux-namespace.md)
- [Linux-进程.md](./Linux-进程.md)
- [Linux_awk.md](./Linux_awk.md)
- [Linux_sed.md](./Linux_sed.md)
- [Linux 下磁盘扩容.md](./Linux下磁盘扩容.md)
- [Linux 常用命令.md](./Linux常用命令.md)
- [LVM 相关笔记.md](./LVM相关笔记.md)
- [RAID(磁盘阵列)相关笔记.md](<./RAID(磁盘阵列)相关笔记.md>)
- [yum.md](./yum.md)
- [线程的概念.md](./线程的概念.md)

## 其他

##　环境变量

### 全局(所有用户)

- 修改`/etc/profile`

  ```sh
  # 修改环境变量配置文件
  vim /etc/profile
  # 生效
  source /etc/profile
  ```

### 单个用户的环境变量(用户目录)

- 修改`~/.bash_profile`

  ```sh
  # 跳到指定用户
  su username
  # 修改单个用户的环境变量配置
  vim ~/etc/.bash_profile
  # 生效
  source /etc/.bash_profile
  ```
