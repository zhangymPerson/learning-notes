# svn 一款代码管理软件 与git类似

- [教程](https://www.runoob.com/svn/tortoisesvn-intro.html)

- svn 过滤的配置

    右键打开svn > setting 
    
    在Setting中设置Gloabal ignore，多个过滤通配符用空格分隔，
    ```
    *.o *.lo *.la *.al .libs *.so *.so.[0-9]* *.a *.pyc *.pyo __pycache__ *.rej *~ #*# .#* .*.swp .DS_Store [Tt]humbs.db 
    ```
    java 项目过滤的一些内容 主要是针对 eclipse和idea的自动生成文件的
    ```
    .settings .settings/* target target/* .classpath .project *.idea *.iml
    ```