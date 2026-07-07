# Scalar CLI 命令参考文档

> 工具：`@scalar/cli`
> 用途：处理 OpenAPI 文件、管理 Scalar 平台资源（文档、项目、注册表、团队、SDK、Schema）
> 运行方式：`npx @scalar/cli <command>` 或全局安装后使用 `scalar <command>`
> 文档生成时间：2026-07-07（随版本更新而变化，运行 `scalar upgrade` 可升级）

---

## 一、主命令概览

```
scalar [options] [command]
```

| 选项            | 说明         |
| --------------- | ------------ |
| `-V, --version` | 输出版本号   |
| `-h, --help`    | 显示帮助信息 |

### 命令树

```
scalar
├── readme          打开 CLI 文档
│   └── generate    自动生成 CLI 文档
├── upgrade         升级当前版本的 CLI
├── auth            管理 Scalar 平台的授权
│   ├── login       登录 Scalar
│   ├── whoami      显示当前用户
│   └── logout      退出登录
├── document        管理本地 OpenAPI 文件（纯本地，无需登录）
│   ├── bundle      打包 OpenAPI 规范（解析所有引用与外部依赖）
│   ├── split       将 OpenAPI 文档拆分为小块
│   ├── format      格式化 OpenAPI 文件
│   ├── mock        基于 OpenAPI 文件启动 Mock 服务
│   ├── serve       基于 OpenAPI 文件启动 API Reference 服务
│   ├── share       分享一个 OpenAPI 文件
│   ├── validate    校验 OpenAPI 文件
│   ├── void        启动一个镜像 HTTP 请求的服务器
│   ├── lint        使用 spectral 规则进行 OpenAPI 规范检查
│   └── upgrade     将 OpenAPI 文档升级到 3.1 版本
├── project         管理 Scalar 项目
│   ├── init        创建新的 scalar.config.json 配置文件
│   ├── check-config 检查 Scalar 配置文件
│   ├── create      创建一个未关联 GitHub 的新项目
│   ├── preview     预览 Scalar guides
│   └── publish     为未关联的 GitHub 同步项目发布新构建
├── registry        管理 Scalar 注册表
│   ├── publish     发布 OpenAPI 文档到 Scalar 注册表
│   ├── update      更新 Scalar 注册表上的文档元数据
│   ├── delete      从 Scalar 注册表删除文档
│   └── list        列出某个团队命名空间下的所有注册表 API
├── team            管理用户团队
│   ├── list        列出当前用户所属的所有团队
│   └── set         设置当前激活的团队
├── sdk             管理 Scalar SDK（仅企业版）
│   ├── list        列出某个团队命名空间下的所有 SDK
│   ├── create      创建新的 SDK
│   ├── update      更新 SDK 元数据
│   ├── delete      删除 SDK
│   └── build       创建一个 SDK 构建
└── schema          管理 Scalar Schema
    ├── delete      删除一个 Schema
    ├── update      更新 Schema 元数据
    ├── list        列出某个团队命名空间下的所有 Schema
    └── publish     发布共享 Schema 到 Scalar 注册表
```

---

## 二、document（本地 OpenAPI 文件管理，最常用）

> 这一组命令全部在本地运行，不需要登录 Scalar 账号，是日常开发中最常用的部分。

### `scalar document bundle [options] [file|url]`

解析所有引用和外部依赖，将 OpenAPI 规范打包为一个文件。

| 参数/选项              | 说明                                |
| ---------------------- | ----------------------------------- |
| `file\|url`            | 待打包的 OpenAPI 文件路径或 URL     |
| `-o, --output <file>`  | 打包输出文件的保存路径              |
| `--treeShake`          | 从打包结果中移除未使用的 components |
| `--urlMap`             | 在打包结果中生成已解析 URL 的映射   |
| `--fetchLimit <limit>` | 打包时同时抓取 URL 的最大数量       |
| `-h, --help`           | 显示帮助                            |

### `scalar document split [options] [file|url]`

将 OpenAPI 文档拆分为多个小块。

