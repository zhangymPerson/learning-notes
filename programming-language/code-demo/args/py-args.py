#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sys


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
    run()
