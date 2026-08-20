# Dagu CLI 命令参考文档

> 自动生成于 `dagu --help` 递归探索

## 概览

**Dagu** 是一个紧凑、可移植的工作流引擎，使用声明式模型编排命令执行（shell 脚本、Python 命令、容器操作、远程命令等）。

**全局参数**：

- `--context <name>`：指定 CLI 上下文（默认当前上下文或 local）
- `-h, --help`：显示帮助

---

## 命令树

```
dagu
├── cleanup              - 清理旧的 DAG 运行历史
├── completion           - 生成自动补全脚本
│   ├── bash
│   ├── fish
│   ├── powershell
│   └── zsh
├── config               - 显示解析后的配置路径
├── context              - 管理 CLI 上下文
│   ├── add
│   ├── list
│   ├── remove
│   ├── test
│   ├── update
│   └── use
├── coordinator          - 启动分布式任务协调器 gRPC 服务器
├── dequeue              - 从队列中取出 DAG-run
├── dry                  - 模拟 DAG-run，不实际执行
├── enqueue              - 将 DAG-run 加入队列
├── example              - 显示示例 DAG 定义
├── exec                 - 执行一次性命令作为 DAG run
├── history              - 显示 DAG 运行历史
├── license              - 许可证管理
│   ├── activate
│   ├── check
│   └── deactivate
├── profile              - 运行时配置管理
│   ├── create
│   ├── delete
│   ├── delete-key
│   ├── disable
│   ├── enable
│   ├── list
│   ├── set-secret
│   ├── set-var
│   └── show
├── restart              - 用新 ID 重启运行中的 DAG-run
├── retry                - 使用相同 run ID 重试之前的 DAG-run
├── scheduler            - 启动调度器
├── schema               - 显示 DAG 或配置 schema 文档
├── server               - 启动 Web UI 服务器
├── start                - 根据 DAG 定义执行 DAG-run
├── start-all            - 同时启动 UI、调度器和协调器
├── status               - 显示 DAG-run 当前状态
├── stop                 - 停止活动的 DAG-run
├── sync                 - Git 同步操作
│   ├── cleanup
│   ├── delete
│   ├── discard
│   ├── forget
│   ├── mv
│   ├── publish
│   ├── pull
│   └── status
├── upgrade              - 升级 dagu
├── validate             - 验证 DAG 规范
├── version              - 显示版本信息
└── worker               - 启动轮询协调器任务的工作进程
```

---

## 常用命令使用样例

### 启动与运行 DAG

```bash
# 启动一个 DAG
dagu start my_dag -- P1=foo P2=bar

# 指定自定义 DAG 名称启动
dagu start --name my_custom_name my_dag.yaml -- P1=foo P2=bar

# dry-run 模拟执行
dagu dry my_dag.yaml -- P1=foo P2=bar

# 验证 DAG 文件
dagu validate my_dag.yaml
```

### 运行状态管理

```bash
# 查看 DAG 最新运行状态
dagu status my_dag

# 指定 run-id 查看状态
dagu status --run-id=abc123 my_dag

# 停止运行
dagu stop --run-id=abc123 my_dag

# 重试
dagu retry --run-id=abc123 my_dag

# 查看历史
dagu history
dagu history my-dag --status failed --last 24h
dagu history --format json --limit 50
```

### 历史清理

```bash
# 删除所有历史（带确认）
dagu cleanup my-workflow

# 保留最近 30 天
dagu cleanup --retention-days 30 my-workflow

# 预览将要删除的内容
dagu cleanup --dry-run my-workflow

# 跳过确认
dagu cleanup -y my-workflow
```

### 启动服务

```bash
# 启动 Web UI
dagu server --host=0.0.0.0 --port=8080 --dags=/path/to/dags

# 启动调度器
dagu scheduler --dags=/path/to/dags

# 同时启动 UI + 调度器 + 协调器
dagu start-all

# 分布式模式
dagu start-all --host=0.0.0.0 --coordinator.host=0.0.0.0 --coordinator.port=50055
```

### 队列操作

```bash
# 入队
dagu enqueue --run-id=run_id my_dag -- P1=foo P2=bar

# 出队
dagu dequeue default --dag-run=dag_name:my_dag_run_id
```

### 一次性执行

```bash
dagu exec -- echo "hello world"
dagu exec --env FOO=bar -- sh -c 'echo $FOO'
dagu exec --worker-label role=batch -- python remote_script.py
```

### 上下文管理

```bash
dagu context add prod --server http://dagu.example.com --api-key xxx
dagu context list
dagu context use prod
dagu context test prod
dagu context update prod --server http://new.example.com
dagu context remove prod
```

