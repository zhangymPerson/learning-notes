# Redocly CLI 命令参考（@redocly/cli@latest）

Redocly CLI 是用于 OpenAPI / Arazzo 描述文件的质量管理工具集（校验、打包、拆分、文档生成、评分等）。

> 调用方式：`npx @redocly/cli@latest <command>`

## 命令树总览

```
redocly
├── lint [apis...]             校验 API / Arazzo 描述（最常用）
├── bundle [apis...]           多文件描述合并为单文件
├── split [api]                单文件拆分为多文件结构
├── join [apis...]             多个描述合并为一个 [实验性]
├── stats [api]                显示描述文件的统计信息
├── score [api]                为 API 打“集成简洁度 / AI 就绪度”评分
├── scorecard-classic [api]    多等级质量评分卡
├── build-docs [api]           生成 HTML 文档（静态站点）
├── preview                    本地预览 Redocly 项目
├── push [files...]            推送文档到 Reunite 平台
├── translate <locale>         生成/更新翻译文件
├── eject <type> [path]        导出项目元素（如 component）以便自定义
├── respect [files...]         运行 Arazzo 测试
├── generate-arazzo <path>     从 API 描述自动生成 Arazzo 文件
├── check-config               校验 redocly 配置文件
├── login / logout             登录 / 退出 Redocly 账号
└── completion                 生成 shell 自动补全脚本
```

## 各命令详解与使用示例

### 🔸 lint — 校验（核心命令）

校验 OpenAPI 描述是否符合规范与自定义规则。

```bash
redocly lint openapi.yaml
redocly lint openapi.yaml --config redocly.yaml
redocly lint openapi.yaml --format github-actions   # CI 中输出 GitHub 注解
redocly lint openapi.yaml --max-problems 50
redocly lint openapi.yaml --skip-rule no-unused-components
redocly lint .                                       # 校验目录下所有描述
```

常用选项：

- `--format`：`stylish` / `codeframe` / `json` / `checkstyle` / `codeclimate` / `summary` / `markdown` / `github-actions` / `junit`（默认 `codeframe`）
- `--max-problems`：最多显示的问题数（默认 100）
- `--skip-rule`：忽略指定规则（可重复）
- `--skip-preprocessor`：忽略指定预处理器
- `--generate-ignore-file`：生成忽略文件
- `--config` / `--extends`：配置文件 / 覆盖 extends 配置
- `--lint-config`：`warn` / `error` / `off`

### 🔸 bundle — 打包合并

将 `$ref` 引用的多文件描述打包成单个文件。

```bash
redocly bundle openapi.yaml -o bundled.yaml
redocly bundle openapi.yaml -o dist/openapi.json --ext json
redocly bundle openapi.yaml -d            # 完全解引用（dereferenced）
redocly bundle openapi.yaml -f            # 即使有错误也强制输出
redocly bundle openapi.yaml --remove-unused-components
```

常用选项：

- `-o, --output`：输出文件 / 目录
- `--ext`：`json` / `yaml` / `yml`
- `-d, --dereferenced`：生成完全解引用的 bundle
- `-f, --force`：出错也输出
- `--remove-unused-components`：移除未使用的 components
- `-k, --keep-url-references`：保留绝对 URL 引用
- `--metafile`：输出打包元信息
- `--component-names-strategy`：`basename`（默认）/ `title`

### 🔸 split — 拆分

把单个大文件拆成分目录的多文件结构（与 bundle 相反）。

```bash
redocly split openapi.yaml --outDir openapi/
redocly split openapi.yaml --outDir openapi/ --separator _
```

`--outDir`（输出目录）为必填；`--separator` 默认 `_`。

### 🔸 join — 合并多个描述 [实验性]

```bash
redocly join api1.yaml api2.yaml -o merged.yaml
redocly join ./**/openapi.yaml --prefix-tags-with-filename
```

常用选项：

- `-o, --output`：输出文件
- `--prefix-tags-with-info-prop` / `--prefix-tags-with-filename`：为 tag 加前缀
- `--prefix-components-with-info-prop`：为 components 加前缀
- `--without-x-tag-groups`：跳过自动创建 x-tagGroups

### 🔸 stats — 统计信息

```bash
redocly stats openapi.yaml
redocly stats openapi.yaml --format json
```

`--format`：`stylish` / `json` / `markdown`（默认 `stylish`）。

### 🔸 score — AI 就绪度评分

```bash
redocly score openapi.yaml
redocly score openapi.yaml --operation-details
redocly score openapi.yaml --debug-operation-id getUser
```

常用选项：

