#!/usr/bin/env python3

import json


def mapMethod():
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
    }

    # 字典转换成json字符串
    # map转json
    cstr = json.dumps(dict)
    print(cstr)

    # 解决中文乱码问题
    str = json.dumps(dict, ensure_ascii=False)
    print(splitStr)

    # json转map
    # json字符串转换成字典
    map = json.loads(str)
    print(map['2.1'])

    return


def getMap():
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
    # mapMethod()
    # toJson()
    getMap()
    print("end ...")


if __name__ == '__main__':
    """
    main 运行入口
    python3 py-string.py
    """
    run()
