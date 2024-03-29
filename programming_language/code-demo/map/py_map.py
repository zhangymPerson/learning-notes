#!/usr/bin/env python3

import datetime
import json


def crud():
    # python中的 map 叫 字典
    map = {
        'bob': 7387,
        'alice': 3719,
        'jack': 7052,
    }

    # map查询 get查询不存在不报错 返回 None
    # map['key'] key不存在则报错
    a = map.get('aaaa')
    print(a)
    # a = map['aaaa']

    # 增
    map['test'] = True
    map['testOne'] = 2.2
    map['testTwo'] = None

    # 删除
    del map['testOne']

    # 删除不存在的报错
    # del map['testOneaa']

    # 判断 key 是否存在
    key = 'bob'
    if key in map:
        print(str(map[key]))
    else:
        print(False)

    print(map)
    # 值为列表
    dict1 = {"a": [1, 2]}
    print(dict1["a"][1])

    # 值为字典
    dict2 = {"a": {"c": "d"}}
    print(dict2["a"]["c"])


def toJson():
    """
    python json转化
    """
    dict = {
        "key": "value",
        "1": 1,
        2: True,
        2.1: False,
        "a": None,
        None: 0,
        "中文": "乱码",
        "date": datetime.datetime(2021, 12, 17, 10, 27, 48)
    }

    # 字典转换成json字符串
    # Object of type 'datetime' is not JSON serializable
    # map转json
    cstr = json.dumps(dict, default=str)
    print(cstr)

    # 解决中文乱码问题
    strs = json.dumps(dict, ensure_ascii=False, default=str)
    print(strs)

    # 格式化输出json
    # 格式化 json
    strs = json.dumps(dict, ensure_ascii=False, default=str, indent=2)
    print(strs)

    # json转map
    # json字符串转换成字典
    map = json.loads(strs)
    print(map['2.1'])

    return


def loop():
    """
    遍历map
    """
    map = {
        'bob': 7387,
        'alice': 3719,
        'jack': 7052,
    }
    splitStr = "==========================="
    # 方式一：
    for key in map:
        print(key+':'+str(map[key]))
    print(splitStr)
    # 方式二：
    for key in map.keys():
        print(key+':'+str(map[key]))
    print(splitStr)
    # 遍历 value
    for value in map.values():
        print(value)
    print(splitStr)
    # 方式三：
    for key, value in map.items():
        print(key+':'+str(value))
    print(splitStr)
    # 方式四：
    for (key, value) in map.items():
        print(key+':'+str(value))
    print(splitStr)


def run():
    print("start ...")
    crud()
    toJson()
    loop()
    print("end ...")


if __name__ == '__main__':
    """
    main 运行入口
    python3 py-string.py
    """
    run()
