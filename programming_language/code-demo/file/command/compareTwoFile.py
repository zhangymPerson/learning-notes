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
    # 差集
    # arr 中 去掉 brr
    diffList = set(arr).difference(set(brr))
    print("a - b 差集", list(diffList))
    diffList = set(brr).difference(set(arr))
    print("b - a 差集", list(diffList))
    # 交集
    intList = set(arr).intersection(set(brr))
    print("交集", list(intList))
    # 并集
    # arr + brr
    unionList = set(arr).union(set(brr))
    print("并集", list(unionList))


def compareTwoFile(one, two):
    wordsOne = readFile(one)
    wordsTwo = readFile(two)
    # print(wordsOne, wordsTwo)
    print("one 数量 [%s] ,two  数量 [%s]" % (len(wordsOne), len(wordsTwo)))
    print("去重后...")
    print("one 数量 [%s] ,two  数量 [%s]" %
          (len(set(wordsOne)), len(set(wordsTwo))))
    compareTwoList(wordsOne, wordsTwo)


def run():
    print("task")
    one = "/Users/work/person/github/learning-notes/programming-language/code-demo/file/command/compare/one.txt"
    two = "/Users/work/person/github/learning-notes/programming-language/code-demo/file/command/compare/two.txt"
    compareTwoFile(one, two)


if __name__ == '__main__':
    run()
