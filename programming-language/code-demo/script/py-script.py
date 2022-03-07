#!/usr/bin/env python3

import time
import sys


class Task(object):
    """
    脚本的主要功能是:

    脚本执行逻辑介绍:
    输入:
    输出:
    逻辑:

    """

    def __init__(self):
        super(Task, self).__init__()

    def input(self, msg):
        """
        输入交互
        msg 是 输入的提示语
        """
        args = input(msg.strip() + "\n")
        print("你的输入是[%s]" % args)
        return args

    def now(self):
        """
        格式化时间
        """
        # 格式化成2016-03-20 11:45:39形式
        res = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 格式化成Sat Mar 28 22:24:24 2016形式
        # print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
        # 将格式字符串转换为时间戳
        # a = "Sat Mar 28 22:24:24 2016"
        # print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
        return res

    def task(self):
        """
        执行脚本任务
        """
        print("task start")
        # python 命令脚本路径 
        print("command python path is [%s]" % sys.path[0])
        print(self.now())
        arg = task.input("请输入参数")


task = Task()
task.task()
