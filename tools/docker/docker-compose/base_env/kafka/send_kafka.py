#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@file : send_kafka.py
@desc : 脚本运行方式 [python3 send_kafka.py]
        脚本说明: 向kafka发送消息 
@date : 2024-12-12 10:41:49
@auth : danao
@version : 1.0
"""
import time
from kafka import KafkaProducer
import logging

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s-%(name)s][%(filename)s:%(lineno)d][%(funcName)s][%(levelname)s]%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


def send_msg(topic, kafka_server, msg):
    """
    向kafka发送消息
    """
    try:
        logger.debug('kafka server is %s', kafka_server)
        producer = KafkaProducer(bootstrap_servers=kafka_server)
        producer.send(topic, msg.encode("utf-8"))
    except Exception as e:
        logger.error(e)


def read_all_file(file_name):
    """
    读取整个文件
    """
    # 读
    with open(file=file_name, mode='r', encoding='utf-8') as f:
        content = f.read()
        return content


def send(topic, kafka_server):
    # 循环发送
    while True:
        # 循环10次
        # for i in range(10):
        # 读取 msg.txt 中的内容
        msg = read_all_file("msg.txt")
        # 计算函数执行毫秒时间
        start_time = time.time()
        send_msg(topic, kafka_server, msg)
        end_time = time.time()
        print(f"发送耗时: {end_time - start_time} s,消息内容:{msg}")
        # 每隔 10s 发送一次消息
        # time.sleep(100)


def main():
    """
    主要是处理
    """
    topic = "test_topic_1"
    kafka_server = "localhost:9092"
    send(topic, kafka_server)


if __name__ == "__main__":
    main()
