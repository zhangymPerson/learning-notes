# task 命令参考文档

## 概览

**task** 是 [go-task](https://github.com/go-task/task) 的命令行入口，一个简单轻量的任务运行器（task runner）。它读取当前目录（或指定目录）下的 `Taskfile.yml` / `Taskfile.yaml`，按声明执行任务。可类比 Make，但用 YAML 定义、跨平台、无需编译。

- **项目地址**：https://github.com/go-task/task
- **当前版本**：3.52.0
- **用法**：`task [flags...] [task...]`

如果不指定任务名，则回退到 `default` 任务；如果指定的任务名不存在，则列出所有任务。

**task 是「单命令工具」**：它没有传统意义上的「子命令树」，所有功能均通过命令行选项（flags）实现，任务名是用户在自己 Taskfile 中定义的。其选项按功能归类如下。

---

## 选项分类树

```
task [flags...] [task...]
├── TASK EXECUTION   任务执行（运行、强制、干跑、状态、摘要、静默/详细）
├── OUTPUT           输出样式（interleaved/group/prefixed 及分组模板）
├── PARALLEL/WATCH   并行与监听（并行、fail-fast、并发数、watch、interval）
├── LISTING          任务列表（list / list-all / json / 排序 / 模糊匹配）
├── CONFIG           配置与路径（dir / taskfile / temp-dir / global）
├── INTERACTIVE      交互与确认（interactive 变量提示 / yes 自动确认）
├── ENVIRONMENT      环境（color / insecure / 实验特性）
└── HELP             帮助与信息（help / version / completion / experiments / init）
```

---

## TASK EXECUTION（任务执行）

| 选项              | 说明                                                                                                  |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| `[task...]`       | 位置参数，指定要运行的任务名；可同时传多个。不传则用 `default` 任务；传入不存在的任务名则列出所有任务 |
| `-f, --force`     | 即使任务已是最新（up-to-date）也强制执行                                                              |
| `-n, --dry`       | 编译并按任务将要执行的顺序打印出来，但不真正执行（dry run）                                           |
| `--status`        | 若有任一给定任务不是最新状态，以非零退出码退出（用于 CI 中判断是否需要重建）                          |
| `--summary`       | 显示某个任务的摘要信息（依赖、命令数等）                                                              |
| `-s, --silent`    | 关闭命令回显（不打印将要执行的命令本身）                                                              |
| `-v, --verbose`   | 启用详细模式，输出更丰富的过程信息                                                                    |
| `-x, --exit-code` | 透传任务命令的退出码（而非 task 自身的退出码）                                                        |

---

## OUTPUT（输出样式）

| 选项                          | 说明                                                                                                           |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `-o, --output string`         | 设置输出样式：`interleaved`（交错，默认）\| `group`（分组，任务结束后一次性输出）\| `prefixed`（带任务名前缀） |
| `--output-group-begin string` | `group` 模式下，在某任务分组输出**之前**打印的消息模板                                                         |
| `--output-group-end string`   | `group` 模式下，在某任务分组输出**之后**打印的消息模板                                                         |
| `--output-group-error-only`   | `group` 模式下仅显示失败任务的输出，吞掉成功任务的输出                                                         |

---

## PARALLEL / WATCH（并行与监听）

| 选项                      | 说明                                              |
| ------------------------- | ------------------------------------------------- |
| `-p, --parallel`          | 将命令行传入的多个任务**并行**执行                |
| `-F, --failfast`          | 并行运行任务时，一旦有任务失败就立即停止其余任务  |
| `-C, --concurrency int`   | 限制同时运行的任务并发数                          |
| `-w, --watch`             | 监听给定任务，文件变化时自动重新执行              |
| `-I, --interval duration` | 配合 `--watch` 使用的轮询间隔（如 `1s`、`500ms`） |

---

## LISTING（任务列表）

| 选项              | 说明                                                            |
| ----------------- | --------------------------------------------------------------- |
| `-l, --list`      | 列出当前 Taskfile 中**带描述**的任务                            |
| `-a, --list-all`  | 列出所有任务（无论是否带描述）                                  |
| `-j, --json`      | 以 JSON 格式输出任务列表（便于脚本解析）                        |
| `--nested`        | 以 JSON 输出时，将命名空间（namespace）嵌套展示                 |
| `--no-status`     | 以 JSON 输出时，忽略各任务的状态字段                            |
| `--sort string`   | 改变列出任务时的排序方式：`default` \| `alphanumeric` \| `none` |
| `--disable-fuzzy` | 关闭任务名的模糊匹配（输入任务名时必须完全精确）                |

---

## CONFIG（配置与路径）

| 选项                    | 说明                                                                         |
| ----------------------- | ---------------------------------------------------------------------------- |
| `-d, --dir string`      | 设置 task 执行并寻找 Taskfile 的目录                                         |
| `-t, --taskfile string` | 指定要运行的 Taskfile 文件名（默认 `Taskfile.yml`）                          |
| `--temp-dir string`     | 设置 task 存放临时文件（如校验和 checksum）的目录；相对路径相对于根 Taskfile |
| `-g, --global`          | 运行全局 Taskfile，路径为 `$HOME/{T,t}askfile.{yml,yaml}`                    |

---

## INTERACTIVE（交互与确认）

| 选项            | 说明                                            |
| --------------- | ----------------------------------------------- |
| `--interactive` | 当必填变量缺失时，交互式提示用户输入            |
| `-y, --yes`     | 对所有提示一律回答「yes」（非交互环境自动确认） |

---

## ENVIRONMENT（环境）

| 选项            | 说明                                                        |
| --------------- | ----------------------------------------------------------- |
| `-c, --color`   | 彩色输出，默认开启。设为 `false` 或设置 `NO_COLOR=1` 可关闭 |
| `--insecure`    | 强制 task 通过不安全连接下载远程 Taskfile                   |
| `--experiments` | 列出所有可用的实验特性及其开启状态                          |

---

## HELP（帮助与信息）

| 选项                  | 说明                                                    |
| --------------------- | ------------------------------------------------------- |
| `-h, --help`          | 显示 task 用法                                          |
| `--version`           | 显示 task 版本                                          |
| `--completion string` | 生成指定 shell 的补全脚本（如 `bash` / `zsh` / `fish`） |
| `-i, --init`          | 在当前目录创建一个新的 `Taskfile.yml` 模板              |

---

## 实验特性（--experiments）

当前版本（3.52.0）内置以下实验特性，默认均关闭：

| 特性名             | 状态 | 说明                        |
| ------------------ | ---- | --------------------------- |
| `GENTLE_FORCE`     | off  | 更温和的 `--force` 语义     |
| `REMOTE_TASKFILES` | off  | 支持下载并运行远程 Taskfile |
| `ENV_PRECEDENCE`   | off  | 调整环境变量优先级          |

开启方式（环境变量，值取 `1` / `true`）：

```bash
export TASK_X_GENTLE_FORCE=1
```

---

## 使用示例

### 1. 初始化并运行一个任务

```bash
# 在当前目录生成 Taskfile.yml 模板
task --init

# 运行名为 "build" 的任务
task build

# 不传任务名时运行 default 任务
task

# 一次运行多个任务
task clean build test
```

### 2. 查看任务清单

```bash
# 列出带描述的任务
task --list

# 列出全部任务（含无描述的）
task --list-all

# 以 JSON 输出，便于脚本解析
task --list --json

# 按字母序排列
task --list-all --sort alphanumeric
```

### 3. 执行控制

```bash
# 强制重跑（忽略 up-to-date 判断）
task --force build

# 干跑：只打印将要执行的顺序，不真正执行
task --dry deploy

# 检查任务是否为最新状态（CI 中常用）
task --status build && echo "already up-to-date"

# 查看任务摘要
task --summary build
```

### 4. 并行与监听

```bash
# 并行运行多个任务
task --parallel lint test

# 并行且任一失败时立即停止其余任务
task --parallel --failfast lint test build

# 限制并发数为 4
task --concurrency 4 --parallel task1 task2 task3 task4

# 监听文件变化自动重新运行
task --watch serve

# 指定监听轮询间隔
task --watch --interval 2s serve
```

### 5. 输出样式

```bash
# 分组输出（任务结束后一次性打印其输出）
task --output group test

# 带任务名前缀（多任务并行时更易区分）
task --output prefixed --parallel build test

# 仅显示失败任务输出
task --output group --output-group-error-only test
```

### 6. 指定目录 / Taskfile / 全局

```bash
# 在指定目录中运行
task --dir ./services/api build

# 使用自定义的 Taskfile
task --taskfile Taskfile.prod.yml deploy

# 运行全局 Taskfile 中的任务
task --global my-global-task
```

### 7. 交互与补全

```bash
# 缺失必填变量时交互式询问
task --interactive deploy

# 非交互环境自动确认所有提示
task --yes clean

# 生成 zsh 补全脚本并写入配置
task --completion zsh > ~/.zsh/completions/_task
```

---

## 最小 Taskfile 示例

```yaml
version: "3"
tasks:
  hello:
    cmds:
      - echo "I am going to write a file named 'output.txt' now."
      - echo "hello" > output.txt
    generates:
      - output.txt
```

运行 `task hello` 将生成 `output.txt`，内容为 `hello`。
