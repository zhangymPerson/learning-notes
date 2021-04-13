# svn 一款代码管理软件 与 git 类似

- [返回](./README.md)

- [教程](https://www.runoob.com/svn/tortoisesvn-intro.html)

- svn 过滤的配置

  右键打开 svn > setting

  在 Setting 中设置 Gloabal ignore，多个过滤通配符用空格分隔，

  ```
  *.o *.lo *.la *.al .libs *.so *.so.[0-9]* *.a *.pyc *.pyo __pycache__ *.rej *~ #*# .#* .*.swp .DS_Store [Tt]humbs.db
  ```

  java 项目过滤的一些内容 主要是针对 eclipse 和 idea 的自动生成文件的

  ```
  .settings .settings/* target target/* .classpath .project *.idea *.iml
  ```
