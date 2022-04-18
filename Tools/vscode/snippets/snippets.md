# vscode snippets

- 代码片段配置
- [官方文档](https://code.visualstudio.com/docs/editor/userdefinedsnippets)

- 全局配置

  ```json
  // 自定义常用的联想
  {
    // 自定义常用结构的代码联想
    // ==============================================================================================
    "slef_配置模板说明": {
      // 指定对应的编程语言 如 java,javascript,python 等
      "scope": "",
      // 指定代码联想输入的关键字 如 输入 sheader 则进行代码片段替换
      "prefix": "sheader",
      // 要替换的代码片段
      "body": [""],
      // 说明这个代码片段的作用
      "description": "创建一个[main]函数"
    },
    "self_language_header": {
      "scope": "",
      "prefix": "sheader",
      "body": [""],
      "description": "创建一个[main]函数"
    },
    "self_language_main": {
      "scope": "",
      "prefix": "smain",
      "body": [""],
      "description": "创建一个[main]函数"
    },
    "self_language_array": {
      "scope": "",
      "prefix": "sarr",
      "body": [""],
      "description": "创建一个[数组]结构"
    },
    "self_language_list": {
      "scope": "",
      "prefix": "slist",
      "body": [""],
      "description": "创建一个[list]结构"
    },
    "self_language_set": {
      "scope": "",
      "prefix": "sset",
      "body": [""],
      "description": "创建一个[set]结构"
    },
    "self_language_map": {
      "scope": "",
      "prefix": "smap",
      "body": [""],
      "description": "创建一个[map]结构"
    },
    "self_language_now": {
      "scope": "",
      "prefix": "snow",
      "body": [""],
      "description": "获取当前时间"
    },
    "self_language_log": {
      "scope": "",
      "prefix": "slog",
      "body": [""],
      "description": "创建一个日志"
    },
    "self_language_print": {
      "scope": "",
      "prefix": "sprint",
      "body": [""],
      "description": "创建一个打印输出"
    },
    "self_language_object": {
      "scope": "",
      "prefix": "sobject",
      "body": [""],
      "description": "创建一个[object]结构"
    },
    "self_language_tojson": {
      "scope": "",
      "prefix": "tojson",
      "body": [""],
      "description": "obj 转 json"
    },
    "self_language_toobj": {
      "scope": "",
      "prefix": "toobj",
      "body": [""],
      "description": "json 转 obj"
    },
    "self_language_class_note": {
      "scope": "",
      "prefix": "//class",
      "body": [""],
      "description": "类注释"
    },
    "self_language_method_note": {
      "scope": "",
      "prefix": "//method",
      "body": [""],
      "description": "函数注释"
    }
    // ==============================================================================================
  }
  ```

- 单语言配置

  ```json
  {
    // 自定义单语言常用结构的代码联想
    // ==============================================================================================
    "模板名称": {
      // 模板关键字
      "prefix": "sheader",
      // 模板代码内容
      "body": [""],
      // 模板说明
      "description": "创建一个[main]函数"
    }
    // ==============================================================================================
  }
  ```
