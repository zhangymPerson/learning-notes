#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@file : py-object.py
@desc : 脚本运行方式 [python3 py-object.py]
        脚本说明: 对象常见的函数
@date : 2022-03-16 20:02:07
@version : 1.0
'''

import datetime

context = dict()


def isNull(obj=None):
    """
    python Null 对象判断

    禁止使用==或!=判断表达式是否为None，应该用is或is not None

    对于 None 等单例对象测试时,使用 is 或者 is not.当你要测试一个默认值是None的变量或参数是否被设为其它值. 这个值在布尔语义下可能是false!

    永远不要用 == 将一个布尔量与false相比较. 使用 if not x: 代替. 如果你需要区分false和None, 你应该用像 if not x and x is not None: 这样的语句.

    对于序列(字符串, 列表, 元组), 要注意空序列是false. 因此 if not seq: 或者 if seq: 比 if len(seq): 或 if not len(seq): 要更好.

    处理整数时, 使用隐式false可能会得不偿失(即不小心将None当做0来处理). 你可以将一个已知是整型(且不是len()的返回结果)的值与0比较.
    return bool
    """
    print("[%s]的判断结果如下:" % obj)
    if obj is None:
        print("A = [%s] is None is true" % obj)
    if obj is not None:
        print("B = [%s] is not None is true" % obj)
    if not obj:
        print("C = [%s] is False" % obj)
    print()
    return False


def testIsNull():
    list = [None, 0, -1, 1, '', '  ', [], [2], set(), set([1, 2, 3]),
            {}, {'key': 'value'}]
    for value in list:
        isNull(value)


def getType(obj=None):
    """
    判断变量类型的函数
    """
    type = None
    if isinstance(obj, int):
        type = "int"
    elif isinstance(obj, str):
        type = "str"
    elif isinstance(obj, float):
        type = "float"
    elif isinstance(obj, list):
        type = "list"
    elif isinstance(obj, tuple):
        type = "tuple"
    elif isinstance(obj, dict):
        type = "dict"
    elif isinstance(obj, set):
        type = "set"
    return type


def testGetType():
    list = [None, 0, -1, 1, '', '  ', [], [2], set(), set([1, 2, 3]),
            {}, {'key': 'value'}]
    for value in list:
        type = getType(value)
        print("[%s] type = [%s]" % (value, type))


def getNow():
    """
    获取当前格式化时间
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def run():
    print("task start")
    testIsNull()
    testGetType()


if __name__ == '__main__':
    context['start script'] = getNow()
    run()
    context['end script'] = getNow()
    print(context)
