#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@file : py-redis.py
@desc : 脚本运行方式 [python3 py-redis.py]
        脚本说明:操作redis
@date : 2022-01-20 16:44:34
@author : danao
@version : 1.0
'''

import redis


def redisTest():
    pool = redis.ConnectionPool(
        host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # 设置 name 对应的值
    r.set('name', 'runoob')
    # 取出键 name 对应的值
    print(r.get('name'))


def run():
    print("task")
    redisTest()


if __name__ == '__main__':
    run()
