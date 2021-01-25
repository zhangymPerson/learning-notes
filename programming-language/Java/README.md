# 此笔记主要记录 Java 开发中遇到的问题

- [返回](../README.md)

## 目录

- [Java-JVM.md](./Java-JVM.md)
- [java-script.md](./java-script.md)
- [javadoc.md](./javadoc.md)
- [Java 中注释规范.md](./Java中注释规范.md)
- [Java 中的注解.md](./Java中的注解.md)
- [Java 中的线程.md](./Java中的线程.md)
- [Java 中编写 jar 脚本.md](./Java中编写jar脚本.md)
- [Java 多线程编程.md](./Java多线程编程.md)
- [Java 经典面试题,.md](./Java经典面试题,.md)
- [JDK.md](./JDK.md)
- [volatile.md](./volatile.md)

## 其他

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

  **windows 下编辑环境变量**

  ```sh
  # 1 新建JAVA_HONE变量
  变量名：JAVA_HOME
  变量值：电脑上JDK安装的绝对路径

  # 2 新建/修改 CLASSPATH 变量

  #如果存在 CLASSPATH 变量，选中点击 Edit(编辑)。

  #如果没有，点击 New（新建）... 新建。

  #输入/在已有的变量值后面添加：

  #变量名：CLASSPATH
  #变量值：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;
  # 3 修改Path 变量
  %JAVA_HOME%\bin
  %JAVA_HOME%\jre\bin
  ```
