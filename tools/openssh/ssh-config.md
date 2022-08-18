# ssh 配置说明

- [返回](./README.md)

- **ssh 配置分为客户端配置和服务端配置**(重点)

## 服务端配置

- 位置

  - `/etc/ssh/sshd_config` 文件

  - `/etc/ssh/sshd_config.d` 目录下

- 配置项说明

  - ListenAddress

  ​ 指定 sshd(8) 监听的网络地址，默认监听所有地址。

  ```conf
  #允许root登录
  PermitRootLogin yes
  #不允许空密码登录
  PermitEmptyPasswords no
  # 不允许密码登录
  PasswordAuthentication no
  ```

## 客户端配置

- 位置

  - `/etc/ssh/sshd_config` 文件

  - `/etc/ssh/sshd_config.d` 目录下

- 配置说明

  通过配置 可以 在本地 直接 `ssh home` 到远程服务器中，而不需要输入完整的数据

  配置如下。各个参数的解释:

  ```conf
  # 别名 home是服务器别名   可以直接 使用 ssh home连接
  Host home
      # 如果服务器有域名，使用域名，没有域名则使用具体地址 如:127.0.0.1
      HostName github.com
      # 用户名 gitlab 或者 github 上配置的名称
      User apollo
      # 端口号 没有默认是 22
      Port 4567
      # 配置私钥文件，此私钥文件与目标服务器配置的免密登录公钥要对应
      IdentityFile ~/.ssh/work
  #配置其他服务器，可以配置多个服务器
  Host work
      HostName gitee.com
      User apollo
  ```

## 错误处理

- 常见错误 Bad owner or permissions on .ssh/config 的解决

  ssh 对配置有权限要求 一般的解决方案是 对 报错文件的权限进行修改 如

  `sudo chmod 600 ~/.ssh/config`

  如果整个文件夹下的文件权限都不对 则

  `sudo chmod 600 ~/.ssh/*`
