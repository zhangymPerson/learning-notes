# python project 结构

> python 项目结构 打包 发布的简单介绍

## python 项目结构

- 常用的项目结构

  ```sh
  Python通用目录结构
  ProjectName
  │ readme 项目说明文档
  │ requirements.txt 存放依赖的外部Python包列表
  │ setup.py 安装、部署、打包的脚本
  ├─ bin 存放脚本，执行文件等
  │ └─ projectname
  ├─ docs 文档和配置
  │ └─ abc.rst
  │ └─ conf.py 配置文件
  └─ projectname 工程源码（包括源码、测试代码等）
  │ main.py 程序入口
  │ init.py
  └─ tests 测试代码
  └─ test_main.py
  └─ init.py

  ```

## python 打包工具 setuptools

- [工具文档](https://setuptools.readthedocs.io/en/latest/index.html#)

  核心 setup.py 文件 在文件所在目录下执行

  `python setup.py install`

  默认发布到本地

## 发布到 pip.python.com

- 发布官方渠道

  [官网地址](https://pypi.org/project/pip/)
