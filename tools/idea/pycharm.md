# python 中使用 pycharm 开发

## 目录

- [返回](./README.md)

- python 中的注释

  File->settings->Editor->File and Code Templates->Python Script

  ```python
  #!/usr/bin/env python
  # -*- encoding: utf-8 -*-
  """
  @File    :   ${NAME}.py
  @Contact :   zhangyanmingjiayou@163.com

  @Modify Time      @Author    @Version    @Desciption
  ------------      -------    --------    -----------
  ${DATE} ${TIME}   danao      1.0         None
  """
  ```

- python 解释器 Configure Python Interpreter

  file - setting - Python Interpreter - 创建文件夹 - 如 venv 文件夹

- python 虚拟环境

  新版本的 Python 都自带一个 venv 模块，它可以很方便的管理我们的虚拟环境。

  比如我们有个项目叫 blog

  ```sh
  mkdir blog
  cd blog
  # 第一个venv是包名，第二个是创建虚环境名字
  python -m venv venv
  # linux进入虚拟环境
  source venv/bin/activate
  # venv/Scripts\activate.bat #windows进入虚拟环境
  ```

  ```sh
  #创建虚拟环境
  python3 -m venv .
  #激活虚拟环境
  #激活虚拟环境
  #还是在windows cmd下操作：
  #进入到Scripts,执行activate.bat，
  #Linux环境激活
  source bin/activate
  #退出环境
  deactivate
  ```
