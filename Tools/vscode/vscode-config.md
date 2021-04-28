# vscode 的配置文件说明

-[返回](./README.md)

> vscode 有三个配置文件 launch.json setting.json tasks.json

- [官方文档](https://code.visualstudio.com/docs)

## launch.json

- 主要是进行运行环境的相关配置

  可以自动生成 - 点击左侧的第四个 debug/run 按钮(快捷键 ctrl+shift+d)创建 launch.json 文件

  这个文件中配置启动相关命名等

- 执行一些命令的配置

## setting.json

- vscode 的项目相关的定制化配置

- 两种配置方式

  一种是 file - preferences - settings

  打开 settings.json 文件的方式 ctrl + p --> search settings.json 即可打开 settings.json 文件

  单个项目配置 vscode,在项目根目录下 创建 .vscode 文件夹 然后创建 settings.json 文件

  在里面编译 json,即可进行自定义的相关 vscode 配置

## tasks.json

- 编译过程的配置等

## 区别

- tasks 可以被用来做编译，而 launch 用来执行编译好的文件。

## vscode 配置代码块

- Snippets (代码)设置 代码联想配置 各个语言的都可以配置

- [snippets 官方说明文档](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

  按 F1 -> 查询 snippets ->

  配置代码块快捷方式 以下配置为测试

  ```json
  {
    "console.log": {
      "prefix": "log",
      "body": ["fmt.Println($1)", "$2"],
      "description": "fmt快捷输入方式"
    },
    "test": {
      "prefix": "tttt",
      "body": "test.Test('$0')",
      "description": "test"
    }
  }
  ```

## 常用自定义配置

- 字体配置

  `"editor.fontFamily": "JetBrains Mono, 'Courier New', monospace",`

## 插件的相关配置

- vim 插件 自定义 vscode-vim 插件配置

  Settings 中配置如下 过滤掉

  ```json
    "vim.handleKeys": {
      "<C-a>": false,
      "<C-f>": false,
      "<C-n>": false,
      "<C-d>": true
    },
    "vim.insertModeKeyBindings": [
      {
        "before": ["h", "h"],
        "after": ["<Left>"]
      },
      {
        "before": ["l", "l"],
        "after": ["<Right>"]
      },
      {
        "before": ["q", "q"],
        "after": ["<Esc>"]
      }
    ],
  ```
