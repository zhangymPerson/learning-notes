## idea-plug 笔记

### vim 插件

- 名称 ideaVim

- 安装

  点击 File > settings - > plugins > 搜索 vim > IdeaVim

- 配置

  ideavim 的快速打开配置文件

  在 idea 软件打开后，右下角有一个 vim 的图标，点击后，选择 `Open ~/.ideavimrc`

  即可在 idea 中打开 vim 的相关配置并进行相关的设置

  用户目录下添加配置文件
  C:\Users\Administrator

  创建 .ideavimrc 文件

  不能直接创建.\*\*的文件 可以 cmd / powershell

  windows 下 配置文件 .ideavimrc 和 \_ideavimrc 均可

  ```sh
  echo a > .ideavimrc
  ```

  **注意：修改vim配置要生效，需要重启idea**

  ```vim
  imap <C-e> <END>
  imap <C-a> <HOME>
  imap ll <Right>
  imap hh <Left>
  " 显示当前的模式
  set showmode
  " 共享系统粘贴板
  set clipboard=unnamed
  " 高亮显示查询结果
  set hlsearch
  " 查询不分大小写 小写全匹配，有一个大写则按照大小写规则匹配
  set ignorecase smartcase

  " 下面的配置只能在idea系列中生效
  " Leader默认的键盘位置是 \
  nnoremap <Leader>r :action Replace<CR>
  vnoremap <Leader>/ :action Find<CR>
  vnoremap <Leader>./ :action FindInPath<CR>
  nnoremap <Leader>/ :action Find<CR>
  nnoremap <Leader>./ :action FindInPath<CR>
  ```

### lombok plug 安装

- idea 使用 lombak

  在插件中查找该插件并安装 lombok

  重启 idea

  安装完成后需要配置,在配置 setting 中查找

  **Annotation Processors** -> **Enable annotation processing** 是否勾选 为勾选需要勾选

### 查看 controller 中 RequestMapping 的插件 Request mapper

- idea 插件地址

  快速查看项目中后台路由 如 "/boot/hello/word"

  https://plugins.jetbrains.com/plugin/9567-request-mapper

- 插件安装后使用快捷键为

  `ctrl + shift + \`
