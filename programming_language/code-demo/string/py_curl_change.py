#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@file : py_curl_change.py
@desc : 脚本运行方式 [python3 py_curl_change.py]
        脚本说明: 从剪切板中获取 curl 命令，然后替换成本地请求地址，并复制到剪切板
@date : 2024-08-01 11:28:05
@auth : danao
@version : 1.0
"""

import pyperclip
import yaml
from pathlib import Path
import sys
import os
import logging
# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s-%(name)s][%(filename)s:%(lineno)d][%(funcName)s][%(levelname)s]%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


def get_yaml_from_file(filename: str):
    """
    # 模板 yaml :
    replaces:
      - old-text: "https://www.baidu.com"
        new-text: "https://127.0.0.1:8080"
      - old-text: "http://www.baidu.com"
        new-text: "http://localhost:8080"
    """
    # 从 yaml 文件中读取 yaml 数据
    with open(filename, 'r', encoding='utf-8') as file:
        # 读取文件内容
        content = file.read()

        # 使用yaml.load()函数将YAML字符串转换为Python字典
        data = yaml.load(content, Loader=yaml.FullLoader)

        # 打印转换后的数据
        logging.debug(f"type = {type(data)},data = {data}")

        # 访问字典中的特定值
        logging.debug(data.get('replaces'))
        return data.get('replaces')


def read_and_modify_clipboard(array: list) -> str:
    # 读取剪切板内容
    clipboard_content = pyperclip.paste()
    if clipboard_content:
        # 修改剪切板内容
        logger.debug(f"当前剪切板内容:{clipboard_content}")
        if array:
            for item in array:
                logger.debug(f"item = {item}")
                clipboard_content = clipboard_content.replace(
                    item.get('old-text'), item.get('new-text'))

        if clipboard_content.startswith("curl"):
            # 是否包含 -sS 字符
            if clipboard_content.find('-sS') == -1:
                # -S 选项允许显示错误信息，而 -s 选项则隐藏其他信息
                clipboard_content = clipboard_content.replace(
                    'curl', 'curl -sS').replace("\\", "").replace("\n", " ")
                clipboard_content = clipboard_content+" | python -m json.tool"
                logger.debug(f"clipboard_content = {clipboard_content}")

        # 将修改后的内容写回剪切板
        pyperclip.copy(clipboard_content)
        logger.debug(f"剪切板内容已更新为:\n{clipboard_content}")
        return clipboard_content
    else:
        logger.error("剪切板中没有内容。")
        return clipboard_content


def main(run: bool):
    """
    主要是处理
    """
    try:
        home_directory = Path.home()
        config_name = f"{home_directory}/.config/replace.yaml"
        logging.debug(f"config_name = {config_name}")
        arr = get_yaml_from_file(config_name)
        command_str = read_and_modify_clipboard(arr)
        print(command_str)
        if run:
            logger.info(f"curl = \n{command_str}")
            print("")
            print("执行结果:")
            # 执行命令
            logging.debug(f"command_str = {command_str}")
            os.system(command_str)
    except Exception as e:
        # 打印错误所在位置
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    run = False
    # 如果 -h 参数，则打印帮助信息
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        print("Usage: python3 py_clipboard_text_replacement.py [-h] [-d] [-r]")
        print("-h: 打印帮助信息.")
        print("-d: 打印 debug 信息.")
        print("-r: 直接运行修改后的信息")
        sys.exit(0)
    #  如果后面加 -d 参数，则打印调试信息
    if len(sys.argv) > 1 and sys.argv[1] == "-d":
        logging.getLogger().setLevel(logging.DEBUG)
    # 如果添加了 -r 参数，则运行
    if len(sys.argv) > 1 and sys.argv[1] == "-r":
        run = True
    main(run)
