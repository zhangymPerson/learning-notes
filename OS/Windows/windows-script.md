## windows 下脚本编写

**注意：**

- windows 下的脚本都是 用/a /b 等格式的，所以文件路径尽量用 \ 表示

- windows 下 cmd 命令的查看 help 的格式 `cmdname /?` 获取帮助 如： `cd /?` 在 powershell 中不行

- powershell 中查看帮助 `man copy` 或者 `get-help copy`

- bat 脚本中的 `&` 和 `&&` 的区别

  **&** 之后的命令 **无论如何都会被执行**。
  **&&** 之后的命令 **只有在&&之前的命令执行成功**才会被执行。

- 最基本的

  ```bat
  @echo off
  rem 在cmd脚本中表述注释
  rem @echo off 表述不输入echo本身
  echo "启动程序的小脚本"

  rem 启动exe文件使用start命令
  rem 路径不使用 \ 容易被转义
  rem 路径包含中文和空格等字符的无法启动需修改启动路径
  start D:/Users/Administrator/AppData/Roaming/Typeeasy/TypeEasy.exe

  rem pause 命令
  rem 运行 Pause 命令时，将显示下面的消息：
  rem Press any key to continue . . .
  Pause
  ```

- 定义变量

  ```bat
  @echo off
  :: 也可以表示注解
  :: set var=xxx：设置变量var的值是xxx
  set var=我是值
  echo %var%
  :: set /p value=请输入变量的值：意思是定义一个变量value，这个value的值需要在控制台上动态输入
  :: =号右边的是提示语,不是变量的值
  set /p value=请输入变量的值
  :: echo.是换行的意思
  echo.
  echo %value%
  pause
  ```

* 进入其他目录下执行脚本

  ```bat
  @echo off
  :: 测试在其他目录下执行脚本 启动bat脚本 或者 打开exe文件
  cmd /k "cd /d D:/test &&start start.bat"
  cmd /k "cd /d D:/test &&nginx.exe"
  Pause
  ```

  **说明**

  其中：
  `D:/test`是目标路径 即 exe 文件所在路径或要执行的 bat 脚本所在位置

  `java -version`是要执行的命令

  通过`&&`连接 && 和 & 有区别

* 删除文件/文件夹

  ```bat
  ::删除文件和文件夹
  del fileName
  ::删除文件夹
  rd /s /q dirPath
  ```

* 启动 nginx

  脚本文件 必须在 nginx.exe 所在目录

  start.bat

  ```bat
  @echo off
  :: 启动nginx
  tskill nginx
  nginx.exe -t
  nginx.exe -v
  start nginx.exe

  echo "启动成功"
  Pause
  ```

  stop.bat

  ```bat
  @echo off
  :: 关闭nginx
  nginx.exe -s stop
  echo "关闭nginx成功"
  Pause
  ```

  启动脚本 在其他目录下

  nginx.bat

  ```bat
  @echo off
  ::配置nginx.exe所在目录 且自定义有start.bat
  set nginx=D:/soft/nginx
  echo "要启动的的是%nginx%"
  ::进入文件夹并且执行
  cmd /k "cd /d %nginx%&& start.bat"
  echo "启动nginx成功"
  Pause
  ```

* 启动 tomcat

  ```bat
  @echo off
  ::tomcat启动脚本所在位置
  set tomcat=D:\tomcat\bin\startup.bat
  ::启动tomcat需要指定 CATALINA_HOME 位置在tomcat目录下不能包含 ; 或者 \ 结尾
  set CATALINA_HOME=D:\tomcat
  echo "要启动的是%tomcat%"
  start %tomcat%
  echo "%tomcat%启动成功"
  ```

* 复制文件的脚本

  copyfile.bat

  ```bat
  @echo off
  :: 拷贝文件脚本
  set oldpath=d:\test\user\one
  set oldfile=a.txt
  set newpath=d:\test\user\two
  set newfile=bb.txt

  set old=%oldpath%\%oldfile%
  set new=%newpath%\%newfile%

  echo %old% 拷贝到 %new%
  ::含有空格的路径要加引号
  ::执行结果是命令1提示找不到指定的文件，命令2成功执行文件复制，
  ::可能的原因是dos命令中斜杠\用于参数标志了，而且windows的标准路径应该使用的是反斜杠\来分割。
  copy "%old%" "%new%"
  ```

* 复制文件夹的命令的脚本

  ```bat
  @echo off
  echo "替换文件夹下的文件"
  ::拷贝整个文件夹下的内容到另外一个文件中 文件夹都存在，不然执行有问题
  ::/y 不会有提示 否则有各种覆盖和其他提示
  :: xcopy /? 可以查看命令的提示信息
  xcopy D:\test\file\a\*.* D:\test\file\b /s /e /y
  echo 脚本执行完成
  pause
  ```

* 函数的写法

  ```bat
  rem 函数的调用
  call:func
  pause
  rem 函数的定义 :funcname 结尾用 goto:eof
  :func
  echo this is a bat func
  goto:eof
  ```

  带参数的

  ```bat
  @echo off
  call :add 11 12
  echo %n%
  rem 需要加 goto :eof 否则函数会在执行一遍，也可以使用 exit
  goto :eof
  :add
  set /a n=%1+%2
  goto :eof
  ```

  **用%1-%9 表示第一到第九个答参数,在执行完过程后加上 goto :eof 跳到文件尾可以返回到 call 的下一条语句，避免执行到文件结束才返回**

- windows 下打开文件夹的 bat 脚本

  创建 openPath.bat 文件

  编写脚本内容

  ```bat
  REM 打开文件夹 d:/test
  explorer d:\test
  ```

  双击 bat 脚本即可打开该文件夹
