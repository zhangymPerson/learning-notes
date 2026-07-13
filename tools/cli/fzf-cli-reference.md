# fzf 命令参考文档

## 概览

**fzf** 是一个交互式模糊查找（filter）程序，可用于任意列表。它实现了「模糊匹配」算法，因此可以输入省略了某些字符的模式，仍然能快速找到想要的结果。

- **项目地址**：https://github.com/junegunn/fzf
- **作者**：Junegunn Choi <junegunn.c@gmail.com>
- **更多信息**：`fzf --man`（查看 man page）
- **用法**：`fzf [options]`

fzf 是**单命令工具**，没有传统意义上的「子命令树」，所有功能均通过命令行选项（options）实现。其选项按功能归类如下。

---

## 选项分类树

```
fzf [options]
├── SEARCH            搜索行为（模糊/精确、大小写、排序、作用字段）
├── INPUT/OUTPUT      输入输出处理（NUL 分隔、ANSI、同步）
├── GLOBAL STYLE      全局样式（配色、预设、加粗）
├── DISPLAY MODE      显示模式（高度、弹窗/--popup、tmux）
├── LAYOUT            布局（排版、边距、边框）
├── LIST SECTION      列表区域（多选、滚动、冻结列、滚动条等）
├── INPUT SECTION     输入区域（提示符、信息行、标签）
├── PREVIEW WINDOW    预览窗口（命令、窗口布局、边框）
├── HEADER            页眉（字符串、前 N 行、边框）
├── FOOTER            页脚（字符串、边框）
├── SCRIPTING         脚本模式（初始查询、自动选择、过滤）
├── KEY/EVENT BINDING 按键/事件绑定（--bind）
├── ADVANCED          高级（子进程 shell、HTTP 监听）
├── DIRECTORY TRAVERSAL 目录遍历（walker 系列，未设置 $FZF_DEFAULT_COMMAND 时生效）
├── HISTORY           历史记录（文件、大小）
├── SHELL INTEGRATION  shell 集成（bash/zsh/fish/nushell 脚本）
└── HELP              帮助（version / help / man）
```

---

## SEARCH（搜索）

| 选项                   | 说明                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------ |
| `-e, --exact`          | 启用精确匹配                                                                         |
| `+x, --no-extended`    | 禁用扩展搜索模式                                                                     |
| `-i, --ignore-case`    | 大小写不敏感匹配                                                                     |
| `+i, --no-ignore-case` | 大小写敏感匹配                                                                       |
| `--smart-case`         | 智能大小写匹配（默认）                                                               |
| `--scheme=SCHEME`      | 评分方案 `[default\|path\|history]`                                                  |
| `-n, --nth=N[,..]`     | 仅在这些字段索引内搜索（逗号分隔，整数或范围 `[BEGIN]..[END]`）                      |
| `--with-nth=N[,..]`    | 用字段表达式转换每行展示内容                                                         |
| `--accept-nth=N[,..]`  | 定义选中时打印哪些字段                                                               |
| `-d, --delimiter=STR`  | 字段分隔符正则（默认 AWK 风格）                                                      |
| `+s, --no-sort`        | 不排序结果                                                                           |
| `--literal`            | 不对拉丁字母做归一化                                                                 |
| `--tail=NUM`           | 内存中保留的最大条目数                                                               |
| `--disabled`           | 不执行搜索                                                                           |
| `--tiebreak=CRI[,..]`  | 分数相同时的排序标准 `[length\|chunk\|pathname\|begin\|end\|index]`（默认 `length`） |

---

## INPUT/OUTPUT（输入/输出）

| 选项       | 说明                            |
| ---------- | ------------------------------- |
| `--read0`  | 以 ASCII NUL 字符作为输入分隔符 |
| `--print0` | 以 ASCII NUL 字符打印输出       |
| `--ansi`   | 处理 ANSI 颜色码                |
| `--sync`   | 同步搜索，用于多阶段过滤        |

---

## GLOBAL STYLE（全局样式）

| 选项              | 说明                                                  |
| ----------------- | ----------------------------------------------------- |
| `--style=PRESET`  | 应用样式预设 `[default\|minimal\|full[:BORDER_STYLE]` |
| `--color=COLSPEC` | 基础配色方案及/或自定义颜色 `dark\|light\|base16\|bw` |
| `--no-color`      | 禁用颜色                                              |
| `--no-bold`       | 不使用加粗文本                                        |

---

## DISPLAY MODE（显示模式）

