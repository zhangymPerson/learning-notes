#!/usr/bin/env python3
import copy


def run():
    print("start ...")
    test()
    print("end ...")


def test():
    list = ['Google', 'Runoob', 1997, 2000]
    print(list[0])
    print(list[1])
    print(list[2])

    print("第三个元素为 : ", list[2])
    list[2] = 2001
    print("更新后的第三个元素为 : ", list[2])

    list.append('Baidu')
    print("更新后的列表 : ", list)

    print("原始列表 : ", list)
    del list[2]
    print("删除第三个元素 : ", list)

    # 正向遍历
    for i in range(len(list)):
        print(list[i])
    for item in list:
        print(item)

    # 反向遍历
    for i in range(len(list) - 1, -1, -1):
        print(list[i])

    a = [1, 2, 3, 4]
    b = a
    # 复制
    d = copy.copy(a)
    b[0] = 'b'
    print(a, b, d)
    print(id(a), id(b), id(d))


if __name__ == '__main__':
    """
    main 运行入口
    python3 py-string.py
    """
    run()
