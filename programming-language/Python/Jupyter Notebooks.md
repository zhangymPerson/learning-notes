# Jupyter Notebooks

## 介绍

- [百度百科](https://baike.baidu.com/item/Jupyter/20423051?fr=aladdin)

- [jupyter官网](https://jupyter.org/)

## 安装使用

- pip 安装

    如果超时 可以添加 --default-time=1000 或者  修改远程源地址
    ```sh
    pip install jupyter
    ```

- 启动

    ```python
    #以当前目录为主 启动 访问地址 ： http://localhost:8888/tree
    jupyter notebook 
    ```

## 重要概念

- 工作目录

    jupyter notebook中有个叫做工作空间（工作目录）的概念，也就是说如果你想在哪个目录进行之后的工作，那就在哪个目录启动它。
    
    例如，这里我想将家目录的的jp_workspace目录作为工作空间，那我就需要进入到这个目录下。