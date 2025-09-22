#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@file : py_sftp.py
@desc : 脚本运行方式 [python3 py_sftp.py]
        脚本说明: 测试sftp
        脚本说明: 测试sftp，包括文件的上传和下载
@date : 2025-03-28 16:46:20
@auth : danao
@version : 1.0
@version : 1.1
"""

import paramiko


def upload_file(sftp, local_path, remote_path):
    """
    上传文件到SFTP服务器

    :param sftp: SFTP客户端对象
    :param local_path: 本地文件路径
    :param remote_path: 远程文件路径
    """
    try:
        sftp.put(local_path, remote_path)
        print(f"文件上传成功: {local_path} -> {remote_path}")
    except Exception as e:
        print(f"文件上传失败: {e}")


def download_file(sftp, remote_path, local_path):
    """
    从SFTP服务器下载文件

    :param sftp: SFTP客户端对象
    :param remote_path: 远程文件路径
    :param local_path: 本地文件路径
    """
    try:
        sftp.get(remote_path, local_path)
        print(f"文件下载成功: {remote_path} -> {local_path}")
    except Exception as e:
        print(f"文件下载失败: {e}")


def main():
    """
    sftp测试
    """
    print("hello world!")
    hostname = 'localhost'  # SFTP服务器主机名或IP地址
    port = 2222 # SFTP服务器端口，默认为22
    username = 'foo'  # SFTP服务器用户名
    password = '123'  # SFTP服务器密码

    local_upload_path = '~/.vimrc'  # 本地要上传的文件路径
    remote_upload_path = '/'  # 远程文件路径

    local_download_path = '~/.a'  # 本地保存下载文件的路径
    remote_download_path = '/.vimrc'  # 远程要下载的文件路径

    try:
        # 创建SSH客户端
        ssh_client = paramiko.SSHClient()
        # 自动添加策略，保存服务器的主机名和密钥信息
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接到SFTP服务器
        ssh_client.connect(hostname=hostname, port=port,
                           username=username, password=password)

        # 打开SFTP会话
        sftp = ssh_client.open_sftp()

        print("SFTP连接成功")

        # 上传文件
        upload_file(sftp, local_upload_path, remote_upload_path)

        # 下载文件
        download_file(sftp, remote_download_path, local_download_path)

        # 关闭SFTP会话
        sftp.close()
        # 关闭SSH连接
        ssh_client.close()
    except Exception as e:
        print(f"SFTP操作失败: {e}")


if __name__ == "__main__":
    main()
