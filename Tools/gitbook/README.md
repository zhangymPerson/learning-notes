# Gitbook 的搭建和使用

## 目录

- [返回](../README.md)

## 其他

## 简介

- [官网](https://www.gitbook.com/)

- [百度百科](https://baike.baidu.com/item/GitBook/17969908?fr=aladdin)

  GitBook 是一个基于 Node.js 的命令行工具，可使用 Github/Git 和 Markdown 来制作精美的电子书，GitBook 并非关于 Git 的教程。

- 安装

  gitbook 依赖于 nodejs

  安装命令 `npm install gitbook-cli -g`

- 使用

  `gitbook -V` 检查安装是否成功

  创建 book 文件夹 并进入文件夹

  `gitbook init` 初始化一个项目

  > 至少需要一个 README 和 SUMMARY 文件来构建一本书

  `gitbook build` 只创建页面文件(html)

  `gitbook serve` 提供服务 默认接口 4000

  `gitbook serve --port 8080` 指定提供服务的端口 8080 默认接口 4000

- 配置

  所有的配置都以 JSON 格式存储在名为 book.json 的文件中。

  自己创建这个文件 在 项目根目录下 创建即可

  配置举例

  ```json
  {
    "title": "danao learnging-notes",
    "author": "zhangyanming",
    "description": "learning-note",
    "language": "zh-hans",
    "gitbook": "3.2.3",
    "styles": {},
    "structure": {
      "readme": "README.md"
    },
    "links": {
      "sidebar": {
        "项目github地址": "https://github.com/zhangymPerson/learning-notes",
        "项目gitee地址": "https://gitee.com/ZhangYanMingGood/learning-notes"
      }
    },
    "plugins": [],
    "pluginsConfig": {}
  }
  ```

  `title` - 本书标题

  `author` - 本书作者

  `description` - 本书描述

  `language` - 本书语言，中文设置 "zh-hans" 即可

  `gitbook` - 指定使用的 GitBook 版本

  `styles` - 自定义页面样式

  `structure` - 指定 Readme、Summary、Glossary 和 Languages 对应的文件名

  `links` - 在左侧导航栏添加链接信息

  `plugins` - 配置使用的插件

  `pluginsConfig` - 配置插件的属性

  `SUMMARY.md` - 这个文件主要决定 GitBook 的章节目录，它通过 Markdown 中的列表语法来表示文件的父子关系，简单示例：

  ```md
  # Summary

  - [Introduction](README.md)
  - [Part I](part1/README.md)
    - [Writing is nice](part1/writing.md)
    - [GitBook is nice](part1/gitbook.md)
  - [Part II](part2/README.md)
    - [We love feedback](part2/feedback_please.md)
    - [Better tools for authors](part2/better_tools.md)
  ```
