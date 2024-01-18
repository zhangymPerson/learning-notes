# vim 中自定义配置

> Vim 会在许多地方查找 vimrc 文件（参见 :h vimrc ）。

- 在 UNIX 系统中，Vim 希望能找到路径为 ~/.vimrc 的文件。

- 在 Windows 系统中，理想的文件路径为 $HOME/\_vimrc。

  无论运行的是哪种系统，都可 以通过以下命令在 Vim 的内部打开该文件：

  ➾ `:edit $MYVIMRC`

  **$MYVIMRC** 是 Vim 的一个环境变量，它将被扩展为 vimrc 的文件路径。

  在完成针对 vimrc 文件的改动后， 可以通过以下命令为当前的 Vim 会话加载新的配置选项。

  ➾ `:source $MYVIMRC`

## vim 配置文件中的说明

### 自定义 vim 配置的方式

- 指定自定义的配置文件启动 vim

  注意:启动 vim 使用默认的 ~/.vimrc

  - 编写自定义相关的配置

  - 使用自定义的配置文件进行 vim 启动

    命令是 `vim -u ~/.selfvimrc filename`

    其中 -u 是指定自定义的 vim 自定义配置

    可以使用 alias 配置别称替换自己的配置文件启动 vim

### 配置说明

- 文件类型

  | 配置项                                                   | 说明                                                             | 备注 |
  | -------------------------------------------------------- | ---------------------------------------------------------------- | ---- |
  | set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936 | Vim 写入文件时采用的编码类型                                     |      |
  | set termencoding=utf-8                                   | 输出到终端时采用的编码类型                                       |      |
  | set encoding=utf-8                                       | 设置编码格式,encoding 选项用于缓存的文本、寄存器、Vim 脚本文件等 |      |

- 编辑器

  | 配置项                         | 说明                                                                     | 备注 |
  | ------------------------------ | ------------------------------------------------------------------------ | ---- |
  | set nu/set number              | 行号                                                                     |      |
  | set cursorline                 | 高亮当前行                                                               |      |
  | set cursorcolumn               | 高亮当前列                                                               |      |
  | set laststatus=2               | 0.不显式状态行<br/>1.仅当窗口多于一个时，显示状态行<br/>2.总是显式状态行 |      |
  | set statusline=                | 配置状态行显示信息                                                       |      |
  | set showmatch                  | 高亮显示匹配的括号                                                       |      |
  | set showcmd                    | 右下角显示输入的命令内容                                                 |      |
  | set backspace=indent,eol,start | 不设定在插入状态无法用退格键和 Delete 键删除回车符                       |      |

  注:`set statusline=%<%f%m\ %=\[%{&ff}:%{&fenc}:%Y]\ %{getcwd()}\ \ \[%{strftime('%Y-%b-%d\ %a\ %I:%M\ %p')}\]\ %=\ Line:%l\/%L\ Column:%c%V\ %P`

- 系统剪切板

  **注：查看 vim 是否支持`vim --version | grep "clipboard" `**

  | 配置项                | 说明   | 备注 |
  | --------------------- | ------ | ---- |
  | set clipboard=unnamed | 剪切板 |      |

- 查询相关

  | 配置项         | 说明                                       | 备注 |
  | -------------- | ------------------------------------------ | ---- |
  | set ignorecase | 设置默认进行大小写不敏感查找               |      |
  | set smartcase  | 如果有一个大写字母，则切换到大小写敏感查找 |      |
  | set incsearch  | 输入搜索内容时就显示搜索结果               |      |
  | set wrapscan   | 禁止在搜索到文件两端时重新搜索             |      |
  | set hlsearch   | 搜索高亮                                   |      |

- tab 缩进问题

  | 配置项                             | 说明                                     | 备注 |
  | ---------------------------------- | ---------------------------------------- | ---- |
  | set autoindent                     | 设置自动缩进，即每行的缩进同上一节相同。 |      |
  | set expandtab                      | 使用空格来替换 Tab                       |      |
  | set tabstop=4                      | 设置 Tab 键宽度为 4 个空格。             |      |
  | set shiftwidth=4                   | 设定 << 和 >> 命令移动时的宽度为 4       |      |
  | set softtabstop=4<br/>set smarttab | 使得按退格键时可以一次删除 4 个空格      |      |

- 鼠标启用

  | 配置项                                                               | 说明     | 备注 |
  | -------------------------------------------------------------------- | -------- | ---- |
  | set mouse=a<br/>set selection=exclusive<br/>set selectmode=mouse,key | 启动鼠标 |      |

- 折叠相关

  | 配置项                | 说明     | 备注 |
  | --------------------- | -------- | ---- |
  | set foldmethod=syntax | 启用折叠 |      |
  | set foldenable        | 开始折叠 |      |

  操作：za，打开或关闭当前折叠；zM，关闭所有折叠；zR，打开所有折叠

  indent 方式，vim 会自动利用缩进进行折叠，我们可以使用现成的折叠成果．

- 开发

  | 配置项    | 说明     | 备注 |
  | --------- | -------- | ---- |
  | syntax on | 语法高亮 |      |

  **注: `?`（按住 Shift + /）往上查找。 `q/` 查看查找历史，选中一项后回车可以重新查找。`q?` 查看向上查找历史。**

- 快捷键

  | 配置项              | 说明                       | 备注 |
  | ------------------- | -------------------------- | ---- |
  | imap <C-e> <END>    | 插入模式下 ctrl + e 到最后 |      |
  | imap <C-a> <HOME>   | 插入模式下 ctrl + a 到开始 |      |
  | imap ll <Right>     | 插入模式下 ll 右移         |      |
  | imap hh <Left>      | 插入模式下 hh 左移         |      |
  | imap jj<Down>       | 插入模式下 jj 下移         |      |
  | imap kk <Up>        | 插入模式下 kk 上移         |      |
  | imap dd <backspace> | 插入模式下 dd 回退         |      |
  | imap oo <enter>     | 插入模式下 oo 下一行       |      |
