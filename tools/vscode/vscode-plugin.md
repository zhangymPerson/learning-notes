# vscode 中常用的插件

- [返回](./README.md)

## 插件

- Chinese (Simplified) Language Pack for Visual Studio Code

- CodeBing

  查询插件 - 使用方式 alt + shift + f 或者控制台输入 Bing

- Git History

  git 日志查看插件 - 右键文件 选择 git history 即可

- **Git File History**

  git 文件修改历史查看便捷神器插件 直观查看 git 对文件的修改历史 使用方式 ctrl + shift + p 然后输入命令 Git File History 可以动态查看文件 git 提交记录

- **Git History Diff**

  git 文件查看插件，会在鼠标所在行显示修改历史

- **Prettier - Code formatter**

  代码格式化插件，最重要的是能格式化 markdown

- vscode-icons

  这个也是 vscode 官方提供的插件，作用是给 vscode 编辑的文件增加图标。这里再推荐一个相同功能的插件**vscode-icons-mac**，文件图标变成 Mac 风格，相当美观。

- vim 插件

  配置参考[vim 插件-github 地址](https://github.com/vscodevim/vim)

- 括号插件 Bracket Pair Colorizer

  这个插件的作用是给代码中的括号增加颜色，同一对括号是相同的颜色，尤其是在括号中还包着括号的时候，看起来更加的清晰。

- 路径自动补全 Path Intellisense

  这个插件的作用是当代码中读入文件名或者文件路径时，提供文件名或者文件路径的自动补全

- Beautify 代码美化

- [vscode-快捷键说明文档](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

- vscode 中制作流程图的插件 - Draw.io Integration

  [Draw.io](https://app.diagrams.net/)

  vscode 中安装插件之后，可以在本地进行相关图形的绘制

  如 [draw-png.drawio](./draw-png.drawio)

- [REST Client](https://github.com/Huachao/vscode-restclient) 类 postman 的接口测试工具

  postman 和 浏览器的 F12 可以直接导出能运行的 http 文件格式内容

  postman 选择 Code snippet 为 HTTP

  浏览器 单击 network 处的请求,选择 Copy -> copy request headers (复制请求头)

  http 测试工具插件测试 api.的插件通过文件来发现和测试 [测试文件](./restclient.http)

  配置多种测试环境的相关配置

  在.http 文件目录下 创建项目的 .vscode/.settings.json 配置文件，然后 配置举例如下

  ```json
  {
    "rest-client.environmentVariables": {
      "local": {
        "version": "v2",
        "host": "127.0.0.1:8080",
        "token": "token"
      },
      "prod": {
        "host": "http://host:port",
        "token": "token"
      }
    }
  }
  ```

  通过 F1 输入 Rest Client switch enviroment 选择要生效的环境配置

- vscode 自动代码提示补全插件工具

  TabNine 智能代码补全插件

  **Postfix Completion** (下称 Postfix) 是一种通过 . + 模板 Key 来对当前已经输出的表达式，添加和应用预设代码模板的编码增强能力。

  idea 自带的代码自动补全相关功能 vscode 需要搜索查询相关插件

  其核心要解决的问题是，将编码过程中一些通用的代码结构范式进行抽象和沉淀，并能在同类型的场景下，通过 . + 模板 Key 的方式进行唤醒和复用。

- vscode 错误信息在当前行显示的插件 error lens

  [github - error lens](https://github.com/usernamehw/vscode-error-lens)

- [vscode-翻译插件 search-online](https://github.com/Wscats/search-online)

  [中文使用说明](https://gitee.com/wscats/search-online/blob/master/README.CN.md)

- Paste JSON as Code 插件 - 代码转换 json 转代码 json 转 bean

  [github 地址](https://github.com/quicktype/quicktype)

  - 使用方式:

    - 首先创建 要生成的语言代码空文件 如: \*\*\*.java / \*\*\*.go

    - 复制要生成 bean 的 json 内容

    - 在创建的空文件打开页 按 F1 输入 Paste JSON as Code 输入顶层的类名 即可生成对应语言的 bean 对象结构

  [在线地址](https://quicktype.io/)

- local-history - 本地修改历史记录 防止修改被损坏

  安装插件 Local History

  注意 安装插件后，会在项目目录下生成 .history 文件夹

  git 中需要过滤下此文件夹

- Code Runner 代码直接执行插件

  修改配置 Code Runner 方式

  在 settings 中搜索 `code-runner.executorMap` 可以根据对应的语言修改其编译方式

  如在 c++ 中指定编译的标准库为 c++11 可以在 g++ 命令下添加 `-std=c++11` 参数

- autopep8 插件 python 格式化插件 python 插件不带格式化功能
