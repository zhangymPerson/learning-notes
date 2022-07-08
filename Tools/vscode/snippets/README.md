# 配置各个语言的代码片段

## 配置自定义的代码片段

- [cpp.json](./cpp.json)

- [golbal.code-snippets](./golbal.code-snippets)

- [markdown.json](./markdown.json)

- [php.json](./php.json)

- [python.json](./python.json)

- [shellscript.json](./shellscript.json)

- [snippets.md](./snippets.md)

## 说明

- [官网说明](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

- 通过输入 某个关键字 自动生成代码片段

- 代码风格参考:<https://github.com/zh-google-styleguide/zh-google-styleguide>

- markdown 代码片段配置需要在 settings.xml 中添加配置

  ```json
  "[markdown]": {
      "editor.formatOnSave": true,
      "editor.renderWhitespace": "all",
      "editor.quickSuggestions": {
          "other": "on",
          "comments": "off",
          "strings": "off"
      },
      "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  ```

## 代码提示相关的配置说明

- [intellisense 代码智能感知](https://code.visualstudio.com/docs/editor/intellisense)

- [Snippets 自定义代码片段](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

- vscode 的代码提示开关

  `quickSuggestions` 配置 `other` 状态为 `on`

- vscode 代码片段 snippets

  单语言 代码片段配置 setting > 搜索 snippets > 单击要选择的语言进行配置

  全局代码片段配置 setting > 搜索 snippets > 选则 > global \*\*\* 进行配置

- vscode 代码 snippets 提示问题

  页面无提示，使用 tab 键生成代码的配置

  `"editor.tabCompletion": "on"`