### 同步（Git sync）

```bash
dagu sync status
dagu sync pull
dagu sync publish my_dag -m "Updated schedule"
dagu sync publish --all -m "Batch update"
dagu sync mv old_dag new_dag -m "Rename workflow"
dagu sync delete my_dag -m "Remove old workflow"
dagu sync discard my_dag
dagu sync cleanup
```

### 配置文件和 schema

```bash
# 查看配置路径
dagu config

# 查看 DAG schema
dagu schema dag
dagu schema dag steps
dagu schema dag steps.container

# 查看配置 schema
dagu schema config
dagu schema config server
```

### 示例

```bash
# 列出所有示例
dagu example

# 查看指定示例
dagu example 1
dagu example 7
```

### 升级

```bash
dagu upgrade
dagu upgrade --check
dagu upgrade --version v1.30.0
dagu upgrade --dry-run
```

### 自动补全

```bash
# bash
source <(dagu completion bash)

# zsh
source <(dagu completion zsh)

# fish
dagu completion fish | source
```

---

## 分类速查

| 类别            | 命令                                                        |
| --------------- | ----------------------------------------------------------- |
| **DAG 执行**    | `start`, `dry`, `exec`, `enqueue`, `dequeue`                |
| **运行管理**    | `status`, `stop`, `restart`, `retry`, `history`, `cleanup`  |
| **服务启动**    | `server`, `scheduler`, `coordinator`, `worker`, `start-all` |
| **配置/开发**   | `config`, `validate`, `schema`, `example`, `version`        |
| **上下文/远程** | `context`                                                   |
| **运行时变量**  | `profile`                                                   |
| **Git 同步**    | `sync`                                                      |
| **许可证**      | `license`                                                   |
| **工具**        | `completion`, `upgrade`                                     |

---

## 详细命令说明

### dagu start

开始执行一个 DAG-run。

**用法**：

```bash
dagu start [flags] <DAG definition> [-- param1 param2 ...]
```

**示例**：

```bash
dagu start my_dag -- P1=foo P2=bar
dagu start --name my_custom_name my_dag.yaml -- P1=foo P2=bar
```

**常用选项**：

- `-N, --name`：覆盖 DAG 名称
- `-p, --params`：传递参数
- `-r, --run-id`：指定 DAG-run ID
- `--labels`：附加标签
- `--profile`：运行时配置
- `--trigger-type`：触发类型（默认 manual）

---

### dagu dry

模拟 DAG-run，不执行实际命令。

**用法**：

```bash
dagu dry [flags] <DAG definition> [-- param1 param2 ...]
```

**示例**：

```bash
dagu dry my_dag.yaml -- P1=foo P2=bar
```

---

### dagu exec

无需创建 YAML 文件，直接执行一次性命令作为 DAG run。

**用法**：

```bash
dagu exec [flags] -- <command> [args...]
```

**示例**：

```bash
dagu exec -- echo "hello world"
dagu exec --env FOO=bar -- sh -c 'echo $FOO'
dagu exec --worker-label role=batch -- python remote_script.py
```

---

### dagu validate

验证 DAG YAML 文件。

**用法**：

```bash
dagu validate [flags] <DAG definition>
```

---

### dagu status

显示 DAG-run 实时状态。

**用法**：

```bash
dagu status [flags] <DAG name>
```

**示例**：

```bash
dagu status my_dag
dagu status --run-id=abc123 my_dag
dagu status --run-id=abc123 --sub-run-id=def456 my_dag
```

---

### dagu stop

优雅地终止活动的 DAG-run。

**用法**：

```bash
dagu stop [flags] <DAG name>
```

**示例**：

```bash
dagu stop --run-id=abc123 my_dag
```

---

### dagu restart

停止当前运行的 DAG-run 并用新 ID 重启。

**用法**：

```bash
dagu restart [flags] <DAG name>
```

**示例**：

```bash
dagu restart --run-id=abc123 my_dag
```

---

### dagu retry

使用相同的 run ID 重试之前执行的 DAG-run。

**用法**：

```bash
dagu retry [flags] <DAG name or file>
```

**示例**：

```bash
dagu retry --run-id=abc123 my_dag
dagu retry --run-id=abc123 my_dag.yaml
```

---

### dagu history

显示 DAG 运行历史。

**用法**：

```bash
dagu history [flags] [DAG name]
```

**示例**：

```bash
dagu history
dagu history my-dag
dagu history --from 2026-01-01
dagu history --last 7d
dagu history --status failed
dagu history --format json
dagu history --labels "prod,critical"
dagu history --limit 50
```

---

### dagu cleanup

清理旧的 DAG 运行历史。

**用法**：

