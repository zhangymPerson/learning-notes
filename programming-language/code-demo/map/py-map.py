#!/usr/bin/env python3

def mapMethod():
    # python中的 map 叫 字典
    map = {
        'bob': 7387,
        'alice': 3719,
        'jack': 7052,
    }

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
        print(map[key])
    else:
        print(False)

    print(map)
    # 值为列表
    dict1 = {"a": [1, 2]}
    print(dict1["a"][1])

    # 值为字典
    dict2 = {"a": {"c": "d"}}
    print(dict2["a"]["c"])


def run():
    print("start ...")
    mapMethod()
    print("end ...")


if __name__ == '__main__':
    """
    main 运行入口
    python3 py-string.py
    """
    run()
