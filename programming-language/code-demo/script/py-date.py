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


def getDay(year):
    days = []
    begin = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    while begin <= end:
        days.append(begin.strftime("%Y%m%d"))
        begin = begin + datetime.timedelta(days=1)
    return days


def run():
    print("task")
    dates = getDay(2021)
    for date in dates:
        with open('debug.log', 'a') as debug:
            debug.write(date + "\n")


if __name__ == '__main__':
    run()
