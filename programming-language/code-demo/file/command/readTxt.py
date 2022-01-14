#!/usr/bin/env python3

####################################
########### 读取txt文本并处理#########
########### 去重脚本        #########
####################################

import json


def readFile(fileName):
    # 读
    words = []
    with open(file=fileName, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            words.append(line.strip())
    return words


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


def run():
    print("task")
    words = readFile(
        fileName="/Users/zhangyanming02/person/github/learning-notes/programming-language/code-demo/file/conf/t-txt.txt")
    # 获取
    print("原文件 有[%s]行" % len(words))
    print(words)
    # 去重
    newWords = list(set(words))
    print("去重后 有[%s]行" % len(newWords))
    print(json.dumps(newWords))
    analysisWords(words)


if __name__ == '__main__':
    run()
