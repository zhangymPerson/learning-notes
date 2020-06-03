# emacs简单使用


- **[emacs国内社区](https://emacs-china.org/)**

## 常用体验

- 打开退出

    ```sh
    #打开文件
    emacs filename
    #退出 
    # windows 下 ctrl + x ctrl + c 
    ```

- 移动

    ```sh
    #向下移动
    ctrl + v 
    # 向上移动 alt 在xshell中需要配置
    # File => Properties => Terminal => Keyboard => Use ALT key as Meta key
    alt + v 
    # 移动当前行到屏幕中间
    ctrl + l
    
    # n next 下一行 p previous 上一行 b backward 回退 f forward 前进
    #下一行
    ctrl + n
    #上一行
    ctrl + p
    # 向前
    ctrl + b
    #向后
    ctrl + f
    ```

- 失去响应

    ctrl + g 终止一条执行时间太长得命令

- backspace在linux终端中得问题 被映射成 ctrl + h

    在~/.emacs中添加下面两句话：
    ```emacs
    (global-set-key "\C-h" 'backward-delete-char-untabify)  
    (global-set-key "\d" 'delete-char)  
    ```