| 选项                       | 说明                                                                                                                                          |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `--height=[~][-]HEIGHT[%]` | 在光标下方以指定高度显示窗口而非全屏。负值 = 终端高度减该值；前缀 `~` 时按输入大小自动定高                                                    |
| `--min-height=HEIGHT[+]`   | `--height` 为百分比时的最小高度；加 `+` 会根据其他布局选项自动增大（默认 `10+`）                                                              |
| `--popup[=OPTS]`           | 在浮动窗格中启动（需 tmux 3.3+ 或 Zellij 0.44+）`[center\|top\|bottom\|left\|right][,SIZE[%]][,SIZE[%]][,border-native]`（默认 `center,50%`） |
| `--tmux[=OPTS]`            | `--popup` 的别名                                                                                                                              |

---

## LAYOUT（布局）

| 选项                     | 说明                                                                                                                                               |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--layout=LAYOUT`        | 布局：`[default\|reverse\|reverse-list]`                                                                                                           |
| `--margin=MARGIN`        | 屏幕外边距（TRBL \| TB,RL \| T,RL,B \| T,R,B,L）                                                                                                   |
| `--padding=PADDING`      | 边框内边距（同上格式）                                                                                                                             |
| `--border[=STYLE]`       | 绘制边框：`[rounded\|sharp\|bold\|block\|thinblock\|double\|dashed\|horizontal\|vertical\|top\|bottom\|left\|right\|line\|none]`（默认 `rounded`） |
| `--border-label=LABEL`   | 边框上打印的标签                                                                                                                                   |
| `--border-label-pos=COL` | 边框标签位置 `[正整数: 从左\|负整数: 从右][:bottom]`（默认 0 或居中）                                                                              |

---

## LIST SECTION（列表区域）

| 选项                      | 说明                                                   |
| ------------------------- | ------------------------------------------------------ |
| `-m, --multi[=MAX]`       | 启用多选（Tab / Shift-Tab），可限制最大数量            |
| `--highlight-line`        | 高亮整行                                               |
| `--cycle`                 | 循环滚动                                               |
| `--wrap[=MODE]`           | 行换行 `char\|word`（默认 `char`）                     |
| `--wrap-sign=STR`         | 换行行指示器                                           |
| `--no-multi-line`         | 使用 `--read0` 时禁用多行展示                          |
| `--raw`                   | 原始模式（显示不匹配项）                               |
| `--track`                 | 结果更新时跟踪当前选择                                 |
| `--id-nth=N[,..]`         | 定义跨重载操作的条目标识字段                           |
| `--tac`                   | 反转输入顺序                                           |
| `--gap[=N]`               | 每项之间渲染空行                                       |
| `--gap-line[=STR]`        | 每条空行处画水平分隔线（默认 `┈` 或 `-`）              |
| `--freeze-left=N`         | 左侧冻结列数                                           |
| `--freeze-right=N`        | 右侧冻结列数                                           |
| `--keep-right`            | 溢出时保持右端可见                                     |
| `--scroll-off=LINES`      | 滚到顶/底时上下保留的屏幕行数（默认 0）                |
| `--no-hscroll`            | 禁用水平滚动                                           |
| `--hscroll-off=COLS`      | 高亮子串右侧保留的屏幕列数（默认 10）                  |
| `--jump-labels=CHARS`     | jump 模式的标签字符                                    |
| `--gutter=CHAR`           | 边槽字符（默认 `▌`）                                   |
| `--gutter-raw=CHAR`       | 原始模式边槽字符（默认 `▖`）                           |
| `--pointer=STR`           | 当前行指针（默认 `▌` 或 `>`）                          |
| `--marker=STR`            | 多选标记（默认 `┃` 或 `>`）                            |
| `--marker-multi-line=STR` | 多行条目的多选标记（上/中/下 3 个字符，默认 `╻┃╹`）    |
| `--ellipsis=STR`          | 行截断时的省略符（默认 `··`）                          |
| `--tabstop=SPACES`        | Tab 字符宽度（默认 8）                                 |
| `--scrollbar[=C1[C2]]`    | 滚动条字符（分别用于列表与预览窗口）                   |
| `--no-scrollbar`          | 隐藏滚动条                                             |
| `--list-border[=STYLE]`   | 列表区域边框（同 `--border` 样式，默认 `rounded`）     |
| `--list-label=LABEL`      | 列表边框标签                                           |
| `--list-label-pos=COL`    | 列表标签位置（同 `--border-label-pos`，默认 0 或居中） |

---

## INPUT SECTION（输入区域）

| 选项                     | 说明                                                           |
| ------------------------ | -------------------------------------------------------------- |
| `--no-input`             | 禁用并隐藏输入区域                                             |
| `--prompt=STR`           | 输入提示符（默认 `> `）                                        |
| `--info=STYLE`           | 信息行样式 `[default\|right\|hidden\|inline[-right][:PREFIX]]` |
| `--info-command=COMMAND` | 生成信息行的命令                                               |
| `--separator=STR`        | 信息行分隔符（默认 `─` 或 `-`）                                |
| `--no-separator`         | 隐藏信息行分隔符                                               |
| `--ghost=TEXT`           | 输入为空时显示的占位文本                                       |
| `--filepath-word`        | 词级移动尊重路径分隔符                                         |
| `--input-border[=STYLE]` | 输入区域边框（同上样式，默认 `rounded`）                       |
| `--input-label=LABEL`    | 输入边框标签                                                   |
| `--input-label-pos=COL`  | 输入标签位置（默认 0 或居中）                                  |

---

## PREVIEW WINDOW（预览窗口）

| 选项                       | 说明                                                                                                                                                                                                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--preview=COMMAND`        | 预览高亮行的命令（`{}` 代表当前行）                                                                                                                                                                                                                              |
| `--preview-window=OPT`     | 预览窗口布局（默认 `right:50%`）。可组合：`[up\|down\|left\|right\|next][,SIZE[%]][,[no]wrap[-word]][,[no]cycle][,[no]follow][,[no]info][,[no]hidden][,border-STYLE][,+SCROLL[OFFSETS][/DENOM]][,~HEADER_LINES][,default][,<SIZE_THRESHOLD(ALTERNATIVE_LAYOUT)]` |
| `--preview-border[=STYLE]` | 等价于 `--preview-window=border-STYLE`（同上样式，默认 `rounded`）                                                                                                                                                                                               |
| `--preview-label=LABEL`    | 预览窗口标签                                                                                                                                                                                                                                                     |
| `--preview-label-pos=N`    | 预览标签位置（同 `--border-label-pos`）                                                                                                                                                                                                                          |
| `--preview-wrap-sign=STR`  | 预览窗口换行指示符                                                                                                                                                                                                                                               |

