# ssh学习

连接分为两种:基于口令和基于密钥的   

- 常用的ssh密钥生成

    #生成密钥
    ssh-keygen -t rsa -C "zhangyanmingjiayou@163.com"
    #查看密钥
    cat ~/.ssh/id_rsa.pub

- 修改密钥文件位置后，需要在~/.ssh/config文件下修改内容(SSH密钥生成命令的文件不在指定位置时)

    如果，不管你有什么理由，当你决定去用一个非默认的位置或文件名去存放你的ssh key。你必须配置好你的ssh客户端以找到你的ssh私钥去连接Code服务器，对于OpenSSH客户端，这个通常是在~/.ssh/config类似的位置配置的：
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
- 多ssh连接时，多密钥对配置

    需要在~/.ssh/config文件下修改内容(SSH文件不在指定位置时)
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