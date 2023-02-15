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

" zc 折叠当前行 zo 打开当前折叠 zC 折叠代码段 zo 打开代码段
" zM 折叠整个文件 
" zR 打开所以折叠
" 折叠方式
set foldmethod=syntax
" 默认打开折叠层次
set foldlevel=3

" 剪切板
set clipboard=unnamed

" 输入模式下的 快捷键配置
imap <C-e> <END>
imap <C-a> <HOME>
imap ll <Right>
imap hh <Left>
imap jj <Down>
imap kk <Up>
" imap dd <backspace>
" imap oo <enter>

" 括号自动匹配 ide 自带不需要开启
" inoremap ( ()<ESC>i
" inoremap [ []<ESC>i
" inoremap { {}<ESC>i
" inoremap < <><ESC>i
" inoremap " ""<ESC>i
" inoremap ' ''<ESC>i

" 代码联想 输入 sout + tab键 => System.out.println("")
ab sout System.out.println("")
ab key value

set completeopt=preview,menu

" 设置 leader 键为空格
" let mapleader=<SPACE>
let mapleader=" "

" 创建文件时 设置代码模板
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

" 在文件中插入时间的使用方式
" 在vim使用方式 输入 :call  InsertDate() 
function InsertDate()
    $delete
    read !date
endfunction

" https://yianwillis.github.io/vimcdoc/doc/usr_29.html#29.3
" nmap [[ [m
" nmap ]] ]m

" zz: 将当前行移动到屏幕中央。
" zt: 将当前行移动到屏幕顶端。
" zb: 将当前行移动到屏幕底端o

" 戒掉使用 上下左右移动文本的习惯
nnoremap <Left>  :echoe "Use h"<CR>
nnoremap <Right> :echoe "Use l"<CR>
nnoremap <Up>    :echoe "Use k"<CR>
nnoremap <Down>  :echoe "Use j"<CR>
" ...and in insert mode
" inoremap <Left>  <ESC>:echoe "Use h"<CR>
" inoremap <Right> <ESC>:echoe "Use l"<CR>
" inoremap <Up>    <ESC>:echoe "Use k"<CR>
" inoremap <Down>  <ESC>:echoe "Use j"<CR>

set hidden

" 显示上下相对行数
set relativenumber

" 禁用 vim 使用过程中的铃声
set noerrorbells visualbell t_vb=

" vim 中 使用 :find *a* 查找当前目录下 文件名包含 a 的文件夹
" 递归查找子文件
set path+=**
" 展示match的文件列表
set wildmenu

" 使用 . 高效执行一些重复的操作

" 关闭文件再重新打开时，无法撤回历史动作。以下配置可以实现持久化undo记录
set undofile 

" 配置你的undo保存路径 目录需要自己创建，并且有权限
set undodir=~/.vim/undodir
" 使用:x替代:wq，使用:qa替代每个窗口执行一次:q