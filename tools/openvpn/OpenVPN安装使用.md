# Linux下安装

- 为vps安装openvpn及所有所需软件

yum install epel-release

yum -y install openssl openssl-devel pam pam-devel


#证书生成
yum -y install easy-rsa

#主要软件
yum -y install openvpn

- 配置文件

    #模板配置文件的位置

    /usr/share/doc/openvpn-*.*.*/sample/sample-config-files/

    #复制配置文件到配置位置
    cp /usr/share/doc/openvpn-*.*.*/sample/sample-config-files/server.conf /etc/openvpn/


    ./easyrsa import-req /etc/openvpn/client/easy-rsa/3.0.3/pki/reqs/dalin.req dalin

**需要配合证书软件easy-rsa结合使用（参考别的笔记）**

配置文件说明

```conf

注：可按照默认模板配置，本例为自定义配置文件，";"还有"#"开头的是注释
--------------------------
# 设置监听IP，默认是监听所有IP
;local a.b.c.d
# 设置监听端口，必须要对应的在防火墙里面打开
port 1194
# 设置用TCP还是UDP协议？（用UDP会比较快些）
;proto tcp
proto tcp
# 设置创建tun的路由IP通道，还是创建tap的以太网通道路，由于IP容易控制，所以推荐使用tun；但如果IPX等必须使用第二层才能通过的通讯，则可以用tap方式，tap也就是以太网桥接
;dev tap
dev tun
# Windows服务端需要给网卡一个名称，linux不需要
;dev-node MyTap
# 这里是重点，必须指定SSL/TLS root certificate (ca),certificate(cert), and private key (key)，ca文件是服务端和客户端都必须使用的，但不需要ca.key，服务端和客户端指定各自的.crt和.key，请注意路径,可以使用以配置文件开始为根的相对路径,也可以使用绝对路径，请小心存放.key密钥文件
ca /usr/share/doc/open***-2.3.7/sample/sample-keys/ca.crt
cert /usr/share/doc/open***-2.3.7/sample/sample-keys/server.crt
key /usr/share/doc/open***-2.3.7/sample/sample-keys/server.key
# 指定Diffie hellman parameters.
dh /usr/share/doc/open***-2.3.7/sample/sample-keys/dh2048.pem
# 配置服务器模式和***使用的网段，Open***会自动提供基于该网段的DHCP服务，但不能和任何一方的局域网段重复,***服务器将会把10.8.0.1留给自己，其余的分配给***客户端，每一个客户端都会从10.8.0.1这个IP到达Open***服务端，如果使用dev tap模式，则需要注释掉该指令。
server 10.8.0.0 255.255.255.0
# 维持一个客户端和virtual IP的对应表，以方便客户端重新连接可以获得同样的IP
ifconfig-pool-persist ipp.txt
# 配置为以太网桥模式（dev tap）,但需要使用系统的桥接功能,这里不需要使用
;server-bridge 10.8.0.4 255.255.255.0 10.8.0.50 10.8.0.100
# 为客户端创建对应的路由,以另其通达公司网内部服务器,但记住，公司网内部服务器也需要有可用路由返回到客户端,这里主要填写open***所在局域网的网段，我的open***所在的局域网是10.0.0.0,如果你的open***所在的局域网是其他的网段，下面请填写其他网段,可以填写多个网段。
;push "route 192.168.20.0 255.255.255.0"
push "route 10.0.0.0 255.255.255.0"
# 若客户端希望所有的流量都通过***传输,则可以使用该语句，其会自动改变客户端的网关为***服务器,推荐关闭，一旦设置，请小心服务端的DHCP设置问题，如果需要抓取所以连接***客户端的流量信息，需要开启，这就是网络上面所说的×××。
;push "redirect-gateway def1 bypass-dhcp" 

# 如果客户端都使用相同的证书和密钥连接VPN，一定要打开这个选项，否则每个证书只允许一个人连接VPN
duplicate-cn

```


# 客户端 下载openvpn软件

- 找到相应的conf配置文件夹


将下载下来的客户端文件填写到此处

easy-rsa/easyrsa3/pki/ca.crt <制作server证书的文件夹> 
easy-rsa/easyrsa3/pki/issued/client.crt <制作server证书的文件夹> 
easy-rsa/easyrsa3/pki/private/client.key <制作client证书的文件夹>

- 创建对应的 ***.ovpn文件
```
client   #这个不能改
proto tcp  #要与server.conf一致
dev tun    #要与server.conf一致
remote 主机外网IP 12306

ca ca.crt   
cert dalin.crt
key dalin.key      #对应所下载的证书

resolv-retry infinite
nobind
mute-replay-warnings

keepalive 20 120
comp-lzo
#user openvpn
#group openvpn

persist-key
persist-tun
status openvpn-status.log
log-append openvpn.log
verb 3
mute 20

```