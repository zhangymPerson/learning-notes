# GOROOT GOPATH 理解

>不同于其他语言，go中没有项目的说法，只有包, 其中有两个重要的路径，GOROOT 和 GOPATH

>GOROOT是安装目录，GOPATH是我们的工作空间, 用来存放包的目录


## GOROOT

- GOROOT就是go的安装路径

## GOPATH配置的理解

- go install/go get和 go的工具等会用到GOPATH环境变量.

- GOPATH是作为编译后二进制的存放目的地和import包时的搜索路径 (其实也是你的工作目录, 你可以在src下创建你自己的go源文件, 然后开始工作)。

- GOPATH之下主要包含三个目录: bin、pkg、src

    bin目录主要存放可执行文件; 

    pkg目录存放编译好的库文件, 主要是*.a文件; 

    src目录下主要存放go的源文件

- 不要把GOPATH设置成go的安装路径,

    可自定义位置

- **注意：GOPATH和GOROOT不能设置成一样的，否则会报错**

    `$GOPATH must not be set to $GOROOT`

    个人项目依赖包不应该和go的标准库放一起
    Because /usr/local/go/src already contains the code for the standard library, and you should keep your own code separate from that.

    I know, other development tools would have no problem with that, but Go is a little more strict in some ways. It's probably the same philosophy that lies behind flagging unused variables or imports as errors - avoiding problems which may seem small at first, but can lead to bigger headaches in the future.
## 查看命令

- `go env`

    查看配置列表


## Go使用github上的开源包的方式

- 前提

    - 前提是配好go的环境变量，包括GOROOT和GOPATH。

    - 需要安装与远程包匹配的代码管理工具，如 Git、SVN、HG 等，参数中需要提供一个包名。

- 命令 `go get projectname-url`

    go get github.com/auth/projectname

    - 网站域名：表示代码托管的网站，类似于电子邮件 @ 后面的服务器地址。

    - 作者或机构：表明这个项目的归属，一般为网站的用户名，如果需要找到这个作者下的所有项目，可以直接在网站上通过搜索“域名/作者”进行查看。这部分类似于电子邮件 @ 前面的部分。

    - 项目名：每个网站下的作者或机构可能会同时拥有很多的项目，图中标示的部分表示项目名称。
    
    go get 使用时的附加参数
    
    使用 go get 时可以配合附加参数显示更多的信息及实现特殊的下载和安装操作，详见下表所示。

    go get 使用时的附加参数
    |附加参数|备  注|
    |-|-|
    |-v|显示操作流程的日志及信息，方便检查错误
    |-u|下载丢失的包，但不会更新已经存在的包
    |-d|只下载，不安装
    |-insecure|允许使用不安全的 HTTP 方式进行下载操作


- Go 环境变量

    Go 开发环境依赖于一些操作系统环境变量，你最好在安装 Go 之前就已经设置好他们。如果你使用的是 Windows 的话，你完全不用进行手动设置，Go 将被默认安装在目录 c:/go 下。这里列举几个最为重要的环境变量：

    
    $GOROOT 表示 Go 在你的电脑上的安装位置，它的值一般都是 $HOME/go，当然，你也可以安装在别的地方。
    
    $GOARCH 表示目标机器的处理器架构，它的值可以是 386、amd64 或 arm。
    
    $GOOS 表示目标机器的操作系统，它的值可以是 darwin、freebsd、linux 或 windows。
    
    $GOBIN 表示编译器和链接器的安装位置，默认是 $GOROOT/bin，如果你使用的是 Go 1.0.3 及以后的版本，一般情况下你可以将它的值设置为空，Go 将会使用前面提到的默认值。
    
    目标机器是指你打算运行你的 Go 应用程序的机器。

    Go 编译器支持交叉编译，也就是说你可以在一台机器上构建运行在具有不同操作系统和处理器架构上运行的应用程序，也就是说编写源代码的机器可以和目标机器有完全不同的特性（操作系统与处理器架构）。

    为了区分本地机器和目标机器，你可以使用 $GOHOSTOS 和 $GOHOSTARCH 设置本地机器的操作系统名称和编译体系结构，这两个变量只有在进行交叉编译的时候才会用到，如果你不进行显示设置，他们的值会和本地机器（$GOOS 和 $GOARCH）一样。

    $GOPATH 默认采用和 $GOROOT 一样的值，但从 Go 1.1 版本开始，你必须修改为其它路径。它可以包含多个 Go 语言源码文件、包文件和可执行文件的路径，而这些路径下又必须分别包含三个规定的目录：src、pkg 和 bin，这三个目录分别用于存放源码文件、包文件和可执行文件。
    
    $GOARM 专门针对基于 arm 架构的处理器，它的值可以是 5 或 6，默认为 6。
    
    $GOMAXPROCS 用于设置应用程序可使用的处理器个数与核数，详见第 14.1.3 节。
 