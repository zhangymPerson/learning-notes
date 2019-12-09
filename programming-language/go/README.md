# Go语言学习笔记

- 下载

    安装包下载地址为：https://golang.org/dl/。
    
    如果打不可以使用这个地址：https://golang.google.cn/dl/。

- 安装 

    下载相应的安装包

    解压到指定文件夹并且配置环境变量

    测试命令 `go version`

- helloword

    helloword.go

    ```go
    package main

    import "fmt"

    func main() {
    /* 这是我的第一个简单的程序 */
    fmt.Println("Hello, World!")
    }
    ```

    执行有两种方式 `go run helloword.go` 或者 `go build helloword.go` 生成 helloword 可执行文件 然后直接执行可执行文件 `helloword` 