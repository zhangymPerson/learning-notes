# 学习笔记

- 中文文档

  https://www.kotlincn.net/docs/reference/

## 踩坑记录

- 在 Java 中可变参数是可以直接传递，并且可以和数组相互转换传递：

  kotlin 中的可变参数传入 使用 \*args

  ```kotlin
  fun main() {
      foo("1", "2", "3")
  }

  fun foo(vararg args: String) {
      //不能使用 args 报错
      //要使用 *args
      bar1(*args)
      bar2(args)
  }
  //可变参数函数
  fun bar1(vararg args: String) {
      println(args.contentToString())
  }

  fun bar2(args: Array<out String>) {
      bar1(*args)
  }
  ```

- kotlin 中的 Object 类型是 Any 类型

- kotlin 调用 java 中的方法时，类型是 Class<?> classType

  传值方式 类名::class.java

  ```java
  //Java中的方法
  public String funcName(Class<?> classType) {
      return classType.getName();
  }
  ```

  ```kotlin
  //语法格式是： 类名::class.java
  var arg = Obj().funcName(ClassName::class.java)
  ```
