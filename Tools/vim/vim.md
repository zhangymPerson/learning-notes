# vim 的使用

## 常用命令

- [vim 中文使用文档-github](https://github.com/yianwillis/vimcdoc)

### 命令说明

- 各种模式切换

  - i 从当前位置进入光标前的位置编辑模式
  - I 进入行首
  - a 进入光标后的位置编辑模式
  - A 进入末尾
  - o 重新开启一行进入编辑模式
  - esc 推出编辑模式

- 到指定行

  - ngg/nG （跳转到文件第 n 行，无需回车）
  - :n （跳转到文件第 n 行，需要回车）
  - vim +n filename （在打开文件后，跳转到文件的第 n 行）

- 常用编辑命令

  - dd 删除 1 行 ndd 删除多行
  - yy 复制 p 粘贴
  - u 撤销
  - :w 保存
  - :w filename 另存为
  - :q 退出
  - :q! 强制退出
  - b 跳到上一个字 B 跳到上一个字，长跳
  - w 跳到下一个字首，按标点或单词分割 W 跳到下一个字首，长跳，如 end-of-line 被认为是一个字
  - e 跳到下一个字尾 E 跳到下一个字尾，长跳
  - D 删除到行末
  - x 删除当前字符
  - X 删除前一个字符
  - yy 复制一行
  - yw 复制一个字
  - y/Y 复制到行末
  - p 粘贴粘贴板的内容到当前行的下面
  - P 粘贴粘贴板的内容到当前行的上面

- 替换命令

  - :%s/old/new/g 搜索整个文件，将所有的 old 替换为 new
  - :%s/old/new/gc 搜索整个文件，将所有的 old 替换为 new，每次都要你确认是否替换

- vim 跳转

  - **gd 跳转到局部函数定义.**
  - gD 跳转到全局函数定义.
  - **g\* 向下搜索光标所在单词 ( 当光标在 'he' 会查找包含 'he' 的词).**
  - g# 向上搜索光标所在单词

- vim 代码折叠

  - **zc 折叠**
  - **zo 展开折叠**

- vim 操作多行的方法

  - vim 文件 #进入行模式 ctrl + v

- 上下移动图标

  - h j k l 或者 上下左右键盘

  - 输入 d 删除选中的内容

  - 输入 i 输入相关内容后 按 esc 退出键 会发现修改生效

- 全局删除匹配到的行

  - :g/pattern/d

- 删除第 1-10 行里的匹配到的行

  - :1,10g/pattern/d

- 删除不包含指定字符的行

  - :v/pattern/d #或 :g!/pattern/d

## vim 安装到 windows 在 cmd 下用 vim 命令启动

- 安装 gvim

- 将 gvim 启动位置配置到环境变量下

- 修改部分配置 乱码问题

.vimrc（在 win 中是\_vimrc）

windows 下是在 gvim 启动文件夹位置的上一层

```vim
"设置文件的代码形式 utf8
set encoding=utf-8
set termencoding=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf-8,chinese,cp936

"vim的菜单乱码解决
source $VIMRUNTIME/delmenu.vim
source $VIMRUNTIME/menu.vim

"vim提示信息乱码的解决
language messages zh_CN.utf-8
```

```vim
"colorscheme evening	"配色方案
colorscheme desert
set helplang=cn		"设置中文帮助
set history=500		"保留历史记录
set guifont=Monaco:h10	"设置字体为Monaco，大小10
set tabstop=4		"设置tab的跳数
set expandtab
set backspace=2 	"设置退格键可用
"set nu! 		"设置显示行号
set wrap 		"设置自动换行
"set nowrap 		"设置不自动换行
set linebreak 		"整词换行，与自动换行搭配使用
"set list 		"显示制表符
set autochdir 		"自动设置当前目录为正在编辑的目录
set hidden 		"自动隐藏没有保存的缓冲区，切换buffer时不给出保存当前buffer的提示
set scrolloff=5 	"在光标接近底端或顶端时，自动下滚或上滚
"Toggle Menu and Toolbar 	"隐藏菜单栏和工具栏
"set guioptions-=m
"set guioptions-=T
set showtabline=2 	"设置显是显示标签栏
set autoread 		"设置当文件在外部被修改，自动更新该文件
set mouse=a 		"设置在任何模式下鼠标都可用
set nobackup 		"设置不生成备份文件
"set go=				"不要图形按钮
set guioptions-=T           " 隐藏工具栏
"set guioptions-=m           " 隐藏菜单栏

"===========================
"查找/替换相关的设置
"===========================
set hlsearch "高亮显示查找结果
set incsearch "增量查找

"===========================
"状态栏的设置
"===========================
set statusline=[%F]%y%r%m%*%=[Line:%l/%L,Column:%c][%p%%] "显示文件名：总行数，总的字符数
set ruler "在编辑过程中，在右下角显示光标位置的状态行

"===========================
"代码设置
"===========================
syntax enable "打开语法高亮
syntax on "打开语法高亮
set showmatch "设置匹配模式，相当于括号匹配
set smartindent "智能对齐
"set shiftwidth=4 "换行时，交错使用4个空格
set autoindent "设置自动对齐
set ai! "设置自动缩进
"set cursorcolumn "启用光标列
set cursorline	"启用光标行
set guicursor+=a:blinkon0 "设置光标不闪烁
set fdm=indent "


"插件管理
set rtp+=$VIM\vimfiles\bundle\Vundle.vim\
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
"Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'kien/ctrlp.vim'
Plugin 'eshion/vim-sync'
call vundle#end()

" 关闭NERDTree快捷键
map <leader>t :NERDTreeToggle<CR>
" 显示行号
let NERDTreeShowLineNumbers=1
let NERDTreeAutoCenter=1
" 是否显示隐藏文件
let NERDTreeShowHidden=1
" 设置宽度
let NERDTreeWinSize=21
" 在终端启动vim时，共享NERDTree
let g:nerdtree_tabs_open_on_console_startup=1
" 忽略一下文件的显示
let NERDTreeIgnore=['\.pyc','\~$','\.swp']
" 显示书签列表
let NERDTreeShowBookmarks=1

```

- vim 中的查询

  在 vim 和 vim 插件中均可使用。按 `F3` 可以打开搜索框

- vim 中取消高亮

  `:noh`

- vim 中插入模式下的快捷键 shell 中也可使用

| 按键操作 | 用途                       |
| -------- | -------------------------- |
| <C-h>    | 删除前一个字符（同退格键） |
| <C-w>    | 删除前一个单词             |
| <C-u>    | >删至行首                  |
