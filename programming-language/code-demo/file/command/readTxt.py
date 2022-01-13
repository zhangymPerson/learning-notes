#!/usr/bin/env python3

####################################
########### 读取txt文本并处理#########
####################################

def readFile(fileName):
    # 读
    words = []
    with open(file=fileName, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            words.append(line.strip())
    return words


def run():
    print("task")
    words = readFile(
        fileName="/Users/zhangyanming02/person/github/learning-notes/programming-language/code-demo/file/conf/t-txt.txt")
    # 获取
    print(words)
    # 去重
    newWords = list(set(words))
    print(newWords)


if __name__ == '__main__':
    run()