| 参数/选项             | 说明                            |
| --------------------- | ------------------------------- |
| `file\|url`           | 待拆分的 OpenAPI 文件路径或 URL |
| `-o, --output <path>` | 拆分后分块文件的保存路径        |
| `-h, --help`          | 显示帮助                        |

### `scalar document format [options] [file|url]`

格式化 OpenAPI 文件。

| 参数/选项             | 说明                 |
| --------------------- | -------------------- |
| `file\|url`           | 待格式化的文件或 URL |
| `-o, --output <file>` | 输出文件             |
| `-h, --help`          | 显示帮助             |

### `scalar document mock [options] [file|url]`

基于 OpenAPI 文件启动一个 Mock API 服务器。

| 参数/选项           | 说明                          |
| ------------------- | ----------------------------- |
| `file\|url`         | 待 Mock 的 OpenAPI 文件或 URL |
| `-w, --watch`       | 监听文件变化                  |
| `-o, --once`        | 只运行一次服务器，结束后退出  |
| `-p, --port <port>` | 设置 Mock 服务器的 HTTP 端口  |
| `-h, --help`        | 显示帮助                      |

### `scalar document serve [options] [file|url]`

基于 OpenAPI 文件启动一个 API Reference（接口文档）本地服务。

| 参数/选项           | 说明                                   |
| ------------------- | -------------------------------------- |
| `file\|url`         | 待展示 Reference 的 OpenAPI 文件或 URL |
| `-w, --watch`       | 监听文件变化                           |
| `-o, --once`        | 只运行一次服务器，结束后退出           |
| `-p, --port <port>` | 设置 API Reference 服务的 HTTP 端口    |
| `-h, --help`        | 显示帮助                               |

### `scalar document share [options] [file]`

分享一个 OpenAPI 文件（上传到 Scalar 沙盒）。

| 参数/选项             | 说明                              |
| --------------------- | --------------------------------- |
| `file`                | 待分享的文件                      |
| `-t, --token <token>` | 传入 token 以更新一个已存在的沙盒 |
| `-h, --help`          | 显示帮助                          |

### `scalar document validate [options] [file|url]`

校验 OpenAPI 文件的合法性。

| 参数/选项    | 说明               |
| ------------ | ------------------ |
| `file\|url`  | 待校验的文件或 URL |
| `-h, --help` | 显示帮助           |

### `scalar document void [options]`

启动一个镜像 HTTP 请求的服务器（便于调试请求）。

| 选项                | 说明                         |
| ------------------- | ---------------------------- |
| `-o, --once`        | 只运行一次服务器，结束后退出 |
| `-p, --port <port>` | 设置 Mock 服务器的 HTTP 端口 |
| `-h, --help`        | 显示帮助                     |

### `scalar document lint [options] [file|url]`

使用 spectral 规则对 OpenAPI 文件进行规范检查（lint）。

| 参数/选项                | 说明                   |
| ------------------------ | ---------------------- |
| `file\|url`              | OpenAPI 文件路径或 URL |
| `-r, --rule <file\|url>` | 规则文件路径或 URL     |
| `-h, --help`             | 显示帮助               |

### `scalar document upgrade [options] [file|url]`

将 OpenAPI 文档升级到 3.1 版本。

| 参数/选项             | 说明                     |
| --------------------- | ------------------------ |
| `file\|url`           | 待升级的文件或 URL       |
| `-o, --output <file>` | 升级后输出文件的保存路径 |
| `-h, --help`          | 显示帮助                 |

---

## 三、auth（平台授权管理）

### `scalar auth login [options]`

登录 Scalar。

| 选项                    | 说明                       |
| ----------------------- | -------------------------- |
| `--email <email>`       | 邮箱                       |
| `--password <password>` | 密码                       |
| `--token <token>`       | 个人令牌（Personal Token） |
| `-h, --help`            | 显示帮助                   |

### `scalar auth whoami [options]`

显示当前登录用户。仅 `-h, --help` 选项。

### `scalar auth logout [options]`

退出登录。仅 `-h, --help` 选项。

---

## 四、project（项目管理）

### `scalar project init [options]`

创建新的 `scalar.config.json` 配置文件，指定 OpenAPI 文件位置。

