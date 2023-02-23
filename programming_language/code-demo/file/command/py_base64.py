#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@file : py_base64.py
@desc : 脚本运行方式 [python3 py_base64.py]
        脚本说明:图片转base64工具
@date : 2023-02-23 11:03:50
@auth : danao
@version : 1.0
"""
import base64


def get_img_base64():
    print("函数  get_img_base64 执行")
    # 图片地址
    filename = '***.jpg'
    f = open(filename, 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    print(ls_f)


def main():
    """
    主要是处理
    """
    print("图片转base64的小工具")
    get_img_base64()


if __name__ == "__main__":
    main()
