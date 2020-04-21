# python脚本日常积累

## logging使用

**注意** python中的logging的参数字符需要为一个整的字符串，


- python使用 logging 的脚本

    ```py
    #!/usr/bin/env python
    # _*_encoding:utf-8_*_
    import logging

    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 日志格式化输出
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"  # 日期格式
    # 配置脚本日志记录文件，可取消
    fp = logging.FileHandler('script-run.log', encoding='utf-8')
    fs = logging.StreamHandler()
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])  # 调用


    def run():
        """
        自定义的实现逻辑和代码
        :return:
        """
        logging.info("自定义实现")


    def main():
        logging.info("script start ...")
        run()
        logging.info("script end ...")


    if __name__ == '__main__':
        main()

    ```

- python使用getopt的脚本

    ```py
    # _*_encoding:utf-8_*_

    import getopt
    import sys


    def main():
        """
        getopt函数的使用
        python脚本读取 -a --aaa 参数
        :return:
        """
        shortargs = 'a:b:c'
        longargs = ['aaa=', 'bbb', 'ccc']
        optlist, args = getopt.getopt(sys.argv[1:], shortargs, longargs)
        # optlist 是 key : value 格式的参数 args是脚本后面跟着的参数
        print(optlist)
        print(args)
        for optlist_namess, optlist_value in optlist:
            print(optlist_namess, optlist_value)
        print("start")


    if __name__ == '__main__':
        main()

    ```

- 生成uuid

    ```py
    import uuid


    def gen_uuid():
        """
        生成uuid
        :return:
        """
        return ''.join(str(uuid.uuid4()).split('-'))
    ```