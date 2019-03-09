# 配置python-shell中的tab自动补全


- 编写脚本

    vim tab.py
    存放到 /usr/lib/python**/site**/ 位置   其他位置也可
    ```py
    #!/usr/bin/python   
    # python tab file   
    import sys
    import readline
    import rlcompleter
    import atexit
    import os
    # tab completion   
    readline.parse_and_bind('tab: complete')
    # history file   
    histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
    try:
        readline.read_history_file(histfile)
    except IOError:
        pass
    atexit.register(readline.write_history_file, histfile)

    del os, histfile, readline, rlcompleter
    ```

- 配置

    在 vim ~/.bashrc  追加配置
    #自定义的tab.py存放的位置
    export PYTHONSTARTUP=/usr/lib/python**/site**/ 


- 生效

    source ~/.bashrc


- 重启python shell 
    python 

    tab即可生效


- 简单的方法

    import sys

    print sys.path

    将tab.py作为模块放入 上面命令查找的路径下

    下次启动直接

    直接import tab