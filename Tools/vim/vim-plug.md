# vim 的插件使用

## 首先安装一个 vim 插件管理器

- vim-plug 安装

  > 特别注意:vim-plug 将 plug.vim 拷贝到文件夹下之后，必须改 .vimrc 文件配置 加入配置才能使用相关命令

  [github 地址](https://github.com/junegunn/vim-plug)

  安装命令

  `curl -fLo ~/.vim/autoload/plug.vim --create-dirs \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim`

  如遇网络问题无法执行上述命令安装时可以使用以下办法

  `mkdir ~/.vim/autoload/`

  `vim plug.vim`

  将 github 项目中的`plug.vim`文件的内容直接复制进去

  **复制时，注意格式要正确**

- vim-plug 使用

  在 `~/` 目录下 创建 `.vimrc` 文件

  编写要添加的插件 格式如下

  **先配置插件，然后在安装插件，命令需要在 vim 中执行，先打开 vim 编辑器**

  插件安装位置可以自己定义 如 `'~/.vim/plugged'`

  ```vim
  call plug#begin('~/.vim/plugged')
  "可以在此处添加多个插件
  Plug 'itchyny/lightline.vim'
  call plug#end()
  ```

  然后打开`vim` 执行以下命令

  - 状态查看

    `:PlugStatus` 检查现在 plug 负责的插件状态

  - 安装

    `:PlugInstall` 安装配置好的插件

  - 更新

    `:PlugUpdate` 更新已安装的插件

  - 清理

    `:PlugClean` 清理插件，需要现在 .vimrc 里面删除或注释掉

  - 升级

    `:PlugUpgrade` 升级自身

- nerdtree 插件的安装

  [github 地址](https://github.com/preservim/nerdtree)

  基于 vim-plug 配置

  ```vim
  call plug#begin()
  "添加下面这句配置
  Plug 'preservim/nerdtree'
  call plug#end()
  ```

  然后 vim 下执行 `:PlugInstall`命令初始化即可

  测试安装是否成功

  `vim file` 后 执行 `:NERDTreeToggle` 如果打开了目录说明安装成功
