## windows 下使用 Emacs

#### 卡顿，中文字符

- 修改字体 - 在 `Options` 下配置 `Set Default Font` 设置为宋体

- 修改完可能解决部分问题

#### 生成配置文件

- 利用 `emacs` 创建 `.emacs.d` 文件夹和 `.emacs` 文件
- 启动 `emacs` ，用鼠标点击 `Options` 菜单，随便点击一两个选项，比方点击一下 `Active Region Highlighting` ，
- 然后点击 `Save Options` 。

- 操作目的是让 emacs 自己主动创建.emacs.d 文件夹以及.emacs 文件！
- **观察你的 Emacs 窗体最后一行，是否显示 `Wrote ~/emacs/.emacs` 假设是的话就对了，当你选择 `Save Options` 的时候，`Emacs` 会在 `home` 路径下产生 `.emacs` 文件，并把配置信息写进这个文件。如今看看你的 `~/emacs/.emacs` 文件夹下是否产生了配置文件**

- windows 卡顿，在 `.emacs` 配置文件中添加以下内容

  ```emacs
  ;; 禁止压缩字体
  (setq inhibit-compacting-font-caches t)
  ```

  解决卡顿问题

### emacs 的配置文件说明

- .emacs 是在主目录$HOME下；init.el是在主目录$HOME/.emacs.d/init.el。

    即$HOME/.emacs等价于$HOME/.emacs.d/init.el;
- init.el 相比.emacs，在目录安排上更舒服一些。
- .emacs 比 init.el 优先级更高。

### 常用快捷键

- 基本操作

  ```sh
  # 打开/新建文件
  Ctrl-x Ctrl-f
  # 保存当前缓冲区
  Ctrl-x Ctrl-s
  # 当前缓冲区另存为
  Ctrl-x Ctrl-w
  # 关闭当前Buffer并打开新文件
  Ctrl-x Ctrl-v
  # 光标处插入文件
  Ctrl-x i
  # 切换Buffer
  Ctrl-x b
  # 显示Buffer列表
  Ctrl-x Ctrl-b
  # 关闭当前Buffer
  Ctrl-x k
  # 关闭EmacsCtrl-c Ctrl-z     终止shell中的进程
  Ctrl-x Ctrl-c
  ```

- 窗口操作
  ```sh
  # 水平分割窗格
  Ctrl-x 2
  # 垂直分割窗格
  Ctrl-x 3
  # 关闭当前窗口
  Ctrl-x 0
  # 切换窗口
  Ctrl-x o
  # 关闭其他窗口
  Ctrl-x 1
  # 新建窗口
  Ctrl-x 5 2
  # 新窗口中打开文件
  Ctrl-x 5 f
  ```
- 光标移动操作
  ```sh
  # 前进一个字符
  Ctrl-f
  # 后退一个字符
  Ctrl-b
  # 上一行
  Ctrl-p
  # 下一行
  Ctrl-n
  # 前进一个单词
  Alt-f
  #  后退一个单词
  Alt-b
  # 行首
  Ctrl-a
  # 行尾
  Ctrl-e
  # 下翻一页
  Ctrl-v
  # 上翻一页
  Alt-v
  # 文件头
  Alt-<
  # 文件尾
  Alt->
  ```
- 编辑操作
  ```sh
  # 设置开始标记
  Ctrl-Space
  # 设置开始标记(Ctrl-space可能被操作系统拦截)
  Ctrl-@
  # 复制标记区内容
  Alt-w
  #  帖粘
  Ctrl-y
  # 使光标处的单词大写
  Alt-u
  # 使光标处的单词小写
  Alt-l
  # 使光标处单词首字母大写
  Alt-c
  # 删除一行
  Ctrl-k
  ```
- 搜索/替换操作
  ```sh
  # 向下搜索
  Ctrl-s 
  # 向上搜索
  Ctrl-r 
  # 替换
  #-space/y     替换当前匹配
  #-Del/n不要替换当前匹配
  #-.      仅替换当前匹配并退出
  #-,      替换并暂停(按space或y继续)
  #-!      替换所有匹配
  #-   ^     回到上一个匹配位置
  #-   return/q    退出替换
  Alt-%        
  ```
- 撤销操作（undo tree 模式的使用）
  ```sh
  Ctrl-x u         撤销操作进入undo-tree-visualizer-mode
  p n 上下移动，
  b f 在分支之前，左右切换
  t   显示时间戳
  q   退出
  ```
