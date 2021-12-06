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

  **打开 settings.json 文件的方式**

  1.打开用户的 settings 文件

  ctrl + p --> search settings.json 即可打开 settings.json 文件

  2.打开全局的 settings 文件

  ctrl+shift+p -> search -> open default settings 即可打开 settings.json 文件

  单个项目配置 vscode,在项目根目录下 创建 .vscode 文件夹 然后创建 settings.json 文件

  在里面编译 json,即可进行自定义的相关 vscode 配置

## tasks.json

- 编译过程的配置等

## 区别

- tasks 可以被用来做编译，而 launch 用来执行编译好的文件。

## vscode 配置代码块

### vscode 配置不同语言的关键字联想

- 在 VScode 主界面 -> 点击左下角设置图标 -> 点击用户代码片段 -> 选择语言

- file -> preference -> user snippet -> 各个语言的 snippet

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

## vscode 配置标签页自动换行全部展示 一行展示不下自动换行展示

- setting 搜索 wrap tabs 选中标签即可

- 将当前行代码高亮显示（更改光标所在行的背景色）

  当我们把光标放在某一行时，这一行的背景色并没有发生变化。如果想高亮显示当前行的代码，需要设置两步：

  （1）在设置项里搜索 editor.renderLineHighlight，将选项值设置为 all 或者 line。

  （2）在设置项里增加如下内容：

  ```json
  "workbench.colorCustomizations": {
    "editor.lineHighlightBackground": "#00000090",
    "editor.lineHighlightBorder": "#ffffff30"
  }
  ```

  复制代码上方代码，第一行代码的意思是：修改光标所在行的背景色（背景色设置为全黑，不透明度 90%）；第二行代码的意思是：修改光标所在行的边框色。

## vscode 文件比较/比较文件更改

- 比较两个文件差异

  选中两个文件 右键 -> 将已选项进行比较 / compare selected

- 插件支持 可以和剪切板中的数据比较

  插件名:compareit

## vscode 代码提示失效 不能自动联想

- 修改提示相关的配置

  打开 settings -> search -> `Suggest: Snippets Prevent Quick Suggestions`

## vscode 配置大括号换行问题

- 修改 settings

  php / c / C++ 大括号换行问题
  
  打开 settings -> search -> `format:braces` -> 选择对应的语言/插件 修改相关配置
