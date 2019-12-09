# GO

## 程序组成

- 包声明

    ```go
    package packageName
    ```

    **注意：包名和文件名无关 一个文件夹内的代码必须为一个包名 否则编译报错**
- 引入包

    ```go
    import (
        "fmt"
        "./filepath"
    )
    ```
    **import为() 一个包换一行 可以是文件夹路径**
- 函数

    ```go
    func FunctionNane(a,b int) int {
        return a + b
    }

    func function_name( [parameter list] ) [return_types] {
        //函数体
    }
    ```

    说明：
    
    - func：函数由 func 开始声明

    - function_name：函数名称，函数名和参数列表一起构成了函数签名。
    - parameter list：参数列表，参数就像一个占位符，当函数被调用时，你可以将值传递给参数，这个值被称为实际参数。参数列表指定的是参数类型、顺序、及参数个数。参数是可选的，也就是说函数也可以不包含参数。
    - return_types：返回类型，函数返回一列值。return_types 是该列值的数据类型。有些功能不需要返回值，这种情况下 return_types 不是必须的。
    - 函数体：函数定义的代码集合。

    函数可以返回多个值

    

    **注意：错误语法格式**
    ```go
    func main()  
    {  // 错误，{ 不能在单独的行上
        fmt.Println("Hello, World!")
    }
    ```

- 变量

- 语句 & 表达式

- 注释

## 程序介绍
- 程序入口

    一个项目一个main包和 func main(){} 方法 为入口


