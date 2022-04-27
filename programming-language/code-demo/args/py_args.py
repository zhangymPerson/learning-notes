#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import datetime
import sys


def getDate(startDate, endDate):
    """
    根据起止日期，获取中间所有的日期
    日期格式 yyyyMMdd 20220101
    """
    print("开始日期[%s],结束日期[%s]" % (startDate, endDate))
    dates = []
    if endDate < startDate:
        print("开始日期不能大于结束日期")
        return dates
    date = startDate
    dates.append(date)
    dt = datetime.datetime.strptime(startDate, '%Y%m%d')
    while date < endDate:
        dt = dt+datetime.timedelta(days=1)
        date = dt.strftime('%Y%m%d')
        dates.append(date)
    print("arr=(", end="")
    for dstr in dates:
        print("%s " % dstr, end="")
    print(")", end="")
    return dates


def run():
    print("start ...")
    args = sys.argv
    print("参数个数 %s" % len(args))
    for arg in args:
        print("参数为%s" % arg)
    print("end ...")


if __name__ == '__main__':
    """
    main 运行入口
    python3 py-string.py
    """
    # run()
    arr = getDate('20210425', '20210505')
    # print(arr)
    # getDate('20200301', '20200205')
