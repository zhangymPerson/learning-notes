# Go语言学习笔记
## 目录
- [code.md](./code.md)
- [go-error.md](./go-error.md)
- [GOROOT-GOPATH.md](./GOROOT-GOPATH.md)
- [go_mod.md](./go_mod.md)
- [go_oop.md](./go_oop.md)

## 其他
- [《The Way to Go》中文译本，中文正式名《Go 入门指南》](https://github.com/unknwon/the-way-to-go_ZH_CN)

- [Go语言圣经-源代码](https://github.com/adonovan/gopl.io/)

- [Go中文api说明](https://go-zh.org/doc/)

- [Go的中文api](https://studygolang.com/pkgdoc)

- 下载

    安装包下载地址为：https://golang.org/dl/。
    
    如果打不可以使用这个地址：https://golang.google.cn/dl/。

- 安装 

    下载相应的安装包

    解压到指定文件夹并且配置环境变量

    测试命令 `go version`


- 安装目录

    你的 Go 安装目录（环境变量`$GOROOT`）的文件夹结构应该如下所示：

    README.md, AUTHORS, CONTRIBUTORS, LICENSE

    - /bin：包含可执行文件，如：编译器，Go 工具
    - /doc：包含示例程序，代码工具，本地文档等
    - /lib：包含文档模版
    - /misc：包含与支持 Go 编辑器有关的配置文件以及 cgo 的示例
    - /os_arch：包含标准库的包的对象文件（.a）
    - /src：包含源代码构建脚本和标准库的包的完整源代码（Go 是一门开源语- 言）
    - /src/cmd：包含 Go 和 C 的编译器和命令行脚本

- helloword

    helloword.go

    ```go
    //必须是main
    package main

    import "fmt"
    //启动函数
    func main() {
    /* 这是我的第一个简单的程序 */
        fmt.Println("Hello, World!")
    }
    ```

    执行有两种方式 `go run helloword.go` 或者 `go build helloword.go` 生成 helloword 可执行文件 然后直接执行可执行文件 `helloword` 

- 文件扩展名与包（package）：

    Go 语言源文件的扩展名很显然就是 .go。

    C 文件使用后缀名 .c，汇编文件使用后缀名 .s。所有的源代码文件都是通过包（packages）来组织。包含可执行代码的包文件在被压缩后使用扩展名 .a（AR 文档）。

    Go 语言的标准库（第 9.1 节）包文件在被安装后就是使用这种格式的文件。

    **注意 当你在创建目录时，文件夹名称永远不应该包含空格，而应该使用下划线 "_" 或者其它一般符号代替。**

- command

    go build 编译自身包和依赖包

    go install 编译并安装自身包和依赖包

- 代码风格统一 官方格式化工具

    Go 开发团队不想要 Go 语言像许多其它语言那样总是在为代码风格而引发无休止的争论，浪费大量宝贵的开发时间，因此他们制作了一个工具：go fmt（gofmt）。这个工具可以将你的源代码格式化成符合官方统一标准的风格，属于语法风格层面上的小型重构。遵循统一的代码风格是 Go 开发中无可撼动的铁律，因此你必须在编译或提交版本管理系统之前使用 gofmt 来格式化你的代码。

    在命令行输入 
    
    - `gofmt –w program.go` 会格式化该源文件的代码然后将格式化后的代码覆盖原始内容（如果不加参数 -w 则只会打印格式化后的结果而不重写文件）；
    
    - `gofmt -w *.go` 会格式化并重写所有 Go 源文件；
    
    - `gofmt map1` 会格式化并重写 map1 目录及其子目录下的所有 Go 源文件。

- 文件名命名要求

    Go 的源文件以 .go 为后缀名存储在计算机中，这些文件名均由小写字母组成，如 scanner.go 。如果文件名由多个部分组成，则使用下划线 _ 对它们进行分隔，如 scanner_test.go 。文件名不包含空格或其他特殊字符。

    一个源文件可以包含任意多行的代码，Go 本身没有对源文件的大小进行限制。

- 注意事项

    不能 import 没有用到的包 否则报错
    **如果你导入了一个包却没有使用它，则会在构建程序时引发错误，如 imported and not used: os，这正是遵循了 Go 的格言：“没有不必要的代码！“。**

- go语言模块下载更新失败的问题(修改go语言的代理)

    [Goproxy 中国说明](https://github.com/goproxy/goproxy.cn/blob/master/README.zh-CN.md)

    推荐使用的两个, goproxy.cn 和 goproxy.io
    https://goproxy.cn
    https://goproxy.io

- 设置代理方式

    Go 1.13 及以上（推荐）

    七牛云代理 - https://goproxy.cn/

    阿里云的代理源 - GOPROXY=https://mirrors.aliyun.com/goproxy/

    打开你的终端并执行：

    `$ go env -w GOPROXY=https://goproxy.cn,direct`
    
    完成。

    macOS 或 Linux
    
    打开你的终端并执行：

    `$ export GOPROXY=https://goproxy.cn`

    或者

    `$ echo "export GOPROXY=https://goproxy.cn" >> ~/.profile && source ~/.profile`

    完成。

    Windows

    打开你的 PowerShell 并执行：

    `C:\> $env:GOPROXY = "https://goproxy.cn"`
    
    或者
    ```
    1. 打开“开始”并搜索“env”
    2. 选择“编辑系统环境变量”
    3. 点击“环境变量…”按钮
    4. 在“<你的用户名> 的用户变量”章节下（上半部分）
    5. 点击“新建…”按钮
    6. 选择“变量名”输入框并输入“GOPROXY”
    7. 选择“变量值”输入框并输入“https://goproxy.cn”
    8. 点击“确定”按钮
    ```