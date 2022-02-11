# C++

## C++ 编译工具 

### gcc

- gcc 和 g++
  
  gcc 编译c++ 需要指定部分内容，不能直接编译

  如果想使用 gcc 指令来编译执行 C++ 程序，需要在使用 gcc 指令时，手动为其添加 -lstdc++ -shared-libgcc 选项，表示 gcc 在编译 C++ 程序时可以链接必要的 C++ 标准库。也就是说，我们可以这样编译 demo.cpp 文件：

  `[root@bogon ~]# gcc -xc++ demo.cpp -lstdc++ -shared-libgcc`

  默认编译的文件叫 a.out

  g++ 是gcc针对
  ```sh
  g++ demo.cpp
  gcc -xc++ demo.cpp -lstdc++ -shared-libgcc
  ```

### make cmake