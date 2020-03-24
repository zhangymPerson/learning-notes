## windows下脚本编写

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

- 启动nginx

    ```bat
    @echo off
    ::自己本地nginx.exe文件路径
    set nginx=D:\nginx.exe
    echo "要启动的的是%nginx%"
    start %nginx%
    echo "启动nginx成功"
    ```

- 启动tomcat

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