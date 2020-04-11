# Python 文件中遇到的问题
## Python3以上版本安装sqlite3的解决方案

首先大概会报一下两个问题：

1. no mudole named _sqlite3

2. mportError: dynamic module does not define module export function (PyInit__caffe)

其实这两个问题都是因为python3以上版本不太支持sqlite3，下面的方法是亲测没问题，来自（sparkexpert大神）

- 安装sqlite3的包

    ```  
    $ wget https://www.sqlite.org/2017/sqlite-autoconf-3170000.tar.gz --no-check-certificate
    $ tar zxvf sqlite-autoconf-3170000.tar.gz
    $ cd sqlite-autoconf-3170000
    $ ./configure --prefix=/usr/local/sqlite3 --disable-static --enable-fts5 --enable-json1 CFLAGS="-g -O2 -DSQLITE_ENABLE_FTS3=1 -DSQLITE_ENABLE_FTS4=1 -DSQLITE_ENABLE_RTREE=1"
    ```
- 对python3进行重新编译

    ```    
    $ cd Python-3.6.0a1
    $ LD_RUN_PATH=/usr/local/sqlite3/lib ./configure LDFLAGS="-L/usr/local/sqlite3/lib" CPPFLAGS="-I /usr/local/sqlite3/include"
    $ LD_RUN_PATH=/usr/local/sqlite3/lib make
    $ LD_RUN_PATH=/usr/local/sqlite3/lib sudo make install
    ```
    
经过上述步骤后，应该就没有什么问题了，控制台输入python3进入环境

import sqlite3没报错说明ok

## python中不支持 ++ -- 运算

- 原因

    需要使用id() 函数
    id() 函数返回对象的唯一标识符，标识符是一个整数。
    CPython 中 id() 函数用于获取对象的内存地址。
    
    如下所示
    
    ```py
    Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> a = 5
    >>> b = 5
    >>> id(5)
    1849852144
    >>> id(a)
    1849852144
    >>> id(b)
    1849852144
    >>>
    ```

    变量a,b事实上指向的是同一个内存空间。

    python不支持n++这种写法。

    因此，正确的自增操作应该 n = n + 1 或者 n += 1。

    因为有重新赋值的过程 相当于 n 指向一个新的地址