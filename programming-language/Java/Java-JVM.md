# java 虚拟机

- [返回](../README.md)
- 概念

  JVM 是 Java Virtual Machine（Java 虚拟机）的缩写，JVM 是一种用于计算设备的规范，它是一个虚构出来的计算机，是通过在实际的计算机上仿真模拟各种计算机功能来实现的。

  [百度百科](https://baike.baidu.com/item/JVM/2902369)

### JRE JDK 和 JVM 区分

- JRE

  JRE(JavaRuntimeEnvironment，Java 运行环境)，也就是 Java 平台。所有的 Java 程序都要在 JRE 下才能运行。普通用户只需要运行已开发好的 java 程序，安装 JRE 即可。

- JDK

  JDK(Java Development Kit)是程序开发者用来来编译、调试 java 程序用的开发工具包。JDK 的工具也是 Java 程序，也需要 JRE 才能运行。为了保持 JDK 的独立性和完整性，在 JDK 的安装过程中，JRE 也是 安装的一部分。所以，在 JDK 的安装目录下有一个名为 jre 的目录，用于存放 JRE 文件。

- JVM

  JVM(JavaVirtualMachine，Java 虚拟机)是 JRE 的一部分。它是一个虚构出来的计算机，是通过在实际的计算机上仿真模拟各种计算机功能来实现的。JVM 有自己完善的硬件架构，如处理器、堆栈、寄存器等，还具有相应的指令系统。Java 语言最重要的特点就是跨平台运行。使用 JVM 就是为了支持与操作系统无关，实现跨平台。

## JVM 的分析

### 运行时 数据区域

- 程序计数器

- Java 虚拟机栈

  栈是线程私有的；

  局部变量表存放着基本数据类型(8 种)和对象的引用(reference 类型，可以裂解为指向对象起始位置的引用指针，也可能指向对象的句柄)

  异常有 StackOverflowError 和 OutOfMemoryError 异常

- 本地方法栈

  本地方法执行的是 native 方法

  没有具体的规定实现方式

- 堆

  Java 中的堆是 Java 虚拟机中的管理的内存中最大的一块，Java 堆是被所有线程共享的一块内存区域

  此内存唯一的目的是存放对象实例

  Java 中的堆是垃圾收集管理器的只要区域，有时候也叫 GC 堆

  大部分收集器基本采用分代收集法：新生代和老年代

  会抛出 OutOfMemoryError 异常

- 方法区

  和堆一样，线程共享区域，用于存储 类信息，常量，静态变量，代码等数据； 也称 永久带

  会抛出 OutOfMemoryError 异常

- 运行时常量池

  方法区的一部分，类除了有方法区中的信息，

  还有一项信息是常量池，用于存放编译时期生成的各种字面量和符号引用；这部分内容将在类加载后进入方法区运行时常量池中存放

- 直接内存

### 垃圾回收器

- GC(Garbage Collection)

#### 判断对象的存活

- 引用计数法

- 可达性分析算法

### 垃圾回收算法

- 标记-清除算法

- 复制算法

- 标记-整理算法

- 分代收集算法

--- 以上内容基于 深入理解 java 虚拟机 ---

## jdk 相关的命令工具行

- [JVM 性能调优监控工具 jps、jstack、jmap、jhat、jstat、hprof 使用详解](https://my.oschina.net/feichexia/blog/196575)

### jps 虚拟机进程状况工具

- 类似 linux 的 ps 命令 JVM process Status

  jps 时 Java 性能分析的首要工具，确认 Java 进程的进程 id

  jps -l 输出主类的全名

  jps -v 输出虚拟机启动时的参数

### jstat 虚拟机统计信息监视工具

- 命令格式

  jstat [-命令选项] [vmid] [间隔时间/毫秒] [查询次数]

option： 参数选项

    -t： 可以在打印的列加上Timestamp列，用于显示系统运行的时间

    -h： 可以在周期性数据数据的时候，可以在指定输出多少行以后输出一次表头

    vmid： Virtual Machine ID（ 进程的 pid）

    interval： 执行每次的间隔时间，单位为毫秒

    count： 用于指定输出多少次记录，缺省则会一直打印

    -class                 显示ClassLoad的相关信息；

    -compiler           显示JIT编译的相关信息；

    -gc                     显示和gc相关的堆信息；

    -gccapacity 　　  显示各个代的容量以及使用情况；

    -gcmetacapacity 显示metaspace的大小

    -gcnew               显示新生代信息；

    -gcnewcapacity  显示新生代大小和使用情况；

    -gcold                 显示老年代和永久代的信息；

    -gcoldcapacity    显示老年代的大小；

    -gcutil　　           显示垃圾收集信息；

    -gccause             显示垃圾回收的相关信息（通-gcutil）,同时显示最后一次或当前正在发生的垃圾回收的诱因；

    -printcompilation 输出JIT编译的方法信息；

### jinfo java 配置信息工具

### jmap Java 内存映像工具

### jhat 虚拟机堆转储快照分析工具

### jstack Java 堆栈跟踪工具

### hsdic jit 生成代码反汇编
