#!/usr/bin/env python3


import os


def writeToFile(msg, fileName):
    """
    写文件
    """
    # 写 w 写 w+ 读写 会删除原有内容  a 追加
    with open(file=fileName, mode='a', encoding='utf-8') as f:
        f.write(msg)


def printFile(fileName):
    """
    按行读文件
    """
    # 读
    with open(file=fileName, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line)


def removeFile(fileName):
    os.remove(fileName)


def run():
    print("start ...")
    file = "test.log"
    writeToFile("test\n", fileName=file)
    writeToFile("test", fileName=file)
    writeToFile("test", fileName=file)
    printFile(fileName=file)
    removeFile(file)
    print("end ...")


if __name__ == '__main__':
    """
    main 运行入口
    python3 py-string.py
    """
    run()
