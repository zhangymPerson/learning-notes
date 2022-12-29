#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@file : py_getapi.py
@desc : 脚本运行方式 [python3 py_getapi.py]
        脚本说明: 根据 swagger  地址 生成 json 文档
@date : 2022-12-07 10:23:48
@auth : danao
@version : 1.0
"""
import requests
import json
import os
import argparse


def get_openapi_json(url, file_name):
    payload = {}
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        obj = json.loads(response.text)
        obj_json_str = json.dumps(
            obj, ensure_ascii=False, default=str, indent=2)
        # print(f"obj_json_str = [{obj_json_str}]")
        with open(file=file_name, mode='w', encoding='utf-8') as f:
            f.write(obj_json_str)
            print(f"json 写入[{file_name}]文件成功!")
    except Exception as e:
        print(f"处理异常,e = [{e}]")


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
    args.add_argument("-u", "--url", type=str,
                      help="swagger 文档的 url 链接", default="http://127.0.0.1:8080/project_name/v3/api-docs")
    path = os.getcwd()
    file_name = f"{path}/openapi.json"
    args.add_argument("-f", "--file", type=str,
                      help="导出json的文档地址", default=file_name)
    args = args.parse_args()
    # print(f"args = [{args}]")
    # 使用方式  args.info 即可获取到参数值  如果有 dest 配置则读取dest 无则读取 -- 后面的属性配置
    return args


def main():
    """
    主要是处理
    """
    print("hello world!")
    args = conf_args()
    url = args.url
    file_name = args.file
    print(f"url = [{url}]")
    print(f"file_name = [{file_name}]")
    get_openapi_json(url=url, file_name=file_name)


if __name__ == "__main__":
    main()
