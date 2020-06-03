## windows下使用Emacs

#### 卡顿，中文字符

- 修改字体 - 在 `Options` 下配置 `Set Default Font` 设置为宋体

- 修改完可能解决部分问题

#### 生成配置文件

- 利用 `emacs` 创建 `.emacs.d` 文件夹和 `.emacs` 文件
   
- 启动 `emacs` ，用鼠标点击 `Options` 菜单，随便点击一两个选项，比方点击一下 `Active Region Highlighting` ，
    
-   然后点击 `Save Options` 。
   
- 操作目的是让emacs自己主动创建.emacs.d文件夹以及.emacs文件！
    
- **观察你的Emacs窗体最后一行，是否显示 `Wrote ~/emacs/.emacs` 假设是的话就对了，当你选择 `Save Options` 的时候，`Emacs` 会在 `home` 路径下产生 `.emacs` 文件，并把配置信息写进这个文件。如今看看你的 `~/emacs/.emacs` 文件夹下是否产生了配置文件**

- windows卡顿，在 `.emacs` 配置文件中添加以下内容

    ```emacs
    ;; 禁止压缩字体 
    (setq inhibit-compacting-font-caches t)
    ```
    解决卡顿问题

