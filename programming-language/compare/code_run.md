# 各种语言运行原理浅析

## c/c++

C语言运行

- 编写源代码

    编写.c/.cpp文件 包含相应的业务逻辑

- 编译代码

    初步校验代码

    生成编译文件 *.obj 和 *.o
- 链接

    生成可执行文件 .exe 和 .sh

## Java
Java语言运行原理

- 编写源代码

    编写 .java 文件

- 编译

    `javac`  命令编译.java源文件 编译成 .class文件

    - 分析和输入到符号表

    - 注解处理

    - 语义分析和生成class文件

    `java -verbose **.java`  表示会输出编译器正在执行的操作的消息

    `javap` 是jdk自带的反解析工具。
    
    它的作用就是根据class字节码文件，反解析出当前类对应的code区（汇编指令）、本地变量表、异常表和代码行偏移量映射表、常量池等等信息。

    [Java编译输出简单测试](#Java编译输出简单测试)
-

## python

## javascript

## Go


### 调试过程

#### Java编译输出简单测试

- 编写源代码

    ```java
    //HelloWord.java file
    public class HelloWord{
        public static void main(String[] args) {
            //test [javac HelloWord.java] command and  [javac -verbose HelloWord.java]
            System.out.println("test");
        }
    }
    ```

- 在类所在目录下执行  编译过程简单查看方式

    > 提前配置环境变量 `java -version` 有输出

    `javac HelloWord.java` 生成HelloWord.class文件

    `javac -verbose HelloWord.java` 

    ```log
    PS D:\test\java> javac -verbose .\HelloWord.java
    [解析开始时间 RegularFileObject[.\HelloWord.java]]
    [解析已完成, 用时 22 毫秒]
    [源文件的搜索路径: .]
    [类文件的搜索路径: C:\Program Files\Java\jdk1.8.0_131\jre\lib\resources.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\rt.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\sunrsasign.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\jsse.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\jce.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\charsets.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\jfr.jar,C:\Program Files\Java\jdk1.8.0_131\jre\classes,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\access-bridge-64.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\cldrdata.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\dnsns.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\jaccess.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\jfxrt.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\localedata.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\nashorn.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\sunec.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\sunjce_provider.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\sunmscapi.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\sunpkcs11.jar,C:\Program Files\Java\jdk1.8.0_131\jre\lib\ext\zipfs.jar,.]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Object.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/String.class)]]
    [正在检查HelloWord]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/io/Serializable.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/AutoCloseable.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Byte.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Character.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Short.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Long.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Float.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Integer.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Double.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Boolean.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Void.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/System.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/io/PrintStream.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Appendable.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/io/Closeable.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/io/FilterOutputStream.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/io/OutputStream.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/io/Flushable.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/Comparable.class)]]
    [正在加载ZipFileIndexFileObject[C:\Program Files\Java\jdk1.8.0_131\lib\ct.sym(META-INF/sym/rt.jar/java/lang/CharSequence.class)]]
    [已写入RegularFileObject[.\HelloWord.class]]
    [共 249 毫秒]
    ```

- Java class 反解析查看

    > `javap` 命令

    `java -c -l HelloWord.class` 查看更清晰

    `javap -c .\HelloWord.class` 反汇编代码查看
    ```log
    Compiled from "HelloWord.java"
    public class HelloWord {
    public HelloWord();
        Code:
        0: aload_0
        1: invokespecial #1                  // Method java/lang/Object."<init>":()V
        4: return

    public static void main(java.lang.String[]);
        Code:
        0: getstatic     #2                  // Field java/lang/System.out:Ljava/io/PrintStream;
        3: ldc           #3                  // String test
        5: invokevirtual #4                  // Method java/io/PrintStream.println:(Ljava/lang/String;)V
        8: return
    }
    ```
