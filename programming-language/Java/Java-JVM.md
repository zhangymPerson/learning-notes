# java虚拟机

- 概念

    JVM是Java Virtual Machine（Java虚拟机）的缩写，JVM是一种用于计算设备的规范，它是一个虚构出来的计算机，是通过在实际的计算机上仿真模拟各种计算机功能来实现的。

    [百度百科](https://baike.baidu.com/item/JVM/2902369)

### JRE JDK 和 JVM区分

- JRE

    JRE(JavaRuntimeEnvironment，Java运行环境)，也就是Java平台。所有的Java 程序都要在JRE下才能运行。普通用户只需要运行已开发好的java程序，安装JRE即可。

- JDK

    JDK(Java Development Kit)是程序开发者用来来编译、调试java程序用的开发工具包。JDK的工具也是Java程序，也需要JRE才能运行。为了保持JDK的独立性和完整性，在JDK的安装过程中，JRE也是 安装的一部分。所以，在JDK的安装目录下有一个名为jre的目录，用于存放JRE文件。

- JVM

    JVM(JavaVirtualMachine，Java虚拟机)是JRE的一部分。它是一个虚构出来的计算机，是通过在实际的计算机上仿真模拟各种计算机功能来实现的。JVM有自己完善的硬件架构，如处理器、堆栈、寄存器等，还具有相应的指令系统。Java语言最重要的特点就是跨平台运行。使用JVM就是为了支持与操作系统无关，实现跨平台。

## jdk相关的命令工具行

- [JVM性能调优监控工具jps、jstack、jmap、jhat、jstat、hprof使用详解](https://my.oschina.net/feichexia/blog/196575)

### jps 虚拟机进程状况工具

- 类似linux的ps命令 JVM process Status

    jps时Java性能分析的首要工具，确认Java进程的进程id

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



### jinfo java配置信息工具


### jmap Java内存映像工具

### jhat 虚拟机堆转储快照分析工具

### jstack Java堆栈跟踪工具

### hsdic jit生成代码反汇编
