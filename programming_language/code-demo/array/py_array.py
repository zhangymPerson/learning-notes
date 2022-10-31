#!/usr/bin/env python3

def test():
    """
    Python 没有内置对数组的支持，但可以使用 Python 列表代替。
    """
    # 定义数组
    cars = ["Porsche", "Volvo", "BMW"]
    print("cars = %s" % cars)

    # 获取值
    x = cars[0]
    print("第一个元素[%s]" % x)

    # 修改
    cars[0] = "Audi"
    print("cars = %s" % cars)

    # 获取长度
    x = len(cars)
    print("cars 长度 %d" % x)

    # 追加元素
    cars.append("Audi")
    print("cars = %s" % cars)

    # 遍历
    for x in cars:
        print(x)

    # 移除元素
    cars.pop(1)
    print("cars = %s" % cars)


def run():
    print("start ...")
    test()
    print("end ...")


if __name__ == '__main__':
    """
    main 运行入口
    python3 py-string.py
    """
    run()
