# 创建项目目录

- 测试项目 测试 apidoc 的使用

- 源码目录 src

- 在当前目录下执行

  `apidoc -i src/ -o out/` 即可生成 api 文档

  windows 下 `apidoc.cmd -i src/ -o out/`

  多语言编程时，需指定 文件类型 `-f` 参数
  `apidoc.cmd -i src/ -o out/ -f .js`

- apidoc.json 说明
