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

    安装wsl之后 系统每次开机会自动打开该子系统

    连接方式，打开 `powershell` ，输入 `wsl` 即可进行当前子系统 即可当初普通的 linux 系统直接使用

## 卸载

- 如何卸载

    需要使用命令 `wslconfig` , `wslconfig` 有提示按照提示执行命令

    输入 `wslconfig /l` 查看当前开启的子系统