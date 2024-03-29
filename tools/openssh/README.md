# ssh 学习

## 目录

- [返回](../README.md)

- [ssd 的配置说明](./ssh-config.md)

- [SSL 简介.md](./SSL简介.md)

- [sftp.md](./sftp.md)

## 其他

连接分为两种:基于口令和基于密钥的

- 常用的 ssh 密钥生成

  ```sh
  #生成密钥
  ssh-keygen -t rsa -C "zhangyanmingjiayou@163.com"
  # 指定要生成的密钥文件名称  默认为加密方式名
  # 生成后的位置在 ~/.ssh/ 目录下
  Enter file in which to save the key (~/.ssh/id_ed25519):
  #查看密钥
  cat ~/.ssh/id_rsa.pub
  ```

- 修改密钥文件位置后，需要在 `~/.ssh/config` 文件下修改内容(SSH 密钥生成命令的文件不在指定位置时)

  如果，不管你有什么理由，当你决定去用一个非默认的位置或文件名去存放你的 ssh key。你必须配置好你的 ssh 客户端以找到你的 ssh 私钥去连接 Code 服务器，对于 OpenSSH 客户端，这个通常是在 `~/.ssh/config` 类似的位置配置的：

  ```conf
  #
  # Our company's internal GitLab server
  #
  #自定义host名 配置好可以直接ssh name
  Host selfDefault
  #域名 eg: github.com
      HostName my-git.company.com
      RSAAuthentication yes
      #指定自定义生成的  [密钥文件]  位置  公钥配置在相应要连接的服务器上
      IdentityFile ~/my-ssh-key-directory/company-com-private-key-filename
  ```

- 多 ssh 连接时，多密钥对配置

  需要在~/.ssh/config 文件下修改内容(SSH 文件不在指定位置时)

  ```conf
  #Default github user（DodoMonster@email.com）-这其实是注释
  #把默认的常用的github Host设为github.com较好
  Host github
      HostName github.com
      PreferredAuthentications publickey
      IdentityFile C:\Users\Administrator\.ssh\id_rsa
  #其中Host 后的名字可以随意方便自己记忆，但HostName必须为github.com。
  # ************************************************
  #second user(monster@qq.com)
  Host gitee
      HostName gitee.com
      PreferredAuthentications publickey
      IdentityFile C:\Users\Administrator\.ssh\id_rsa
  #ps:HostName 是域名
  ```

- .ssh/config 文件是 ssh 的配置文件

  可以配置多个服务器

  ```conf
  #别名 home是服务器别名   可以直接 使用 ssh home连接
  Host home
      #如果服务器有域名，使用域名，没有域名则使用具体地址 如:127.0.0.1
      HostName github.com
      #用户名
      User apollo
      #端口号 没有默认是 22
      Port 4567
  #配置其他服务器，可以配置多个服务器
  Host work
      HostName gitee.com
      User apollo

  #其他复杂配置可以百度
  ```

- ssh 连接命令

  ```sh
  #不指定端口默认是22
  #远程连接 linux
  ssh -p 2222 dev@127.0.0.1

  # windows  中xshell
  ssh dev@127.0.0.1:2222
  ```

- 指定密钥登录

  ```sh
  # 生成指定密钥 -t 指定加密方式
  ssh-keygen -t ed25519 -C "邮箱名"
  # 注意 输入指定的密钥文件名 默认和加密方式保持一致，在 ~/.ssh/ 目录下
  Generating public/private ed25519 key pair.
  Enter file in which to save the key (/home/user/.ssh/id_ed25519):'自己输入自己指定的密钥文件名,如:work'

  # 将生成的指定的密钥对应的公钥文件内容复制到要免密登录的远程服务器的 ~/.ssh/authorized_keys 文件中
  # 如: work.pub 文件内容  cat work.pub  然后复制


  # 然后登录时指定私钥文件
  ssh -i ~/.ssh/work work@127.0.0.1
  ```

## ssh / scp 报错解决方式

- 错误 1

  ```sh
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
  @BILS SUGGESTS YOU RUN COMMAND 'clearknownhost' AND RETRY @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
  Someone could be eavesdropping on you right now (man-in-the-middle attack)!
  It is also possible that the RSA host key has just been changed.
  The fingerprint for the RSA key sent by the remote host is
  Please contact your system administrator.
  Add correct host key in /home/work/.ssh/known_hosts to get rid of this message.
  Offending key in /home/work/.ssh/known_hosts:12
  RSA host key for 66danao.com has changed and you have requested strict checking.
  Host key verification failed.
  ```

  解决方式
  删除旧的 IP `vi ~/.ssh/known_hosts`
  删除对应 ip 的相关 rsa 信息（本例可知删除 12 行信息即可）

### ssh-keygen 命令简单介绍

- 通过 ssh-keygen 命令，key 生成所需的秘钥，这里总结了 ssh-key 的使用方法，

  -t 加/解密算法

  -b 秘钥长度,rsa 默认秘钥长度的为 2048

  -C 注释，一般是填写用户名

  -f 指定生成的秘钥文件名，如果不提供此参数则使用默认文件名，如 rsa 私钥默认文件名 ~/.ssh/id_rsa ，公钥默认文件名 ~/.ssh/id_rsa.pub

### ssh-agent

- ssh-agent 网址:https://www.ssh.com/academy/ssh/agent

- 使用 ssh-add 添加私钥到代理，ssh-add 命令会将私钥加入 ssh-agent。

  `ssh-add ~/.ssh/github`

- 查看添加的 ssh
  `ssh-add -l`

- 启动 ssh-agent
  eval `ssh-agent`
