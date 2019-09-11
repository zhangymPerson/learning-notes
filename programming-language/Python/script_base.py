#!/usr/bin/env python
#_*_encoding:utf-8_*_
"""
python 脚本的基本模板
"""
import logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 日志格式化输出
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"  # 日期格式
# 配置脚本日志记录文件，可取消
fp = logging.FileHandler('script-run.txt', encoding='utf-8')
fs = logging.StreamHandler()
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])  # 调用


def run():
    """
    自定义的实现逻辑和代码
    :return:
    """
    logging.info("自定义实现")


def main():
    logging.info("script start ...")
    run()
    logging.info("script end ...")

if __name__ == '__main__':
    main()