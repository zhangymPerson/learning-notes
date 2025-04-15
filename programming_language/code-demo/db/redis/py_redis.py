#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@file : py-redis.py
@desc : 脚本运行方式 [python3 py-redis.py]
        脚本说明:操作redis
@date : 2022-01-20 16:44:34
@author : danao
@version : 1.0
'''

import argparse
import os
import yaml
from redis import Redis


def parse_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config.get('redis_services', [])


def connect_to_redis(host, port, db, password):
    redis_client = Redis(host=host, port=port, db=db,
                         password=password, decode_responses=True)
    return redis_client


def print_redis_connection_info(redis_client):
    try:
        redis_client.ping()
        print(
            f"已连接到 Redis 服务: {redis_client.connection_pool.connection_kwargs}")
    except Exception as e:
        print(f"无法连接到 Redis 服务: {e}")


def conf_args():
    """函数的作用是:
    获取用户指定参数输入
    Returns:
        return res 返回用户输入的参数字典
    Raises:
        列出与接口有关的所有异常.
    """
    name = os.path.basename(__file__)
    args = argparse.ArgumentParser(
        description=f'脚本[{name}]执行中的参数介绍', epilog='请按照以上说明执行脚本')
    # 配置参数和说明
    args.add_argument("-i", "--info", type=str,
                      help="演示参数 info", default="None")
    args.add_argument('-c', '--config', required=True, help='指定 Redis 配置文件')
    args.add_argument('-n', '--index', type=int,
                      help='指定要连接的 Redis 服务索引（从0开始）')
    args = args.parse_args()
    # print(f"args = [{args}]")
    # 使用方式  args.info 即可获取到参数值  如果有 dest 配置则读取dest 无则读取 -- 后面的属性配置
    return args


def do_task(redis_client):
    print("执行任务...")
    try:
        print("正在执行任务...")
        pass
    except Exception as e:
        print(f"执行任务时出现错误: {e}")
    print("任务完成.")


def main():
    args = conf_args()

    config = parse_config(args.config)
    if not config:
        print("配置文件中没有找到 Redis 服务信息")
        return

    if args.index is not None:
        # 如果指定了索引，则连接指定的 Redis 服务
        if 0 <= args.index < len(config):
            service = config[args.index]
            redis_client = connect_to_redis(
                service['host'], service['port'], service['db'], service.get('password'))
            print_redis_connection_info(redis_client)
            do_task(redis_client)
        else:
            print(f"索引 {args.index} 超出了 Redis 服务的范围（0-{len(config)-1}）")
    else:
        # 如果没有指定索引，则遍历并打印所有 Redis 服务的连接信息
        for idx, service in enumerate(config):
            redis_client = connect_to_redis(
                service['host'], service['port'], service['db'], service.get('password'))
            print(f"Redis 服务 {idx}:")
            print_redis_connection_info(redis_client)


if __name__ == '__main__':
    main()
