#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@file : py-demo.py
@desc : 脚本运行方式 [python3 py-demo.py]
        脚本说明:
@date : 2022-03-09 11:10:07
@author : danao
@version : 1.0
'''

import datetime

# 全局字典 单个key list set 和 map
key = 'key'
list = []
set = set()
context = dict()


def getNow():
    """
    获取当前格式化时间
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def run():
    print("task start")


if __name__ == '__main__':
    context['start script'] = getNow()
    run()
    context['end script'] = getNow()
    print(context)