```bash
dagu cleanup [flags] <DAG name>
```

**示例**：

```bash
dagu cleanup my-workflow
dagu cleanup --retention-days 30 my-workflow
dagu cleanup --dry-run my-workflow
dagu cleanup -y my-workflow
```

---

### dagu server

启动 Web UI 服务器。

**用法**：

```bash
dagu server [flags]
```

**示例**：

```bash
dagu server --host=0.0.0.0 --port=8080 --dags=/path/to/dags
```

**常用选项**：

- `-s, --host`：主机地址（默认 localhost）
- `-p, --port`：端口（默认 8080）
- `-d, --dags`：DAG 文件目录
- `--tunnel`：启用隧道模式

---

### dagu scheduler

启动调度器，按 cron 计划自动触发 DAG。

**用法**：

```bash
dagu scheduler [flags]
```

**示例**：

```bash
dagu scheduler --dags=/path/to/dags
```

---

### dagu start-all

同时启动 Web UI、调度器和协调器。

**用法**：

```bash
dagu start-all [flags]
```

**示例**：

```bash
dagu start-all
dagu start-all --host=0.0.0.0 --port=8080 --coordinator.host=0.0.0.0
```

---

### dagu coordinator

启动协调器 gRPC 服务器。

**用法**：

```bash
dagu coordinator [flags]
```

**示例**：

```bash
dagu coordinator --coordinator.host=0.0.0.0 --coordinator.port=50055
```

---

### dagu worker

启动工作进程，连接协调器并轮询任务。

**用法**：

```bash
dagu worker [flags]
```

**示例**：

```bash
dagu worker --worker.coordinators=coordinator-1:50055
dagu worker --worker.coordinators=coordinator-1:50055 --worker.labels gpu=true,memory=64G
```

---

### dagu enqueue / dequeue

队列操作。

```bash
# 入队
dagu enqueue --run-id=run_id my_dag -- P1=foo P2=bar
dagu enqueue --name my_custom_name my_dag.yaml -- P1=foo P2=bar

# 出队
dagu dequeue default --dag-run=dag_name:my_dag_run_id
dagu dequeue default
```

---

### dagu config

显示解析后的配置路径。

```bash
dagu config
dagu config --dagu-home /custom/path
```

---

### dagu schema

浏览 DAG 或配置 JSON schema。

```bash
dagu schema dag
dagu schema dag steps
dagu schema dag steps.container
dagu schema config
dagu schema config server
```

---

### dagu example

显示示例 DAG 定义。

```bash
dagu example      # 列出所有示例
dagu example 1    # 查看并行步骤示例
dagu example 7    # 查看 HTTP 请求示例
```

---

### dagu context

管理 CLI 上下文。

```bash
dagu context add <name> --server <url> [--api-key <key>]
dagu context list
dagu context use <name|local>
dagu context test <name|local>
dagu context update <name> --server <url>
dagu context remove <name>
```

---

### dagu profile

运行时配置管理。

```bash
dagu profile create <profile> [--description <desc>] [--protected]
dagu profile list
dagu profile show <profile>
dagu profile enable <profile>
dagu profile disable <profile>
dagu profile delete <profile>
dagu profile set-var <profile> <key> <value>
dagu profile set-secret <profile> <key> [--value-stdin]
dagu profile delete-key <profile> <key>
```

---

### dagu sync

Git 同步操作。

```bash
dagu sync status
dagu sync pull
dagu sync publish [dag-name] -m "message"
dagu sync publish --all -m "Batch update"
dagu sync mv <old-id> <new-id> -m "message"
dagu sync delete <item-id> -m "message"
dagu sync delete --all-missing -m "Clean up"
dagu sync discard <dag-name>
dagu sync forget <item-id>...
dagu sync cleanup
```

---

### dagu license

许可证管理。

```bash
dagu license activate <key>
dagu license check
dagu license deactivate
```

---

### dagu completion

生成自动补全脚本。

```bash
# bash
source <(dagu completion bash)
dagu completion bash > /etc/bash_completion.d/dagu

# zsh
source <(dagu completion zsh)
dagu completion zsh > $(brew --prefix)/share/zsh/site-functions/_dagu

# fish
dagu completion fish | source
dagu completion fish > ~/.config/fish/completions/dagu.fish

# powershell
dagu completion powershell | Out-String | Invoke-Expression
```

---

### dagu upgrade

升级 dagu。

```bash
dagu upgrade
dagu upgrade --check
dagu upgrade --version v1.30.0
dagu upgrade --dry-run
dagu upgrade --backup
dagu upgrade -y -f
```

---

### dagu version

显示版本信息。

```bash
dagu version
```
