# C++

- [返回](./README.md)

## 代码

### 基本语法省略

### 头文件

- 头文件

  头文件(.h)：

  写类的声明包括类里面的成员和方法的声明）、函数原型、#define 常数等，但一般来说不写出具体的实现。

  在写头文件时需要注意，在开头和结尾处必须按照如下样式加上预编译语句（如下）：

  ```c++
  #ifndef CIRCLE_H
  #define CIRCLE_H

  //你的代码写在这里

  #endif
  ```

  这样做是为了防止重复编译，不这样做就有可能出错。

## C++ 编译工具

- 构建工具 Cmake bazel

## 编译过程

- 概念

  编译是将代码翻译成机器语言的过程：每一个 cpp 源码文件对应一个编译单元，即每一个 cpp 源文件会生成一个对应的目标文件(.o 结尾)，再经过一系列的链接操作，生成最终的应用程序。

- demo.cpp 演示

  // 执行 gcc 命令生成应用程序
  // demo
  $ gcc -o demo demo.cpp

  $ ./demo
  Hello World

  // 添加-v 参数可以输出完整的编译过程，过滤掉冗余信息
  $ gcc -o demo demo.cpp -v

### 编译阶段

预处理阶段 -> 编译阶段 -> 汇编阶段 -> 链接阶段

- 预处理阶段

  该阶段编译器对源文件做展开处理，包括:

  将#include 的头文件展开

  将#define 语句指定的值转换为变量

  将将宏定义转换为具体代码

  根据#if #elif 和#endif 指定的位置包含或排除特定部分的代码

  `gcc -E demo.cpp -o demo.i`

  `cpp demo.cpp > demo.i`

- 编译阶段

  该阶段对展开后的源文件 demo.i 进行语法检查，确认代码是否满足语言相关的语法规则，检查通过后生成汇编文件 demo.s

  `$ gcc -S demo.cpp -o demo.s`

- 汇编阶段

  该阶段汇编器将汇编文件转换为机器可以执行的指令，生成目标文件 demo.o

  `$ gcc -c demo.s -o demo.o`
  或者
  `$ as demo.s -o demo.o`

- 链接阶段

  示例 demo.cpp 文件中调用了 printf 函数，目标文件 demo.o 中引用的 printf 符号还未解析，demo.o 还无法正常运行，还需要将系统运行库 libc 和相关的启动文件(crt 文件)链接在一起，才能生成最终可执行的程序 demo

### gcc

- gcc 和 g++

  gcc 编译 c++ 需要指定部分内容，不能直接编译

  如果想使用 gcc 指令来编译执行 C++ 程序，需要在使用 gcc 指令时，手动为其添加 -lstdc++ -shared-libgcc 选项，表示 gcc 在编译 C++ 程序时可以链接必要的 C++ 标准库。也就是说，我们可以这样编译 demo.cpp 文件：

  `[root@bogon ~]# gcc -xc++ demo.cpp -lstdc++ -shared-libgcc`

  默认编译的文件叫 a.out

  g++ 是 gcc 针对

  ```sh
  g++ demo.cpp
  gcc -xc++ demo.cpp -lstdc++ -shared-libgcc
  ```

### make cmake

- [cmake](./cmake.md)
