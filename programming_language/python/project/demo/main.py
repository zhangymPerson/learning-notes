#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@file : main.py
@desc : 脚本运行方式 [python3 main.py]
        脚本说明: 项目入口
@date : 2023-05-19 15:26:43
@auth : danao
@version : 1.0
"""

# 引入项目的业务代码
import module.server


def main():
    """
    项目启动入口
    """
    print("项目启动")
    module.server.server()


if __name__ == "__main__":
    main()
