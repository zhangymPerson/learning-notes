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

## 常见问题

- 修改部分配置 乱码问题

  .vimrc（在 win 中是\_vimrc）

  windows 下是在 gvim 启动文件夹位置的上一层

- vim 中的查询

  在 vim 和 vim 插件中均可使用。按 `F3` 可以打开搜索框

- vim 中取消高亮

  `:noh`

- vim 中插入模式下的快捷键 shell 中也可使用

  | 按键操作 | 用途                       |
  | -------- | -------------------------- |
  | `<C-h>`  | 删除前一个字符（同退格键） |
  | `<C-w>`  | 删除前一个单词             |
  | `<C-u>`  | >删至行首                  |

- vim 粘贴错乱问题

  运行如下命令，进入 paste 模式：
  `:set paste`
  进入 paste 模式后，按 i 键进入插入模式，然后再粘帖，文本格式不会错乱了。但粘帖后还需要按 `<ESC>` 进入普通模式并执行如下命令结束 paste 模式：

  `:set nopaste`

- vim 多行操作 vim 列式操作

  选中多行

  `ctrl + Shift + v`

## 各个 shell 启动 vim 模式的配置

- bash 下启动 vim 模式

  `set -o vi`

- zsh 下启动 vim 模式

  zsh 通过 `vi-mode` 插件来实现 vim 模式
