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


    声明变量的一般形式是使用 var 关键字：var identifier type

    示例：
    ```go
    var a int
    var b bool
    var str string
    你也可以改写成这种形式：

    //全局变量的声明一般这样写
    var (
        a int
        b bool
        str string
    )
    ```
    
    := 的含义

    ```go
    // = 使用必须使用先var声明例如：
    var a
    a=100
    //或
    var b = 100
    //或
    var c int = 100
    
    // := 是声明并赋值，并且系统自动推断类型，不需要var关键字
    d := 200
    /*
    定义三个变量，它们分别初始化为相应的值
    vname1为v1，vname2为v2，vname3为v3
    然后Go会根据其相应值的类型来帮你初始化它们
    */
    // var vname1, vname2, vname3 = v1, v2, v3
    var number1, number2, number3 = 1, 2, 3

    /*
    定义三个变量，它们分别初始化为相应的值
    vname1为v1，vname2为v2，vname3为v3
    编译器会根据初始化的值自动推导出相应的类型
    */
    // vname1, vname2, vname3 := v1, v2, v3
    number1, number2, number3 := 1, 2, 3
    ```

    **注意：不过它有一个限制，那就是它只能用在函数内部；在函数外部使用则会无法编译通过，所以一般用var方式来定义全局变量。**


- 语句 & 表达式

- 注释

    ```go
    //单行注释
    /*
        多行注释
    */
    ```


## 程序介绍
- 程序入口

    一个项目一个main包和 func main(){} 方法 为入口

- main 启动

    Go语言的包与文件夹是一一对应的，它具有以下几点特性：
        
    - 一个目录下的同级文件属于同一个包。
    - 包名可以与其目录名不同。
    - **main 包是Go语言程序的入口包，一个Go语言程序必须有且仅有一个 main 包。**
    - **如果一个程序没有 main 包，那么编译时将会出错，无法生成可执行文件。**

