# shell 基本概念和变量
- 概念

    在计算机科学中，Shell俗称壳（用来区别于核），是指“为使用者提供操作界面”的软件（命令解析器）。它类似于DOS下的command.com和后来的cmd.exe。它接收用户命令，然后调用相应的应用程序。   - 百度百科

- Linux 上的shell

    建议:学会使用vim 等 linux上的编辑器

    第一个shell
    ```sh
    vim a.sh

    #!/bin/bash
    echo "Hello World !"

    #运行shell
    #为脚本添加可执行权限
    chmod +x a.sh
    #在脚本目录文件下
    ./a.sh

    #作为解释器参数

    #这种运行方式是，直接运行解释器，其参数就是 shell 脚本的文件名，如：
    sh test.sh

    ```

    **注意** : 如果#!/bin/bash 报错 可使用 which bash查找bash的路径

- shell中的变量

    - shell中的变量命名规则：


        命名只能使用英文字母，数字和下划线，首个字符不能以数字开头。

        中间不能有空格，可以使用下划线（_）。
        
        不能使用标点符号。
        
        不能使用bash里的关键字（可用help命令查看保留关键字）

    **注意，变量名和等号之间不能有空格**

