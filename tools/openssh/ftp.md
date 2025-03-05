### FTP 命令备忘录

一些常用的 `FTP` 命令及其用法，使用 FTP 客户端时更高效地进行文件传输和管理。

#### 安装 ftp 命令

- mac 安装

  inetutils 是一个包含 FTP 客户端和 telnet 客户端的工具包，它提供了一些命令行工具，如 ftp 和 telnet，用于在命令行中进行网络通信。
  `brew install inetutils`

- windows 安装

  下载并安装 [WinSCP](https://winscp.net/eng/download.php)。

#### 1. 连接到 FTP 服务器

- **连接到 FTP 服务器**

  ```sh
  ftp <服务器地址>
  ```

  例如：

  ```sh
  ftp 192.168.3.53
  ```

#### 2. 登录到 FTP 服务器

- 连接到服务器后，使用 `user` 命令进行登录。

  ```sh
  user <用户名>
  ```

  例如：

  ```sh
  user user
  ```

  然后输入密码：

  ```sh
  123456
  ```

#### 3. 列出目录内容

- **列出当前目录内容**

  ```sh
  ls
  ```

- **列出远程目录内容**

  ```sh
  ls <远程目录路径>
  ```

  例如：

  ```sh
  ls /home/vsftpd/myuser
  ```

#### 4. 切换目录

- **切换远程目录**

  ```sh
  cd <远程目录路径>
  ```

  例如：

  ```sh
  cd /home/vsftpd/myuser
  ```

- **切换本地目录**

  ```sh
  lcd <本地目录路径>
  ```

  例如：

  ```sh
  lcd /Users/zhangyanming/person/project/person/learning-notes/tools/openssh
  ```

#### 5. 上传文件

- **上传单个文件**

  ```sh
  put <本地文件路径>
  ```

  例如：

  ```sh
  put myfile.txt
  ```

- **上传多个文件**

  ```sh
  mput <本地文件路径1> <本地文件路径2>
  ```

  例如：

  ```sh
  mput file1.txt file2.txt
  ```

- **上传目录中的所有文件**
  ```sh
  mput *
  ```

#### 6. 下载文件

- **下载单个文件**

  ```sh
  get <远程文件路径>
  ```

  例如：

  ```sh
  get myfile.txt
  ```

- **下载多个文件**

  ```sh
  mget <远程文件路径1> <远程文件路径2>
  ```

  例如：

  ```sh
  mget file1.txt file2.txt
  ```

- **下载目录中的所有文件**
  ```sh
  mget *
  ```

#### 7. 删除文件

- **删除远程文件**

  ```sh
  delete <远程文件路径>
  ```

  例如：

  ```sh
  delete myfile.txt
  ```

- **删除多个远程文件**

  ```sh
  mdelete <远程文件路径1> <远程文件路径2>
  ```

  例如：

  ```sh
  mdelete file1.txt file2.txt
  ```

- **删除远程目录中的所有文件**
  ```sh
  mdelete *
  ```

#### 8. 创建目录

- **创建远程目录**

  ```sh
  mkdir <远程目录路径>
  ```

  例如：

  ```sh
  mkdir newfolder
  ```

#### 9. 删除目录

- **删除远程目录**

  ```sh
  rmdir <远程目录路径>
  ```

  例如：

  ```sh
  rmdir oldfolder
  ```

#### 10. 退出 FTP 会话

- **退出 FTP 会话**

  ```sh
  bye
  ```

  或

  ```sh
  quit
  ```

### 注意事项

1. **被动模式（PASV）**：确保 FTP 客户端配置为使用被动模式，特别是在通过防火墙或 NAT 的情况下。
2. **端口配置**：确保服务器的被动模式端口范围（如 21100-21110）在防火墙中开放。
3. **IP 地址**：确保 `PASV_ADDRESS` 设置为正确的主机 IP 地址，而不是 `127.0.0.1`。
