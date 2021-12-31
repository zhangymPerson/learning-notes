#!/usr/bin/env python3


def setCurd():
    # 新建set
    keys = set()
    keys.add("a")
    print("set = ", keys)
    
    # 会自动去重
    setOne = {1, 2, 'a', 'a', 'b', 'c', 'cc'}
    print(setOne)
    # 新增
    setOne.add("aaaa")
    print(setOne)
    # 删除
    setOne.pop()

    # 删除 不存在跳过
    setOne.discard('c')

    # 删除 不存在则报错
    # setOne.remove("abc")

    print(setOne)
    # 两个集合合并
    setOne.update({"ddd", "zzzz"})
    print(setOne)


def setMethod():
    # 用 {} 创建集合
    setOne = {1, 2, 'a', 'a', 'b'}  # 会自动去重的到 {1， 2， 'a', 'b'}
    # 用 set() 函数创建集合
    setTwo = set([2, 3, 'b', 'b', 'c'])  # 将列表转换成集合的过程中会去重得到 {2, 3, 'b','c'}

    # 集合的并集运算（setOne 和 setTwo 中的全部元素 ）
    u = setOne | setTwo
    print(u)
    # 集合的交集运算 （setOne 和 setTwo 中的相同元素）
    i = setOne & setTwo
    print(i)
    # 求差集 （在 setOne 中， 但不在 setTwo 中的元素）
    d = setOne - setTwo
    print(d)
    # 求对称差 （只在 setOne 和 setTwo 其中之一的元素，并集中去除交集的部分）
    d1 = setOne ^ setTwo
    print(d1)


def testSet():
    print("test set")
    setMethod()


def run():
    print("start ...")
    # testSet()
    setCurd()
    print("end ...")


if __name__ == '__main__':
    """
    main 运行入口
    python3 py-string.py
    """
    run()
