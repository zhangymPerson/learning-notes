# SSL 简介

- [返回](./README.md)

## 概念

### 密码学中的相关概念

- 密码学(cryptography)：目的是通过将信息编码使其不可读，从而达到安全性。

- 明文(plain text)：发送人、接受人和任何访问消息的人都能理解的消息。

- 密文(cipher text)：明文消息经过某种编码后，得到密文消息。

- 加密(encryption)：将明文消息变成密文消息。

- 解密(decryption)：将密文消息变成明文消息。

- 算法：取一个输入文本，产生一个输出文本。

- 加密算法：发送方进行加密的算法。

- 解密算法：接收方进行解密的算法。

- 密钥(key)：只有发送方和接收方理解的消息

- 对称密钥加密(Symmetric Key Cryptography)：加密与解密使用相同密钥。

- 非对称密钥加密(Asymmetric Key Cryptography)：加密与解密使用不同密钥。

### SSL 概念

- SSL 含义

  Secure Sockets Layer 安全套接层

  SSL 是传输层加密协议

  SSL 协议位于 TCP/IP 协议与应用层协议之间

  [百度百科](https://baike.baidu.com/item/ssl/320778)

- SSL 协议实现的安全机制包含：

  传输数据的机密性：利用对称密钥算法对传输的数据进行加密。

  身份验证机制：基于证书利用数字签名方法对 server 和 client 进行身份验证，当中 client 的身份验证是可选的。

  消息完整性验证：消息传输过程中使用 MAC 算法来检验消息的完整性。

- 加解密算法分为两类：

  对称密钥算法：数据加密和解密时使用同样的密钥。

  非对称密钥算法：数据加密和解密时使用不同的密钥，一个是公开的公钥，一个是由用户秘密保存的私钥。

  利用公钥（或私钥）加密的数据仅仅能用对应的私钥（或公钥）才干解密。

  与非对称密钥算法相比。对称密钥算法具有计算速度快的长处，通经常使用于对大量信息进行加密（如对全部报文加密）；而非对称密钥算法，一般用于数字签名和对较少的信息进行加密。

  SSL 加密通道上的数据加解密使用对称密钥算法。眼下主要支持的算法有 DES、3DES、AES 等，这些算法都能够有效地防止交互数据被窃听。

- SSLclient 必须验证 SSLserver 的身份，SSLserver 是否验证 SSLclient 的身份。则由 SSLserver 决定。

  参考[SSL 协议详解](https://www.cnblogs.com/jeriffe/articles/2804190.html) 参考[SSL 工作原理](https://www.cnblogs.com/bhlsheji/p/4586597.html)
