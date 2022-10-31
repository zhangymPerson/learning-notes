#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import argparse
import datetime
import sys


def get_date(start_date, end_date):
    """
    根据起止日期，获取中间所有的日期
    日期格式 yyyyMMdd 20220101
    """
    print("开始日期[%s],结束日期[%s]" % (start_date, end_date))
    dates = []
    if end_date < start_date:
        print("开始日期不能大于结束日期")
        return dates
    date = start_date
    dates.append(date)
    dt = datetime.datetime.strptime(start_date, '%Y%m%d')
    while date < end_date:
        dt = dt + datetime.timedelta(days=1)
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


def argparseCmd():
    """
    argparse 库的基本使用 
    python3 py_args.py nameValue birthValue -r 少数民族 -a 20 -g male -p 1212 21 21 -o cc dd ee
    """
    args = argparse.ArgumentParser(
        description='Personal Information ', epilog='Information end ')
    # 必写属性,第一位
    args.add_argument("name", type=str, help="Your name")
    # 必写属性,第二位
    args.add_argument("birth", type=str, help="birthday")
    # 可选属性,默认为None
    args.add_argument("-r", '--race', type=str, dest="race", help="民族")
    # 可选属性,默认为0,范围必须在0~10
    args.add_argument("-a", "--age", type=int, dest="age",
                      help="Your age", default=0, choices=range(10))
    # 可选属性,默认为male
    args.add_argument('-g', "--gender", type=str, dest="gender", help='Your gender', default='male',
                      choices=['male', 'female'])
    # 可选属性,默认为None,-p后可接多个参数
    args.add_argument("-p", "--parent", type=str, dest='self_key',
                      help="Your parent", default="None", nargs='*')
    # 可选属性,默认为None,-o后可接多个参数
    args.add_argument("-o", "--other", type=str, dest='other',
                      help="other Information", required=False, nargs='*')

    args = args.parse_args()  # 返回一个命名空间,如果想要使用变量,可用args.attr
    print("argparse.args=", args, type(args))
    d = args.__dict__
    for key, value in d.items():
        print('%s = %s' % (key, value))
    # 获取指定元素
    print("===========获取指定元素值=============")
    print('name = %s' % args.name)
    print('p = %s' % args.self_key)


if __name__ == '__main__':
    # 脚本参数测试
    argparseCmd()
    # run()
    # arr = getDate('20210425', '20210505')
    # print(arr)
    # getDate('20200301', '20200205')
