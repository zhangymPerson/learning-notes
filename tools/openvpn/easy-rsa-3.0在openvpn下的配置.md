
```sh
# 安装 
yum -y install openvpn easy-rsa

# 创建目录
mkdir /etc/openvpn/easy-rsa
#复制到目录
cp -r /usr/share/easy-rsa/ /etc/openvpn/easy-rsa
cd /etc/openvpn/easy-rsa/
#进入到目录
cd 3.0.3/
#创建空的pki
./easyrsa init-pki
#创建新的CA，不使用密码 
 ./easyrsa build-ca nopass
 #创建服务端证书
./easyrsa gen-req server nopass
#签约服务端证书
./easyrsa sign server server
#创建Diffie-Hellman
./easyrsa gen-dh

#创建客户端证书
mkdir /etc/openvpn/client/easy-rsa
cp -r /usr/share/easy-rsa/ /etc/openvpn/client/easy-rsa
#进入客服端位置
cd 3.0.3
#创建空的pki
 ./easyrsa init-pki
  #客户证书名为boyi_new，木有密码
./easyrsa gen-req boyi_new nopass

#进入服务端位置
cd /etc/openvpn/easy-rsa/easy-rsa/3.0.3/
#签约客户端证书
./easyrsa import-req /etc/openvpn/client/easy-rsa/easy-rsa/3.0.3/pki/reqs/boyi_new.req boyi_new
./easyrsa sign client boyi_new


# 整理所有生成的证书

#服务端所需要的文件
-rw-------. 1 root root 1172 4月  11 10:02 ca.crt
-rw-------. 1 root root  424 4月  11 10:03 dh.pem
-rw-------. 1 root root 4547 4月  11 10:03 server.crt
-rw-------. 1 root root 1704 4月  11 10:02 server.key

# 客户端需要的文件

-rw-------. 1 root root 1172 4月  11 10:07 ca.crt
-rw-------. 1 root root 4431 4月  11 10:08 boyi_new.crt
-rw-------. 1 root root 1704 4月  11 10:08 boyi_new.key

openvpn server端需要的是 
easyrsa3/pki/ca.crt   <制作server证书的文件夹> 
easyrsa3/pki/private/server.key <制作server证书的文件夹> 
easyrsa3/pki/issued/server.crt <制作server证书的文件夹> 
easyrsa3/pki/dh.pem 

openvpn client端需要的是 
easy-rsa/easyrsa3/pki/ca.crt <制作server证书的文件夹> 
easy-rsa/easyrsa3/pki/issued/client.crt <制作server证书的文件夹> 
easy-rsa/easyrsa3/pki/private/client.key <制作client证书的文件夹>
```