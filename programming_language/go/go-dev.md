# go 的 vscode 开发

- 安装 go 插件

  vscode 的插件库中查找 `go` 。找到第一个微软官方的 go 插件安装即可

- 安装 go 的 tool

  使用快捷键：command+shift+P，然后键入：go:install/update tools，将所有 16 个插件都勾选上，然后点击 OK 即开始安装。

  go 插件部分需要科学上网 或者配置公开的镜像源进行下载安装

  使用 `F1` 键 也可以有类似的作用

- go 语言 vscode 配置 test

  在 vscode 中 找到 settings 配置位置 搜索 `Go:Test Tags` 修改此项，加入 `-v`

- 镜像安装失败 则需要配置国内的源

  配置方法 见 [README.md](./README.md#go语言的国内代理配置)

- go 配置语言服务器 - gopls 服务

  <https://github.com/golang/tools/tree/master/gopls>

  <https://github.com/golang/tools/blob/master/gopls/doc/vscode.md> vscode 配置 gopls 服务

- 单个项目配置方式

  在项目中的 .vscode 文件夹下 settings.json 下配置

  ```json
  {
    "go.useLanguageServer": true,
    "[go]": {
      "editor.formatOnSave": true,
      "editor.codeActionsOnSave": {
        "source.organizeImports": true
      },
      // Optional: Disable snippets, as they conflict with completion ranking.
      "editor.snippetSuggestions": "none"
    },
    "[go.mod]": {
      "editor.formatOnSave": true,
      "editor.codeActionsOnSave": {
        "source.organizeImports": true
      }
    },
    "gopls": {
      // Add parameter placeholders when completing a function.
      "usePlaceholders": true,

      // If true, enable additional analyses with staticcheck.
      // Warning: This will significantly increase memory usage.
      "staticcheck": false
    }
  }
  ```
