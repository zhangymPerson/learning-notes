#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@file : py-log.py
@desc : 脚本运行方式 [python3 py-log.py]
        脚本说明: python日志
@date : 2022-04-27 11:23:11
@auth : danao
@version : 1.0
'''


import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 日志格式化输出
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"  # 日期格式
# 配置脚本日志记录文件，可取消
fp = logging.FileHandler('debug.log', encoding='utf-8')
# 配置日志输出到控制台
fs = logging.StreamHandler()
# 配置 logging 调用上面的两种日志记录方式
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT,
                    datefmt=DATE_FORMAT, handlers=[fs, fp])


def log(info):
    logging.info(info)