- `--format`：`stylish` / `json`
- `--operation-details`：打印每个操作的指标明细
- `--debug-operation-id`：打印指定操作的 schema 明细

### 🔸 scorecard-classic — 质量评分卡

```bash
redocly scorecard-classic openapi.yaml
redocly scorecard-classic openapi.yaml --target-level silver --verbose
```

常用选项：

- `--format`：`stylish` / `json` / `checkstyle` / `junit`
- `--target-level`：目标等级
- `--project-url`：远程评分卡配置 URL
- `-v, --verbose`：详细模式

### 🔸 build-docs — 生成 HTML 文档

```bash
redocly build-docs openapi.yaml -o docs.html
redocly build-docs openapi.yaml --title "我的 API" --disableGoogleFont
redocly build-docs openapi.yaml -t custom-template.hbs --theme.openapi.nativeScrollbars
```

常用选项：

- `-o, --output`：输出文件（默认 `redoc-static.html`）
- `--title`：页面标题
- `--disableGoogleFont`：禁用 Google 字体
- `-t, --template`：自定义 handlebars 模板
- `--templateOptions` / `--theme`：点号路径传参，如 `theme.openapi.nativeScrollbars`
- `--config`

### 🔸 preview — 本地预览

```bash
redocly preview
redocly preview --product redoc -p 4000
redocly preview -d ./my-project
```

常用选项：

- `--product`：`redoc` / `revel` / `reef` / `realm` / `redoc-revel` / `redoc-reef` / `revel-reef`
- `--plan`：`pro` / `enterprise`（默认 `enterprise`）
- `-p, --port`：端口（默认 4000）
- `-d, --project-dir`：项目目录（默认当前目录）

### 🔸 push — 推送到 Reunite 平台

```bash
redocly push openapi.yaml -o my-org -p my-project \
  -b main --mp / -a "Jane" -m "Update API" \
  --wait-for-deployment
```

必填项：`-b/--branch`、`-o/--organization`、`-p/--project`、`--mount-path/--mp`、`-a/--author`、`-m/--message`。

其他选项：`--commit-sha`、`--commit-url`、`--namespace`、`--repository`、`--created-at`、`-d/--domain`、`--default-branch`（默认 `main`）、`--max-execution-time`、`--wait-for-deployment`、`--verbose`、`--continue-on-deploy-failures`。

### 🔸 respect — 运行 Arazzo 测试

```bash
redocly respect test.arazzo.yaml
redocly respect test.arazzo.yaml --server '{"apiUrl":"https://api.example.com"}'
redocly respect test.arazzo.yaml -w loginFlow -v
redocly respect test.arazzo.yaml -J result.json -H trace.har
```

常用选项：

- `-i, --input`：输入参数
- `-S, --server`：服务端参数
- `-w, --workflow` / `-s, --skip`：指定 / 跳过工作流
- `-v, --verbose`：详细模式
- `-H, --har-output` / `-J, --json-output`：输出 HAR / JSON
- `--mtls`：逐域双向 TLS 证书（JSON）
- `--max-steps`（默认 2000）、`--max-fetch-timeout`（默认 40000ms）、`--execution-timeout`（默认 3600000ms）
- `--no-secrets-masking`：不在输出中脱敏密钥

### 🔸 generate-arazzo — 生成 Arazzo

```bash
redocly generate-arazzo openapi.yaml -o workflow.arazzo.yaml
```

`-o, --output-file`：输出文件名。

### 🔸 translate / eject — 国际化与自定义

```bash
redocly translate all                 # 为所有语言生成翻译
redocly translate zh-CN -d ./project
redocly eject component Sidebar       # 导出组件自定义
redocly eject component "**/*.vue" -f
```

`translate` 必填 `locale`（或 `all`）；`eject` 的 `type` 当前仅支持 `component`。

### 🔸 check-config — 校验配置

```bash
redocly check-config
redocly check-config --config redocly.yaml
```

`--lint-config`：`warn` / `error`（默认 `error`）。

### 🔸 login / logout / completion

```bash
redocly login -r us
redocly logout
redocly completion >> ~/.zshrc        # 启用 shell 自动补全
```

`login` 选项：`-r, --residency`（默认 `us`）、`-v, --verbose`、`--config`。

## 典型工作流

```bash
# 1. 拆分大文件 → 2. 编辑 → 3. 校验 → 4. 打包 → 5. 生成文档
redocly split api.yaml --outDir api/
redocly lint api/openapi.yaml
redocly bundle api/openapi.yaml -o dist/api.yaml
redocly build-docs dist/api.yaml -o public/api.html
```
