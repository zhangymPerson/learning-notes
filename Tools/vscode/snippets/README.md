# 配置各个语言的代码片段

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
