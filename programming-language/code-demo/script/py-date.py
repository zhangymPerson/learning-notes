#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@file : py-date.py
@desc : 脚本运行方式 [python3 py-date.py]
        脚本说明: 获取日期脚本
@date : 2022-03-02 19:25:54
@author : danao
@version : 1.0
'''
import datetime
import time


def getDay(year):
    days = []
    begin = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    while begin <= end:
        days.append(begin.strftime("%Y%m%d"))
        begin = begin + datetime.timedelta(days=1)
    return days


def getNow():
    """
    获取当前格式化时间
    """
    now = time.time()
    now_datetime = datetime.datetime.now(None)
    print(now_datetime)  # 2020-07-21 09:08:15.772915
    # 格式化时间
    # 日期类型转字符串类型
    str_now_date = now_datetime.strftime('%Y-%m-%d %H:%M:%S')  # 注意日期格式大小写
    print(str_now_date)  # 2020-07-21 09:17:42
    
    # 字符串类型转日期类型
    type_datetime = datetime.datetime.strptime(
        str_now_date, '%Y-%m-%d %H:%M:%S')
    print(type(type_datetime))


def run():
    print("task")
    dates = getDay(2021)
    for date in dates:
        with open('debug.log', 'a') as debug:
            debug.write(date + "\n")


if __name__ == '__main__':
    # run()
    getNow()
