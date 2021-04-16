# xshell 使用

- [返回](./README.md)

- xshell 总是前端显示解决办法

  - 使用 `alt+a`，问题解决

  - view（查看） —> Always on top （总在最前）前面的勾去掉就 OK 了

- xshell 中没有会话框解决办法

  - 快捷键 `ctrl+shift+t`

  - 菜单栏中

    - 英文 view——session tab

    - 中文 查看——会话选项卡

- xshell 批量执行 (一个命令全部终端执行)

  在“查看”菜单栏中，勾选“撰写栏”；

  在界面下方的框中输入命令，完成后，点击右侧的图标三横图标；

  在弹出的对话框中选择“发送到全部会话”

- xshell 连接 wsl

  - 安装新的 ssh 服务，

    ```sh
    # 卸载
    sudo apt-get remove openssh-server
    # 安装
    sudo apt-get install openssh-server
    ```

  - 编辑配置文件 注意修改的是**sshd_config**

    ```sh
    # vim /etc/ssh/sshd_config
    # 默认的是22，但是windows有自己的ssh服务用的也是22端口，修改一下
    Port 22
    UsePrivilegeSeparation no
    #允许root登录
    PermitRootLogin yes
    #不允许空密码登录
    PermitEmptyPasswords no
    ```

- 重启 ssh 服务

  ```sh
  # 重启ssh服务
  sudo service ssh --full-restart
  ```
