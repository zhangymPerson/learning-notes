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
from kafka import KafkaConsumer
import logging

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s-%(name)s][%(filename)s:%(lineno)d][%(funcName)s][%(levelname)s]%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


def get_msg(topic, group_id, kafka_server):
    """
    从指定的Kafka主题中获取消息。

    Args:
        topic (str): Kafka主题的名称。
        group_id (str): 消费者组的ID。
        kafka_server (str): Kafka服务器的地址。

    Returns:
        None

    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=kafka_server,
        group_id=group_id,
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )

    for message in consumer:
        logging.info(f"topic={message.topic}, "
                     f"partition={message.partition}, "
                     f"offset={message.offset}, "
                     f"key={message.key}, "
                     f"value={message.value}"
                     )


def read_all_file(file_name):
    """
    读取整个文件
    """
    # 读
    with open(file=file_name, mode='r', encoding='utf-8') as f:
        content = f.read()
        return content


def main():
    """
    主要是处理
    """
    topic = "test_topic_1"
    kafka_server = "localhost:9092"
    group_id = "test"
    get_msg(topic, group_id, kafka_server)


if __name__ == "__main__":
    main()
