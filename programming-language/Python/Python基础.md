# Python基础

- Python 标识符

    在 Python 里，标识符由字母、数字、下划线组成。

    在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。

    Python 中的标识符是区分大小写的。

    以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。

    以双下划线开头的 __foo 代表类的私有成员，
    
    以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。

    Python 可以同一行显示多条语句，方法是用分号 ; 分开;
   
- 行和缩进

    学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。


    缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。

- 多行语句

    Python语句中一般以新行作为语句的结束符。

    但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
    ```py
    total = item_one + \
        item_two + \
        item_three
    ```
    语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：

    ```py
    days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

    ```

- Python 引号

    Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。

    其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
    ```py
    word = 'word'
    sentence = "这是一个句子。"
    paragraph = """这是一个段落。
    包含了多个语句"""
    ```
- Python注释

    python中单行注释采用 # 开头。

    python 中多行注释使用三个单引号(''')或三个双引号(""")。
    ```py
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

    # 文件名：test.py


    '''
    这是多行注释，使用单引号。
    这是多行注释，使用单引号。
    这是多行注释，使用单引号。
    '''

    """
    这是多行注释，使用双引号。
    这是多行注释，使用双引号。
    这是多行注释，使用双引号。
    """

    ```
- python基础语法图示

![基础语法图](../../Picture/Python%E5%9F%BA%E7%A1%80%E8%AF%AD%E6%B3%95%E8%AF%B4%E6%98%8E.png)

- python多个字符输出

    ```py
    #非空判断和 %s 的输出 多个%s 使用 %(a,b,c)
    l = [None, False, 0, 0.0, 0, '', (), [], {}]

    for strs in l:
        if strs:
            print("%s is true"%str(strs))
        else:
            print("%s %s %s is false"%(str(strs),str(strs),str(strs)))
    ```

- python 简单日志引入

    ```py
    import logging
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        # 日期格式
    fp = logging.FileHandler('info.log', encoding='utf-8')   #配置日志输出文件和编码格式
    fs = logging.StreamHandler()
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用
    logging.debug('这是个debug级别的信息')#输出时被过滤掉了
    logging.info('这是个info级别的信息')#输出时被过滤掉了
    logging.warning('这是个warning级别的信息')
    logging.error('这是个error级别的信息')
    logging.critical('这是个critical级别的信息')
    ```

- python 主函数

    ```py

    def main():
        logging.info("start ...")
        #coding
        logging.info("end ...")

    if __name__ == '__main__':
        main()
    ```