---

## HEADER（页眉）

| 选项                            | 说明                                                                             |
| ------------------------------- | -------------------------------------------------------------------------------- |
| `--header=STR`                  | 作为页眉的字符串                                                                 |
| `--header-lines=N`              | 输入的前 N 行作为页眉                                                            |
| `--header-first`                | 在提示符行之前打印页眉                                                           |
| `--header-border[=STYLE]`       | 页眉边框（同上样式 + `inline`，默认 `rounded`）                                  |
| `--header-lines-border[=STYLE]` | 为 `--header-lines` 的页眉单独绘制边框；`none` 仅分隔无边框；`inline` 嵌入列表框 |
| `--header-label=LABEL`          | 页眉边框标签                                                                     |
| `--header-label-pos=COL`        | 页眉标签位置（默认 0 或居中）                                                    |

---

## FOOTER（页脚）

| 选项                      | 说明                                         |
| ------------------------- | -------------------------------------------- |
| `--footer=STR`            | 作为页脚的字符串                             |
| `--footer-border[=STYLE]` | 页脚边框（同上样式 + `inline`，默认 `line`） |
| `--footer-label=LABEL`    | 页脚边框标签                                 |
| `--footer-label-pos=COL`  | 页脚标签位置（默认 0 或居中）                |

---

## SCRIPTING（脚本模式）

| 选项               | 说明                                      |
| ------------------ | ----------------------------------------- |
| `-q, --query=STR`  | 以指定查询启动 finder                     |
| `-1, --select-1`   | 仅有一项匹配时自动选择                    |
| `-0, --exit-0`     | 无匹配时立即退出                          |
| `-f, --filter=STR` | 打印初始查询的匹配项并退出（非交互）      |
| `--print-query`    | 将查询作为第一行打印                      |
| `--expect=KEYS`    | 逗号分隔的按键列表，完成 fzf 时输出对应键 |

---

## KEY/EVENT BINDING（按键/事件绑定）

| 选项              | 说明                                                                    |
| ----------------- | ----------------------------------------------------------------------- |
| `--bind=BINDINGS` | 自定义按键/事件绑定，例如 `--bind='ctrl-j:down,ctrl-k:up,enter:accept'` |

> `--bind` 支持大量动作（accept / abort / down / up / preview / execute / transform-* 等）与事件（focus / load / change / result 等），详情见 `fzf --man`。

---

## ADVANCED（高级）

| 选项                     | 说明                                                                  |
| ------------------------ | --------------------------------------------------------------------- |
| `--with-shell=STR`       | 启动子进程时使用的 shell 命令及参数                                   |
| `--listen[=[ADDR:]PORT]` | 启动 HTTP 服务器，通过 TCP 接收动作（远程执行需用 `--listen-unsafe`） |
| `--listen=SOCKET_PATH`   | 通过 Unix domain socket 启动 HTTP 服务器（路径以 `.sock` 结尾）       |

