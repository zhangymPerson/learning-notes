# cmake 构建工具

- [返回](./README.md)

## 什么是 cmake

- [官网](https://cmake.org/)

- [百度百科](https://baike.baidu.com/item/cmake/7138032)

  CMake 是一个跨平台的安装（编译）工具，可以用简单的语句来描述所有平台的安装(编译过程)。他能够输出各种各样的 makefile 或者 project 文件，能测试编译器所支持的 C++特性,类似 UNIX 下的 automake。只是 CMake 的组态档取名为 CMakeLists.txt。

## 使用方式

- 编写 main.cc 文件

  ```c++
  #include <iostream>

  int main(int argc, char *argv[])
  {
  std::cout << "Hello CMake!" << std::endl;
  return 0;
  }
  ```

- 编写 makefile 的构建文件

  首先编写 CMakeLists.txt 文件，并保存在与 main.cc 源文件同个目录下：

  ```makefile
  # CMake 最低版本号要求
  cmake_minimum_required (VERSION 2.8)

  # 项目信息
  project (Demo1)

  # 指定生成目标
  add_executable(Demo main.cc)
  ```

- 说明:

  CMakeLists.txt 的语法比较简单，由命令、注释和空格组成，其中命令是不区分大小写的。符号 # 后面的内容被认为是注释。命令由命令名称、小括号和参数组成，参数之间使用空格进行间隔。

  对于上面的 CMakeLists.txt 文件，依次出现了几个命令：

  cmake_minimum_required：指定运行此配置文件所需的 CMake 的最低版本；

  project：参数值是 Demo1，该命令表示项目的名称是 Demo1 。

  add_executable： 将名为 main.cc 的源文件编译成一个名称为 Demo 的可执行文件。

  编译项目之后，在当前目录执行 cmake . ，得到 Makefile 后再使用 make 命令编译得到 Demo1 可执行文件。

## 学习参考资源

- [cmake 中文资源](https://github.com/fenneishi/CMake-Summary-of-documentation-chinese-)

- [awesome-cmake](https://github.com/onqtam/awesome-cmake)

- [cmake-demo-test](https://github.com/ttroy50/cmake-examples)
