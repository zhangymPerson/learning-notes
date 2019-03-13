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

--------------------- 
作者：qin147896325 

来源：CSDN 

原文：https://blog.csdn.net/zd147896325/article/details/80092563 

版权声明：本文为博主原创文章，转载请附上博文链接！