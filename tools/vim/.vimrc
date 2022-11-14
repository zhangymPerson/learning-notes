" 编码
set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8
" 行的配置
set nu
set cursorline
set cursorcolumn
" 设置不自动换行
set nowrap
" Vim 编辑器里默认是不启用鼠标的，通过此设置即可启动鼠标。
set mouse=a
set selection=exclusive
set selectmode=mouse,key	
" 设置自动缩进，即每行的缩进同上一节相同。
set autoindent
" 显示状态行当前设置
set laststatus=2
set statusline=%<%f%m\ %=\[%{&ff}:%{&fenc}:%Y]\ %{getcwd()}\ \ \[%{strftime('%Y-%b-%d\ %a\ %I:%M\ %p')}\]\ %=\ Line:%l\/%L\ Column:%c%V\ %P
syntax on
" tab 设置
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set smarttab
" 搜索设置
set ignorecase
set smartcase
set incsearch
set wrapscan
set hlsearch
set showmatch
" 显示命令
set showcmd
" 回车键
set backspace=indent,eol,start
" 折叠 zi 打开关闭折叠  zv 查看此行 zm 关闭折叠 zM 关闭所有 zr 打开 zR 打开所有 zc 折叠当前行 zo 打开当前折叠 zd 删除折叠 zD 删除所有折叠
set foldmethod=syntax
" 剪切板
set clipboard=unnamed
" 快捷键配置
imap <C-e> <END>
imap <C-a> <HOME>
imap ll <Right>
imap hh <Left>
imap jj <Down>
imap kk <Up>
" imap dd <backspace>
" imap oo <enter>
"inoremap ( ()<ESC>i
"inoremap [ []<ESC>i
"inoremap { {}<ESC>i
"inoremap < <><ESC>i
"inoremap " ""<ESC>i
"inoremap ' ''<ESC>i
ab sout System.out.println("")
set completeopt=preview,menu
" 设置 leader 键为空格
let mapleader=" "

autocmd BufNewFile *.sh exec ":call SetShellTitle()"
func SetShellTitle()
	if expand("%:e") == 'sh'
        call setline(1,"#!/bin/env bash")
        call setline(2,"")
        call setline(3,"###########################################################")
        call setline(4,"# @file : ".expand("%"))
        call setline(5,"# @desc : 脚本执行方式 [bash ".expand("%").expand("]"))
        call setline(6,"#         脚本说明: ")
        call setline(7,"# @date : ".strftime("%Y-%m-%d %h:%M:%S"))
        call setline(8,"# @auth : test")
        call setline(9,"# @version : 1.0")
        call setline(10,"###########################################################")
	endif
endfunc
autocmd BufNewFile * normal G

" 使用方式 :call  InsertDate
function InsertDate()
    $delete
    read !date
endfunction