---

## DIRECTORY TRAVERSAL（目录遍历）

> 仅在未设置 `$FZF_DEFAULT_COMMAND` 时生效。

| 选项                      | 说明                                                          |
| ------------------------- | ------------------------------------------------------------- |
| `--walker=OPTS`           | `[file][,dir][,follow][,hidden]`（默认 `file,follow,hidden`） |
| `--walker-root=DIR [...]` | 遍历的根目录列表（默认 `.`）                                  |
| `--walker-skip=DIRS`      | 跳过的目录名（逗号分隔，默认 `.git,node_modules`）            |

---

## HISTORY（历史）

| 选项               | 说明                                               |
| ------------------ | -------------------------------------------------- |
| `--history=FILE`   | 存储 fzf 搜索历史的文件（**不是** shell 命令历史） |
| `--history-size=N` | 历史文件保留的最大条目数（默认 1000）              |

---

## SHELL INTEGRATION（Shell 集成）

| 选项        | 说明                        |
| ----------- | --------------------------- |
| `--bash`    | 打印设置 Bash 集成的脚本    |
| `--zsh`     | 打印设置 Zsh 集成的脚本     |
| `--fish`    | 打印设置 Fish 集成的脚本    |
| `--nushell` | 打印设置 Nushell 集成的脚本 |

---

## HELP（帮助）

| 选项        | 说明               |
| ----------- | ------------------ |
| `--version` | 显示版本信息并退出 |
| `--help`    | 显示帮助信息       |
| `--man`     | 显示 man page      |

---

## 环境变量

| 变量                    | 说明                                                           |
| ----------------------- | -------------------------------------------------------------- |
| `FZF_DEFAULT_COMMAND`   | 输入为 tty 时使用的默认命令（如 `find` / `fd` / `rg --files`） |
| `FZF_DEFAULT_OPTS`      | 默认选项（如 `--layout=reverse --info=inline`）                |
| `FZF_DEFAULT_OPTS_FILE` | 读取默认选项的文件路径                                         |
| `FZF_API_KEY`           | HTTP 服务器（`--listen`）的 X-API-Key 头                       |

---

## 使用示例

### 基础管道过滤

```bash
# 从命令输出中模糊查找并选中
git branch | fzf

# 查找文件并用 vim 打开选中的文件
vim $(fzf)
```

### 设置默认文件源

```bash
# 用 fd 作为默认来源（需在 shell 配置中设置）
export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow --exclude .git'
```

### 预览窗口

```bash
# 右侧预览文件内容，高亮当前行
fzf --preview 'bat --color=always --line-range :500 {}'

# 预览图片（配合 ueberzug 等）
fzf --preview 'scope.sh {}'
```

### 布局与样式

```bash
# 底部显示、内联信息、圆角边框
fzf --layout=reverse --info=inline --border --prompt='🔍 '

# 自定义高度（屏幕的 40%）
fzf --height=40%

# 浮动弹窗（tmux / zellij）
fzf --tmux center,60%
```

### 多选

```bash
# 多选后用 xargs 批量处理
fzf --multi | xargs -d '\n' rm -v
```

### 脚本/批处理模式（非交互）

```bash
# 打印匹配项并退出（不进入交互界面）
fzf --filter='foo'

# 仅一项匹配时自动选择；无匹配立即退出
fzf --select-1 --exit-0

# 返回触发完成的按键
fzf --expect=ctrl-v,ctrl-t,ctrl-x
```

### 自定义按键绑定

```bash
# Ctrl-j/k 上下移动，Ctrl-/ 切换预览
fzf --bind='ctrl-j:down,ctrl-k:up,ctrl-/:toggle-preview'
```

### Shell 集成安装

```bash
# 将对应脚本写入 shell 配置后，可获得 ** 触发补全、CTRL-T / CTRL-R 等增强
eval "$(fzf --bash)"
eval "$(fzf --zsh)"
```

---

## 小贴士

- 默认大小写策略为 `--smart-case`：查询含大写时大小写敏感，全小写时忽略大小写。
- 扩展搜索模式支持 `^` 前缀、`$` 后缀、`!` 取反、`|` 或运算等，可用 `+x` 关闭。
- 常用选项建议写入 `FZF_DEFAULT_OPTS` 或 `FZF_DEFAULT_OPTS_FILE`，避免每次重复输入。
- 想要完整、权威的说明（含 `--bind` 动作、事件、配色细节），运行 `fzf --man`。
