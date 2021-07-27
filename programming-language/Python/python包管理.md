# python 中的包管理命令 pip

- 查看版本

  pip -V

- 查看已经安装包

  pip list

- 源修改

  让 python pip 使用国内镜像

- 国内源：

  - 清华：<https://pypi.tuna.tsinghua.edu.cn/simple>
  - 阿里云：<http://mirrors.aliyun.com/pypi/simple/>
  - 中国科技大学 <https://pypi.mirrors.ustc.ed>- imple/
  - 华中理工大学：<http://pypi.hustunique.com/>
  - 山东理工大学：<http://pypi.sdutlinux.org/>
  - 豆瓣：<http://pypi.douban.com/simple/>

  - 注意：新版 ubuntu 要求使用 https 源。

- 临时使用：

  可以在使用 pip 的时候加参数 -i <https://pypi.tuna.tsinghua.edu.cn/simple>

  例如：

  `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider`
  这样就会从清华这边的镜像去安装 pyspider 库。

  使用 豆瓣源 安装 robobrowser ：

  `pip install robobrowser -i http://pypi.douban.com/simple/`

- pip 学习

- python api 查看 自带 api 查看工具命令

  ```shell
  #不是固定端口
   python -m pydoc -p 0

  #指定端口号启动
   python –m pydoc –p 1234
  ```

- 安装问题

  连接超时

  socket.timeout: The read operation timed out

  ```python
  #指定超时时长
  pip install *** --default-timeout=1000
  ```

- python 包的创建

  **包其实就是文件夹**，更确切的说，是一个包含 `init.py` 文件的文件夹。

  因此，如果我们想手动创建一个包，只需进行以下 2 步操作：

  1.新建一个文件夹，文件夹的名称就是新建包的包名；

  2.在该文件夹中，创建一个 **init**.py 文件（前后各有 2 个下划线‘\_’），该文件中可以不编写任何代码。当然，也可以编写一些 Python 初始化代码，则当有其它程序文件导入包时，会自动执行该文件中的代码。

- 包导入

  通过前面的学习我们知道，包其实本质上还是模块，因此导入模块的语法同样也适用于导入包。无论导入我们自定义的包，还是导入从他处下载的第三方包，导入方法可归结为以下 3 种：

  `import 包名[.模块名 [as 别名]]`
  `from 包名 import 模块名 [as 别名]`
  `from 包名.模块名 import 成员名 [as 别名]`
  用 [] 括起来的部分，是可选部分，即可以使用，也可以直接忽略。
