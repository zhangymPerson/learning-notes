# apidoc 在项目中使用方式

> apidoc 基于注释，所以不受编程语言的影响。

## 引入步骤

- 下载该项目

    [readme.md](./README.md)

- 创建项目/或者原有项目

    ```sh
    # 创建项目
    mkdir app
    # 进入项目目录
    cd app/
    # 创建src 目录
    mkdir src
    # 创建 apidoc 所需的配置文档
    vim apidoc.json
    ```

- apidoc.json 配置项说明

    name：项目名称

    version：项目版本

    description：项目介绍

    title：浏览器显示的标题内容

    url：接口前缀，比如http://www.niyueling.cn
