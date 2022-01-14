#!/usr/bin/env python3
########################
## 比较两个文件中的词    ##
########################

def readFile(fileName):
    words = []
    with open(file=fileName, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            words.append(line.strip())
    return words


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


def compareTwoFile(one, two):
    wordsOne = readFile(one)
    wordsTwo = readFile(two)
    print(wordsOne, wordsTwo)
    compareTwoList(wordsOne, wordsTwo)


def run():
    print("task")
    one = "/Users/zhangyanming02/person/github/learning-notes/programming-language/code-demo/file/command/compare/one.txt"
    two = "/Users/zhangyanming02/person/github/learning-notes/programming-language/code-demo/file/command/compare/two.txt"
    compareTwoFile(one, two)


if __name__ == '__main__':
    run()
