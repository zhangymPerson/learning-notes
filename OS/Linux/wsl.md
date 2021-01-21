# wsl(Windows Subsystem for Linux)

> 在 `windows` 上使用 `linux` 子系统的方法

## 介绍

- 在 `windows` 上使用 `linux`，以前智能装虚拟机软件，然后虚拟化出一个 `linux` 系统，有虚拟软件对系统和硬件进行相关的封装，以达到在 `windows` 上使用 `linux` 的业务场景

## 安装

- 打开微软应用商店

  搜索 `linux` 选择要安装的版本 下载启动

  第一次启动报错的，需要开启 `windows` 下子系统功能

  - 开启方式:

    在微软自带搜索框中搜索 `启用或关闭 Windows 功能`，

    下拉选择开启`适用于 linux 的 windows 子系统`

  然后在安装

  第一次安装需要输入默认用户名和密码

## 使用

- 如何使用

  安装 wsl 之后 系统每次开机会自动打开该子系统

  连接方式，打开 `powershell` ，输入 `wsl` 即可进行当前子系统 即可当初普通的 linux 系统直接使用

- 修改代理源

  不修改代理源，下载会比较慢

  修改阿里云的代理源

  修改方式

  ```sh
  #备份配置文件
  cd /etc/apt/
  sudo cp sources.list sources.list.bak
  #修改源 改成阿里云的源
  vim sources.list
  :%s/security.ubuntu/mirrors.aliyun/g
  :%s/archive.ubuntu/mirrors.aliyun/g
  #更新
  sudo apt update
  ```

## 卸载

- 如何卸载

  需要使用命令 `wslconfig` , `wslconfig` 有提示按照提示执行命令

  输入 `wslconfig /l` 查看当前开启的子系统

## wsl 使用注意事项

- java 方面

  jdk 需要安装两套，win/linux 不兼容

  maven 需要两套，配置文件不通，可以指向同一个本地仓库文件夹地址

  go 环境需要安装两套

## 配置阿里云镜像源

- ubuntu 系统

  修改 `/etc/apt/sources.list` 文件

  将文件中 所有的 ubuntu 网址 `archive.ubuntu.com` (不同版本不同网址) 修改为 `mirrors.aliyun.com`
