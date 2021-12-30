#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# https://www.runoob.com/python3/python3-string.html
class Task(object):
    """docstring for Task."""

    def __init__(self, arg):
        super(Task, self).__init__()
        self.arg = arg

    # 字符串拼接
    def join(self, str1, str2):
        """
        字符串拼接
        """
        if str1 is None:
            if str2 is None:
                return None
            else:
                return str2
        if str2 is None:
            return str1
        return str1 + str2

    # 字符串去掉空格 删除 去掉
    def remove(self, str):
        """
        字符串去掉 \n '' '   '
        """
        # 只删除行末尾的“\n”：
        newStr = str.strip()
        # 去掉行尾的所有空白：
        str.rstrip()
        print("[%s] 去掉 \\n 后 [%s]" % (str, newStr))

    # 字符串为空判断

    # 字符串包含字符判断

    def contain(self):
        str = 'Hello word'
        if 'H' in str:
            print("[%s] 包含 [%s]" % (str, 'H'))

    def replace(self):
        """
        字符串 替换
        """
        str = "hello word aa bb c"
        # 新对象必须用新变量接
        # 需要注意 replace 不会改变原 string 的内容。
        newStr = str.replace("aa", "AAAA")
        print(str, "=>", newStr)

    def getType(self, obj):
        """
        获取类型。类型判断
        """
        return self.typeof(obj)

    def typeof(variate):
        """
        判断变量类型的函数
        """
        type = None
        if isinstance(variate, int):
            type = "int"
        elif isinstance(variate, str):
            type = "str"
        elif isinstance(variate, float):
            type = "float"
        elif isinstance(variate, list):
            type = "list"
        elif isinstance(variate, tuple):
            type = "tuple"
        elif isinstance(variate, dict):
            type = "dict"
        elif isinstance(variate, set):
            type = "set"
        return type


def splitTest():
    """
    字符串截取
    """
    # 0、a,b为参数。从字符串指针为a的地方开始截取字符，到b的前一个位置（因为不包含b）
    str = "hello world"

    # 字符串切割 分割
    list = str.split(" ")
    for key in list:
        print(key)

    a = 0
    b = len(str)
    print(str[a: b])

    # 1、如果a,b均不填写，默认取全部字符。即，下面这两个打印结果是一样的
    print(str[:])  # hello world
    print(str)      # hello world

    # 2、如果a填写，b不填写（或填写的值大于指针下标），默认从a开始截取，至字符串最后一个位置
    print(str[3:])  # lo world

    # 3、如果a不填写， b填写，默认从0位置开始截取，至b的前一个位置
    print(str[: 8])  # hello wo

    print(str[: -2])

    # 4、如果a为负数，默认从尾部某一位置，开始向后截取
    print(str[-2:])  # ld

    # 5、如果a>=b, 默认输出为空。
    print(str[3: 3])
    print(str[3: 2])


def strTolist():
    """
    字符串与列表，元组的互相转换。
    """
    # 字符串转换为列表
    var = '菜鸟教程'
    list = []
    list = [i for i in var]
    print(list)
    # 列表转化为字符串
    # 使用 join 来实现:
    listStr = ' ,'.join(list)
    print(listStr)


def encodeAndDecode(str):
    """
    字符编解码测试
    """
    str_utf8 = str.encode("UTF-8")
    str_gbk = str.encode("GBK")

    print(str)

    print("UTF-8 编码：", str_utf8)
    print("GBK 编码：", str_gbk)

    print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
    print("GBK 解码：", str_gbk.decode('GBK', 'strict'))


def testTwo():
    """
    字符串格式化输出
    """
    res = "我叫 %s 今年 %d 岁!" % ('小明', 10)
    print(res)
    # f-string 格式化字符串以 f 开头，
    # 后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去，实例如下：
    name = "Word"
    res = f'Hello {name}'
    print(res)


def testOne():
    task = Task("")
    # res = task.join("a", "b")
    # a = task.join(None, "a")
    # b = task.join("a", None)
    # c = task.join(None, None)
    # d = task.join(1, 2)
    # print(res, a, b, c, d)
    arr = ["a", "中国", "你\n好", "bb\n",
           "abcd\nefgij\nklmnopqrstuvwxyz", " ", "", "\n", "\t"]
    for str in arr:
        task.remove(str)
    # task.contain()
    # task.replace()


def run():
    print("start ...")
    testOne()
    # testTwo()
    # arr = ["a", "中国", "你好", "bb", "abcdefgijklmnopqrstuvwxyz", " ", "", "\n", "\t"]
    # 编解码测试
    # for key in arr:
    #     encodeAndDecode(key)
    # strTolist()
    # splitTest()

    print("end ...")


if __name__ == '__main__':
    """
    main 运行入口
    python3 py-string.py
    """
    run()
