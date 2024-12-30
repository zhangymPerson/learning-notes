" ================================================================
" 编码设置
" ================================================================
" 设置 vim 内部默认编码
set encoding=utf-8
" 设置编辑文件时的编码
set fileencoding=utf-8
" 设置 vim 能识别的编码
set fileencodings=ucs-bom,utf-8,cp936,gb18030,gb2312,big5,cuc-jp,cuc-kr,latin
" 设置终端模式（非 GUI 模式）下的编码
set termencoding=utf-8
" 防止特殊符号无法显示
set ambiwidth=double

" ================================================================
" 基本设置
" ================================================================
" 可以让你在 vim 编辑时使用鼠标进行操作
set mouse=a
" 显示普通模式未完成的指令 | 一般在右下角
set showcmd
" 解决插入模式下删除键不能删除的问题
set backspace=indent,eol,start
" 命令模式按下 Tab 键, 展示候选词
set wildmenu
" 打通系统 cv 和 vim
" 系统剪切板 -> vim
set clipboard=unnamedplus
" vim -> 系统剪切板
set clipboard=unnamed
" 解决插入模式 -> 普通模式延迟显示的问题
set ttimeout ttimeoutlen=10
" 位置标识记录 | 关闭文件后再次打开, 光标会回到你上一次离开的位置
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

" 可以令屏幕滚动时在光标上下方保留5行预览代码（也就是光标会在第5行触发向上滚动，或者在倒数第5行触发向下滚动）。
set so=5

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

" ================================================================
" 搜索匹配
" ================================================================
" 高亮显示匹配到的括号
set showmatch
" 高亮显示搜索到的关键字
set hlsearch
" 即时搜索 | 即边搜边高亮
set incsearch
" 智能大小敏感, 若有字母大写, 敏感, 否则不敏感
set ignorecase smartcase

" 显示命令
set showcmd

" 回车键 解决插入模式下删除键不能删除的问题
set backspace=indent,eol,start

" 折叠方式
set foldmethod=syntax
" 默认打开折叠层次
set foldlevel=3

" 剪切板
set clipboard^=unnamed,unnamedplus

" 输入模式下的 快捷键配置
imap <C-e> <END>
imap <C-a> <HOME>
" imap ll <Right>
" imap hh <Left>
" imap jj <Down>
" imap kk <Up>

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
" set relativenumber

" 行的配置
set nu
set cursorline
set cursorcolumn

" 禁用 vim 使用过程中的铃声
set noerrorbells visualbell t_vb=

" vim 中 使用 :find *a* 查找当前目录下 文件名包含 a 的文件夹
" 递归查找子文件
set path+=**
" 展示match的文件列表
set wildmenu

" 关闭文件再重新打开时，无法撤回历史动作。以下配置可以实现持久化undo记录
set undofile 

" 自动检测文件类型和缩进格式, 并根据文件类型加载插件
filetype plugin indent on
" 文件被外部改动后, 自动加载
set autoread

" 配置你的undo保存路径 目录需要自己创建，并且有权限
set undodir=~/.vim/undodir
" 使用:x替代:wq，使用:qa替代每个窗口执行一次:q

" 常用的命令
" :sp：水平分屏。（split）
" :vs：垂直分屏。（vsplit）

" https://yianwillis.github.io/vimcdoc/doc/usr_29.html#29.3
" nmap [[ [m
" nmap ]] ]m

" zz: 将当前行移动到屏幕中央。
" zt: 将当前行移动到屏幕顶端。
" zb: 将当前行移动到屏幕底端o

" zc 折叠当前行 zo 打开当前折叠 zC 折叠代码段 zo 打开代码段
" zM 折叠整个文件 
" zR 打开所以折叠

" imap dd <backspace>
" imap oo <enter>

" 使用 . 高效执行一些重复的操作

" 括号自动匹配 ide 自带不需要开启
" inoremap ( ()<ESC>i
" inoremap [ []<ESC>i
" inoremap { {}<ESC>i
" inoremap < <><ESC>i
" inoremap " ""<ESC>i
" inoremap ' ''<ESC>i


" 插件安装
" 插件地址 https://github.com/junegunn/vim-plug
call plug#begin()

" List your plugins here
Plug 'tpope/vim-sensible'
Plug 'easymotion/vim-easymotion'
Plug 'justinmk/vim-sneak'
Plug 'preservim/nerdtree'
Plug 'tpope/vim-surround'

call plug#end()

map <F3> :NERDTreeMirror<CR>
map <F3> :NERDTreeToggle<CR>