| 选项                    | 说明              |
| ----------------------- | ----------------- |
| `-f, --file [file]`     | 你的 OpenAPI 文件 |
| `-s, --subdomain [url]` | 发布所用的子域名  |
| `--force`               | 覆盖已有配置      |
| `-h, --help`            | 显示帮助          |

### `scalar project create [options]`

创建一个未关联 GitHub 的新项目。

| 选项                | 说明      |
| ------------------- | --------- |
| `-n, --name [name]` | 项目名称  |
| `-s, --slug [slug]` | 项目 slug |
| `-h, --help`        | 显示帮助  |

### 其余 project 子命令

- `check-config [file]`：检查 Scalar 配置文件
- `preview [options] [config]`：预览 Scalar guides
- `publish [options]`：为未关联的 GitHub 同步项目发布新构建

---

## 五、registry（注册表管理）

### `scalar registry publish [options] [file]`

发布 OpenAPI 文档到 Scalar 注册表。

| 参数/选项                 | 说明                                 |
| ------------------------- | ------------------------------------ |
| `file`                    | 待上传的 OpenAPI 文件                |
| `--slug <slug>`           | 注册表条目的 slug 标识，默认取 title |
| `--namespace <namespace>` | Scalar 团队命名空间                  |
| `--version <version>`     | API 版本（如 0.1.0）                 |
| `--private`               | 设为私有 API（默认 false）           |
| `--force`                 | 强制覆盖已有版本（默认 false）       |
| `-h, --help`              | 显示帮助                             |

### 其余 registry 子命令

- `update [options] [namespace] [slug]`：更新 Scalar 注册表上的文档元数据
- `delete [namespace] [slug]`：从 Scalar 注册表删除文档
- `list [options]`：列出某个团队命名空间下的所有注册表 API

---

## 六、team（团队管理）

### `scalar team list`

列出当前用户所属的所有团队。仅 `-h, --help` 选项。

### `scalar team set [options]`

设置当前激活的团队。

| 选项            | 说明     |
| --------------- | -------- |
| `--team <team>` | 团队 uid |
| `-h, --help`    | 显示帮助 |

---

## 七、sdk（SDK 管理，仅企业版）

`scalar sdk` 及其子命令 `list` / `create` / `update` / `delete` / `build` 均为企业版功能，
用于管理 Scalar 自动生成的 SDK。各子命令均支持 `[options]` 与 `-h, --help`。

---

## 八、schema（Schema 管理）

- `delete [options]`：删除一个 Schema
- `update [options]`：更新 Schema 元数据
- `list [options]`：列出某个团队命名空间下的所有 Schema
- `publish [options] [file]`：发布共享 Schema 到 Scalar 注册表

---

## 九、readme / upgrade

### `scalar readme`

打开 CLI 文档，子命令 `generate [options]` 可自动生成 CLI 文档本身。

### `scalar upgrade`

升级当前版本的 CLI。仅 `-h, --help` 选项。

---

## 十、常用示例

```bash
# 本地预览接口文档（最常用）
npx @scalar/cli document serve ./openapi.yaml --port 4000

# 启动 Mock 服务器
npx @scalar/cli document mock ./openapi.yaml --watch

# 校验 OpenAPI 文件
npx @scalar/cli document validate ./openapi.yaml

# 把分散的引用打包成单个文件
npx @scalar/cli document bundle ./openapi.yaml -o bundled.yaml

# 用 spectral 规则做规范检查
npx @scalar/cli document lint ./openapi.yaml -r ./my-rules.yaml

# 升级到 OpenAPI 3.1
npx @scalar/cli document upgrade ./openapi.yaml -o openapi-3.1.yaml

# 登录 / 查看当前用户 / 退出
npx @scalar/cli auth login --token <personal-token>
npx @scalar/cli auth whoami
npx @scalar/cli auth logout
```

> 提示：`document` 下的命令均为本地操作，无需登录即可使用；`registry` / `project` / `sdk` / `schema` / `team` 等涉及 Scalar 平台的功能需要先用 `scalar auth login` 登录。
