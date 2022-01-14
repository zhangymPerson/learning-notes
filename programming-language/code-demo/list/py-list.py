#!/usr/bin/env python3
import copy


def run():
    print("start ...")
    arr = [1, 2, 45, 45, 2, 45, 44, 785, 545, 54, 55, 6]
    brr = [12, 23, 4325, 4532, 232, 2345, 4234, 73285, 5345, 54, 55, 6]
    compareTwoList(arr, brr)
    # test()
    # sort()
    # distinct()
    print("end ...")


def compareTwoList(arr, brr):
    """
    获取两个集合的 交集 并集 差集
    """
    if isinstance(arr, list):
        print("arr 类型不正确")
    if isinstance(brr, list):
        print("brr 类型不正确")
    # 交集
    intList = set(arr).intersection(set(brr))
    print("交集", list(intList))
    # 并集
    # arr + brr
    unionList = set(arr).union(set(brr))
    print("并集", list(unionList))
    # 差集
    # arr 中 去掉 brr
    diffList = set(arr).difference(set(brr))
    print("差集", list(diffList))


def analysisWords(words):
    """
    对list中的数据进行分析
    """
    if not isinstance(words, list):
        print("不分析 非list 类型")
        return
    if len(words) == 0:
        print("list 为空")
        return
    if len(words) == len(set(words)):
        print("list 无重复元素")
    else:
        print("list去重前 [%s]" % len(words))
        print("list去重后 [%s]" % len(set(words)))
    map = {}
    for word in words:
        if word not in map:
            map[word] = 1
        else:
            map[word] = map.get(word) + 1
    print("list中word出现的次数对应关系是:\n", json.dumps(
        map, ensure_ascii=False, indent=4))


def sort():
    intList = [13, 2, 3, 5, 44, 5, 56, 76, 76, 5454, 5464, 666, 5, 65, 655]
    print(intList)
    # 排序
    intList.sort()
    print(intList)


def distinct():
    intList = [1, 2, 2, 3, 2, 2, 2, 2, 343, 4,
               43, 43, 4, 34, 43, 43, 43, 43, 4, 44]
    # 去重
    intSet = list(set(intList))
    # 恢复原来顺序
    intSet.sort(key=intList.index)
    print(intSet)


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
