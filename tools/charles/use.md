# 使用方法

- 安装 Charles

- 查找安装 Charles 的电脑 IP

  菜单选项 help -> `Local IP Addresses`

- **重点：需要移动端和PC在同一个路由器/网络环境下**

- 移动端配置请求代理

  手机打开 WiFi，把代理模式设置为手动;

  设置主机名为 Charles 所在机器的 ip，端口号为 Charles 配置的代理端口。

  这样手机客户端的所有 http 请求，都会被 charles 代理。可以方便的查看客户端的 http 请求
