## windows下安装gvim

## 下载安装


## 配置文件


> 查看vim配置文件的方式 在vim下 执行 :version 即可查看

- 使用vim命令

    ```sh
    vim
    #查看配置文件所在位置
    :version
    ```
    配置文件所在位置
    ```
    系统 vimrc 文件: "$VIM\vimrc"
    用户 vimrc 文件: "$HOME\_vimrc"
    第二用户 vimrc 文件: "$HOME\vimfiles\vimrc"
    第三用户 vimrc 文件: "$VIM\_vimrc"
    用户 exrc 文件: "$HOME\_exrc"
    第二用户 exrc 文件: "$VIM\_exrc"
    ```

- 修改配置

    查看目录位置
    powershell下 
    ```sh    
    echo $HOME
    ```
    创建_vimrc文件作为自定义的配置文件

- 配置自定义的vim

    ```vim
    " 自动语法高亮
    syntax on 
    " 突出显示当前行
    set cursorline 
    " 设定 tab 长度为 4
    set tabstop=4 
    " 开启插件
    filetype plugin indent on 
    " 输入搜索内容时就显示搜索结果
    set incsearch 
    " 搜索时高亮显示被找到的文本
    set hlsearch 


    "中文编码支持
    set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
    set termencoding=utf-8
    set encoding=utf-8
    ""启用鼠标
    "set mouse=a
    "set selection=exclusive
    "set selectmode=mouse,key
    "
    "括号匹配
    set showmatch 
    "
    "设置自动缩进长度为4空格
    set shiftwidth=4
    "继承前一行的缩进方式，适用于多行注释
    ```