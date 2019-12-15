# GO的包管理

>Go Module是Go会在1.12中正式推出的包管理机制。

- go mod

    不同于以往基于GOPATH和Vendor的构建方式，其主要是通过GOPATH/pkg/mod下的缓存包来对工程进行构建。

    在Go 1.11中已经可以使用，同以往新添加的功能一样，

    go mod 可以通过GO111MODULE来控制是否启用，GO111MODULE有一下三种类型。

    - on 所有的构建，都使用Module机制

    - off 所有的构建，都不使用Module机制，而是使用GOPATH和Vendor

    - auto 在GOPATH下的工程，不使用Module机制，不在GOPATH下的工程使用

- go mod 是打包自己的项目

- 使用方式

    ```
    go mod init {项目名}

    例：
    $ go mod init mod_demo
    go: creating new go.mod: module mod_demo
    ```

- 配置内容

    go.mod 文件的配置

    go.mod 文件中用到的关键字有三个

    - require：引用哪些包
    - replace：替换一些包的下载和引用路径
    - exclude：不下载和引用哪些包

- require

    一般来说，require () 是不需要自己手动去修改的，当运行代码的时候，会根据代码中用到的包自动去下载导入

- replace

    在我看来，replace 对于国内开发来说是个神功能，他可以将代码中使用，但国内被墙的代码替换成github上的下载路径，例如：golang.org/x/ 下的包，全都替换成github地址上的包，版本使用 latest 即可

    ```go.mod
    module mod_demo

    go 1.12

    replace (
        golang.org/x/net => github.com/golang/net latest
        golang.org/x/tools => github.com/golang/tools latest
        golang.org/x/crypto => github.com/golang/crypto latest
        golang.org/x/sys => github.com/golang/sys latest
        golang.org/x/text => github.com/golang/text latest
        golang.org/x/sync => github.com/golang/sync latest
    )
    ```

- exclude

    这个不常用，意在指定的包，在下载和引用时，排除掉。

- 书写方式

    go.mod文件还可以指定要替换和排除的版本，命令行会自动根据go.mod文件来维护需求声明中的版本。如果想获取更多的有关go.mod文件的介绍，可以使用命令go help go.mod。

    go.mod文件用//注释，而不用/**/。文件的每行都有一条指令，由一个动作加上参数组成。例如：

    ```
    module my/thing
    require other/thing     v1.0.2
    require new/thing 		v2.3.4
    exclude old/thing 		v1.2.3
    replace bad/thing 		v1.4.5 	=> good/thing v1.4.5
    ```

- 命令

    go mod help

    ```go
    download                //下载模块到本地缓存，具体可以通过命令go env查看，其中环境变量GOCACHE就是缓存的地址，如果该文件夹的内容太大，可以通过命令go clean -cache
    edit                    //从工具或脚本中编辑go.mod文件
    graph                   //打印模块需求图
    init                    //在当前目录下初始化新的模块
    tidy                    //添加缺失的模块以及移除无用的模块
    verify                  //验证依赖项是否达到预期的目的
    why                     //解释为什么需要包或模块
    ```

- go.sum

    运行`go mod init {projectName}` 项目 ，然后 `go run / build main.go`

    发现项目目录下多出了一个文件 `go.sum`  

    `go.sum` 是记录所依赖的项目的版本的锁定。