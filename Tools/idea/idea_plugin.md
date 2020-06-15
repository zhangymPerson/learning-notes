## idea-plug 笔记

### vim 插件

- 名称 ideaVim

- 安装

  点击 File > settings - > plugins > 搜索 vim > IdeaVim

- 配置

  用户目录下添加配置文件
  C:\Users\Administrator

  创建 .ideavimrc 文件

  不能直接创建.\*\*的文件 可以 cmd / powershell

  windows 下 配置文件 .ideavimrc 和 \_ideavimrc 均可

  ```sh
  echo a > .ideavimrc
  ```

### lombok plug 安装

- idea 使用 lombak

  在插件中查找该插件并安装 lombok

  重启 idea

  安装完成后需要配置,在配置 setting 中查找

  **Annotation Processors** -> **Enable annotation processing** 是否勾选 为勾选需要勾选
