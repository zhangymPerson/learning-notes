# 线程

- 线程，有时被称为轻量进程

线程是程序中一个单一的顺序控制流程。进程内有一个相对独立的、可调度的执行单元，是系统独立调度和分派CPU的基本单位指令运行时的程序的调度单位。在单个程序中同时运行多个线程完成不同的工作，称为多线程。


线程是进程中的实体，一个进程可以拥有多个线程，一个线程必须有一个父进程。线程不拥有系统资源，只有运行必须的一些数据结构；它与父进程的其它线程共享该进程所拥有的全部资源。线程可以创建和撤消线程，从而实现程序的并发执行。一般，线程具有就绪、阻塞和运行三种基本状态。

线程在程序中是独立的、并发的执行路径，每个线程有它自己的堆栈、自己的程序计数器和自己的局部变量。但是，与分隔的进程相比，进程中的线程之间的隔离程度要小。它们共享内存、文件句柄和其它每个进程应有的状态。

## 线程的状态




## Java中线程的相关方法


### 继承Thread类

- 简单代码
```java
class MyThread extends Thread{
    private static int num = 0;
     
    public MyThread(){
        num++;
    }
     
    @Override
    public void run() {
        System.out.println("主动创建的第"+num+"个线程");
    }
}


Thread.currentThread().getId() //获取线程id
```

注意:

**线程启动需要使用调用 start() 方法,如果使用 run()方法则线程使用的是主线程,并没有新启动线程**

### 实现Runable接口

- 简单代码

```java

class MyRunnable implements Runnable{
     
    public MyRunnable() {
         
    }
     
    @Override
    public void run() {
        System.out.println("子线程ID："+Thread.currentThread().getId());
    }
}

public class Test {
    public static void main(String[] args)  {
        System.out.println("主线程ID："+Thread.currentThread().getId());
        MyRunnable runnable = new MyRunnable();
        Thread thread = new Thread(runnable);
        thread.start();
    }
}

```



## 线程池概念

- 线程池（英语：thread pool）

    一种线程使用模式。线程过多会带来调度开销，进而影响缓存局部性和整体性能。而线程池维护着多个线程，等待着监督管理者分配可并发执行的任务。这避免了在处理短时间任务时创建与销毁线程的代价。线程池不仅能够保证内核的充分利用，还能防止过分调度。可用线程数量应该取决于可用的并发处理器、处理器内核、内存、网络sockets等的数量。 例如，线程数一般取cpu数量+2比较合适，线程数过多会导致额外的线程切换开销。

- 重要的几个概念

　　1.线程池状态

　　2.任务的执行

　　3.线程池中的线程初始化

　　4.任务缓存队列及排队策略

　　5.任务拒绝策略

　　6.线程池的关闭

　　7.线程池容量的动态调整
