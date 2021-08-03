# 自定义的 vim 配置

- 配置如下

  ```vim
  "插入模式下移动位置
  imap <C-e> <END>
  imap <C-a> <HOME>
  imap ll <Right>
  imap hh <Left>
  syntax on "自动语法高亮
  set cursorline " 突出显示当前行
  set tabstop=4 " 设定 tab 长度为 4
  filetype plugin indent on " 开启插件
  set incsearch " 输入搜索内容时就显示搜索结果
  set hlsearch " 搜索时高亮显示被找到的文本

  "中文编码支持
  set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
  set termencoding=utf-8
  set encoding=utf-8
  "启用鼠标
  "set mouse=a
  "set selection=exclusive
  "set selectmode=mouse,key

  set showmatch "括号匹配

  "设置自动缩进长度为 4 空格
  set shiftwidth=4
  ```
