# 此笔记主要记录Java开发中遇到的问题

- 官网

    [官网](https://www.oracle.com/technetwork/java/index.html)

    [下载地址](https://www.oracle.com/technetwork/java/javase/downloads/index.html)


- 环境变量

    **linux 下 /etc/profile**
    ```sh
    export JAVA_HOME=/*/*/jdk*
    export JRE_HOME=${JAVA_HOME}/jre  
    export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib  
    export PATH=$JAVA_HOME/bin:$PATH
    ```

    **windows下编辑环境变量**
    ```
    # 1 新建JAVA_HONE变量
    变量名：JAVA_HOME
    变量值：电脑上JDK安装的绝对路径

    # 2 新建/修改 CLASSPATH 变量

    #如果存在 CLASSPATH 变量，选中点击 Edit(编辑)。

    #如果没有，点击 New（新建）... 新建。

    #输入/在已有的变量值后面添加：

    变量名：CLASSPATH
    变量值：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;
    # 3 修改Path 变量
    %JAVA_HOME%\bin
    %JAVA_HOME%\jre\bin
    ```

