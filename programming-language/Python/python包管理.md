# python 中的包管理命令 pip

- 查看版本 

    pip -V

- 查看已经安装包 

    pip list

- 源修改

    让python pip使用国内镜像
 
    国内源：

                清华：https://pypi.tuna.tsinghua.edu.cn/simple
                阿里云：http://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：http://pypi.hustunique.com/
                山东理工大学：http://pypi.sdutlinux.org/ 
                豆瓣：http://pypi.douban.com/simple/

            注意：新版ubuntu要求使用 https 源。
    临时使用：

        可以在使用 pip 的时候加参数 -i https://pypi.tuna.tsinghua.edu.cn/simple

        例如：
        
        pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider
        这样就会从清华这边的镜像去安装 pyspider 库。


        使用 豆瓣源 安装 robobrowser ：
        
        pip install robobrowser -i http://pypi.douban.com/simple/

- pip 学习

- python api查看 自带api查看工具命令

    ```shell
    #不是固定端口
     python -m pydoc -p 0

    #指定端口号启动
     python –m pydoc –p 1234
    ```