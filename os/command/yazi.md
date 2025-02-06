# yazi 使用

- [github](https://github.com/sxyazi/yazi)

## 与 `ranger` 类似的文件管理器

- 使用方式

  `yazi`

- 操作方式与 vim 类似

- 快捷键

  | 快捷键 | 功能                                                              |
  | ------ | ----------------------------------------------------------------- | --- |
  | ~      | 显示帮助菜单(在 tmux 中显示有问题)                                |
  | q      | 退出                                                              |
  | .      | 显示隐藏文件                                                      |
  | /      | 搜索文件                                                          |
  | s      | 搜索文件 通过 [fd](https://github.com/sharkdp/fd)                 |
  | S      | 搜索文件 通过 [fzf](https://github.com/junegunn/fzf)              |
  | c      | `cc` 复制文件路径 `cd` 复制目录 `cf` 文件名 ...                   |
  | ,      | 文件排序 `,m` 修改时间 `,c` 创建时间 `,a` 字母顺序 ...            |     |
  | z      | 跳转到使用 [zoxide](https://github.com/ajeetdsouza/zoxide) 的目录 |
  | Z      | 使用 [fzf](https://github.com/junegunn/fzf) 跳转到目录或显示文件  |
  | t      | 多标签                                                            |
  | ctrl+c | 关闭标签                                                          |

- 配置修改

  配置文件位置：`~/.config/yazi/*.toml`

  默认的文件夹颜色是蓝色，需要修改配置文件 `~/.config/yazi/theme.toml`

  ```toml
  [filetype]
  rules = [
          # Fallback
          # { name = "*", fg = "white" },
          { name = "*/", fg = "green" }
  ]
  ```
