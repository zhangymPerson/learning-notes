# sftp

- [返回](./README.md)

## 简介

- sftp

  sftp 依赖于 sshd 服务

## 服务搭建

- 确认 openssh 的版本

  `ssh -V` 不得低于 4.8

- 创建用户组和用户

  ```sh
  # 创建用户组
  groupadd sftp
  # 创建用户
  # /bin/false也可以替换为/sbin/nologin，目的是不允许该用户登录到系统中
  useradd -g sftp -s /bin/false sftp
  # 配置密码
  passwd sftp
  ```

- 创建文件夹

  ```sh
  # 创建根目录
  sudo mkdir /data
  # 必须是root用户
  chown root:sftp /data
  # 必须限制权限
  chmod 755 /data

  # 重点
  # 用户目录需要root创建后分配给相应的目录
  # 举例 如 sftp用户
  sudo mkdir -p /data/sftp
  # 默认是sftp是无法读取sftp目录中的文件
  # 需进行如下操作
  chown sftp:sftp /data/sftp
  chmod 755 /data/sftp
  # 这样sftp登录时 才能操作 sftp目录中的内容
  ```

- 修改 sshd 配置

  `vim /etc/ssh/sshd_config`

  配置内容见配置

  校验配置正确性
  `sshd -t`

  重启 sshd 服务
  `systemctl restart sshd`

- 登录

  `sftp sftp@127.0.0.1`

  支持`put / get / ls / cd` 相关操作

## 配置

- 配置说明

  配置文件`/etc/ssh/sshd_config`

  ```conf
  # 找到如下这行，用# 符号注释掉，
  # Subsystem sftp /usr/libexec/openssh/sftp-server

  # 这行指定使用sftp服务使用系统自带的internal-sftp
  Subsystem sftp internal-sftp

  # 这行用来匹配sftpusers组的用户，如果要匹配多个组，多个组之间用逗号分割；
  Match Group sftp

    # 用chroot将用户的根目录指定到%h，%h代表用户home目录，这样用户就只能在用户目录下活动。也可用%u，%u代表用户名。
    ChrootDirectory /data
    # 指定sftp命令
    ForceCommand internal-sftp
    AllowTcpForwarding no
    X11Forwarding no

  # 匹配用户了，多个用户名之间也是用逗号分割
  Match user sftp
    ChrootDirectory /data/sftp
    ForceCommand internal-sftp
    AllowTcpForwarding no
    X11Forwarding no
  ```

## 使用

- 使用

  ```sh
  # 登录sftp 输入密码 或者配置免密登录
  sftp sftp@127.0.0.1
  # 进行操作
  # ls/cd/put/get等
  # 需要创建对应用户权限的目录，然后在进行文件上传下载操作，否则无权限操作
  # 需要使用root用户 进去到 ChrootDirectory 配置的目录下 mkdir sftp_dir 然后 chown sftp:sftp sftp_dir
  cd sftp_dir
  put
  get
  # 权限要在使用前开启 权限大小取决于 root chmod 分配给这个用户的大小
  ```

### SFTP 命令备忘录

#### 1. 简介

`SFTP`（SSH 文件传输协议）是基于 `SSH` 协议的安全文件传输工具。它提供了加密的文件传输通道，确保数据在传输过程中不会被窃听或篡改。

#### 2. 基本用法

- **连接到远程服务器**

  ```bash
  sftp 用户名@主机地址
  ```

  示例：

  ```bash
  sftp user@example.com
  ```

- **指定端口连接**
  如果远程服务器使用非默认端口（22），可以使用 `-oPort` 参数：
  ```bash
  sftp -oPort=端口号 用户名@主机地址
  ```
  示例：
  ```bash
  sftp -oPort=2222 user@example.com
  ```

#### 3. 常用命令

| 命令                       | 描述                         |
| -------------------------- | ---------------------------- |
| `get 远程文件路径`         | 下载远程文件到本地           |
| `put 本地文件路径`         | 上传本地文件到远程服务器     |
| `ls`                       | 列出远程目录下的文件和文件夹 |
| `lls`                      | 列出本地目录下的文件和文件夹 |
| `cd 目录路径`              | 切换远程目录                 |
| `lcd 目录路径`             | 切换本地目录                 |
| `mkdir 目录名`             | 在远程服务器上创建新目录     |
| `rm 文件名`                | 删除远程服务器上的文件       |
| `rmdir 目录名`             | 删除远程服务器上的空目录     |
| `rename 旧文件名 新文件名` | 重命名远程文件或目录         |
| `exit` 或 `bye`            | 退出 SFTP 会话               |

#### 4. 批量操作

- **批量下载文件**
  使用通配符批量下载文件：

  ```bash
  get *.txt
  ```

- **批量上传文件**
  使用通配符批量上传文件：
  ```bash
  put *.jpg
  ```

#### 5. 断点续传

- **启用断点续传**
  使用 `-a` 参数启用断点续传功能：
  ```bash
  sftp -a 用户名@主机地址
  ```

#### 6. 配置文件

- **配置文件路径**
  `~/.ssh/config` 文件可以用来配置常用的 SFTP 连接参数，简化命令行输入。

示例配置：

```bash
Host example
    HostName example.com
    User user
    Port 2222
```

使用配置文件连接：

```bash
sftp example
```

#### 7. 安全提示

- **使用公钥认证**
  推荐使用公钥认证代替密码认证，提高安全性。
  - 生成密钥对：
    ```bash
    ssh-keygen -t rsa
    ```
  - 将公钥添加到远程服务器的 `~/.ssh/authorized_keys` 文件中。
