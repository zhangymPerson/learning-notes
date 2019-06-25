# vscode 笔记

- 插件

    Chinese (Simplified) Language Pack for Visual Studio Code

    CodeBing 查询插件 - 使用方式 alt + shift + f 或者控制台输入 Bing 

    Git History  git  日志查看插件 - 右键文件 选择git history 即可

    vscode-icons

    这个也是vscode官方提供的插件，作用是给vscode编辑的文件增加图标。这里再推荐一个相同功能的插件**vscode-icons-mac**，文件图标变成Mac风格，相当美观。

     vim插件     
     
     amVim 插件

     括号插件 Bracket Pair Colorizer  
     
     这个插件的作用是给代码中的括号增加颜色，同一对括号是相同的颜色，尤其是在括号中还包着括号的时候，看起来更加的清晰。

     路径自动补全 Path Intellisense  
     
     这个插件的作用是当代码中读入文件名或者文件路径时，提供文件名或者文件路径的自动补全
    
    Beautify 代码美化

- [vscode-快捷键说明文档](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

- 常用快捷键

```
    隐藏资源管理器(即文件目录列表)  
        ctrl + b

    快速打开终端和调试窗口  
        ctrl + ` (Esc键下面那个键)

    选中多行  
        按住Alt键点击左键 多选  或者 Alt+Shift键 鼠标左键上下移动多选

    快速查询 替换
        ctrl + f / ctrl + h  (可以进行正则查询替换)

    查看搜索打开目录下的所有的文件
        ctrl+p


    打开控制台
        ctrl+shift+p或者 F1 

```

- 自动换行


文件  -> 首选项 -> 设置 -> 编辑器- > 找到控制折行方式。
    
    可以选择： 
    - "off" （禁用折行），
    - "on" （视区折行）， 
    - "wordWrapColumn"（在"editor.wordWrapColumn"处折行）
    - "bounded"（在视区与"editor.wordWrapColumn"两者的较小者处折行）。
    "editor.wordWrap": "off",

-  配置VS code显示方式 (空格和table的显示方式)

    editor.renderWhitespace : all


- 配置阿里普惠体 

    Alibaba Sans

    Alibaba Sans, 'Courier New', monospace



###  vscode的远程连接方式

- 插件下载

    Remote Development

    Visual Studio Code Remote 允许开发者将容器，远程计算机，或 Windows Subsystem for Linux (WSL) 作为完整的开发环境。


- 配置相关参数
    
    ~\.ssh\config
    ```
    Host Person
        HostName host
        User     root
    ````

    配置文件后，将ssh的公钥复制到要连接的服务器中

    然后连接

