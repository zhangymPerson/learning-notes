# 常用的命令

- 检出项目

  svn checkout path(path 是服务器的目录)

- 常用检出命令：

  `svn co http://路径(目录或文件的全路径)　[本地目录全路径] --username 用户名 --password 密码`
  `svn co svn://路径(目录或文件的全路径)　[本地目录全路径] --username 用户名 --password 密码`
  `svn checkout http://路径(目录或文件的全路径)　[本地目录全路径] --username 　用户名`
  `svn checkout svn://路径(目录或文件的全路径)　[本地目录全路径] --username 　用户名`

  **检出命令说明**

  - 如果不带--password 参数传输密码的话，会提示输入密码，建议不要用明文的--password 选项。

  - 其中 username 与 password 前是两个短线，不是一个。

  - 不指定本地目录全路径，则检出到当前目录下。

- 检出指定具体版本：

  `svn co http://路径(目录或文件的全路径)　[本地目录全路径][--revision] --username 用户名 --password 密码`
  `svn checkout svn://路径(目录或文件的全路径)　[本地目录全路径][--revision] --username 　用户名`
  `svn co [--revision] http://路径(目录或文件的全路径)　[本地目录全路径] --username 用户名 --password 密码`
  `svn checkout [--revision] svn://路径(目录或文件的全路径)　[本地目录全路径] --username 　用户名`
  举例如下：
  `svn checkout http://baidu.com/svn/trunk/ username -r version`
  `svn checkout -r version http://baidu.com/svn/trunk/ username`

- 检出不包括源文件夹根目录：

  比如我要 checkout trunk/ 下面的所有文件，但是不包括 trunk 文件夹

  我们可以在 svn 文件夹后面打个空格，在加个“.”就行了

  `svn co http://baidu.com/svn/project/trunk/ /home/path`
  改为:
  `svn co http://baidu.com/svn/project/trunk/ . /home/path/`

- 往版本库中添加新的文件

  `svn add filename`

  例如：
  
  `svn add test.cpp`

- 查看日志

  `svn log path`

- 更新当前目录以及子目录下的所有文件到最新版本

  `svn update`
  `svn up`
