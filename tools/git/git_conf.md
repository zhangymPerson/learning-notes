# git 相关的 config 命令

- gitconfig 配置文件位置

  `vim ~/.gitconfig`

- 常用的 git config 命令

  ```sh
  #查看所有git config命令提示
  git config

  # 加global的为全局配置
  #配置用户名
  git config --global user.name <your name>

  #配置邮箱
  git config --global user.email <your_email@example.com>

  #查看所有的 key/value
  git config -l |--list

  git config --global push.default simple

  # windows下 git log 查看日志中文乱码问题
  git config --global core.quotepath false

  git config --global core.editor /usr/bin/vim

  git config --global credential.helper store

  git config --global credential.helper wincred

  #  设置大小写敏感，
  # windows下不区分大小写 修改文件名无提示和提交
  # 为了保持Mac/Win/Linux一致性
  # 使文件名大小写发生修改时，git可正常提交
  git config --global core.ignorecase false

  #查看配置 查看用户名 查看git用户信息
  git config --list
  ```

- git alias 配置 

  这样设置以后，直接运行 `git ck` 就和 `git checkout` 有一样的效果~
  `git config --global alias.ck checkout`

- git alias 开源项目 
  
  [gitalias](https://github.com/GitAlias/gitalias)
