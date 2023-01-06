# GO 的包管理

> Go Module 是 Go 会在 1.12 中正式推出的包管理机制。
> go mod 的作用 类似于 Java 中的 mvn 和 nodejs 中 npm 主要做项目中的包管理

- go mod

  不同于以往基于 GOPATH 和 Vendor 的构建方式，其主要是通过 GOPATH/pkg/mod 下的缓存包来对工程进行构建。

  **我们也推荐你在使用 Go 模块时将 GO111MODULE 设置为 on 而不是 auto。(注意：国内一些包需要代理才能下载使用，所以才设置此项)**

  设置命令 `go env -w GO111MODULE=on`

  在 Go 1.11 中已经可以使用，同以往新添加的功能一样，

  go mod 可以通过 GO111MODULE 来控制是否启用，GO111MODULE 有一下三种类型。

  - on 所有的构建，都使用 Module 机制

  - off 所有的构建，都不使用 Module 机制，而是使用 GOPATH 和 Vendor

  - auto 在 GOPATH 下的工程，不使用 Module 机制，不在 GOPATH 下的工程使用

- go mod 是打包自己的项目

- go mod 命令

  **缓存包所在的目录位置是 \${GOPATH}/pkg/mod 下的缓存包**

- 使用方式

  **使用命令必须跟自己的项目名称 否则报错**

  ```shell
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

  在我看来，replace 对于国内开发来说是个神功能，他可以将代码中使用，但国内被墙的代码替换成 github 上的下载路径，例如：golang.org/x/ 下的包，全都替换成 github 地址上的包，版本使用 latest 即可

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

  go.mod 文件还可以指定要替换和排除的版本，命令行会自动根据 go.mod 文件来维护需求声明中的版本。如果想获取更多的有关 go.mod 文件的介绍，可以使用命令 go help go.mod。

  go.mod 文件用//注释，而不用/\*\*/。文件的每行都有一条指令，由一个动作加上参数组成。例如：

  ```conf
  module my/thing
  require other/thing     v1.0.2
  require new/thing    v2.3.4
  exclude old/thing    v1.2.3
  replace bad/thing    v1.4.5 => good/thing v1.4.5
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

- go 中的**包特点**

  多个源文件可同属于一个包(同一文件夹内)，要求 `package packagename` 指定的包名必须一样；

  一个包对应生成一个\*.a 文件，生成的文件名并不是包名+.a 组成，是目录名+.a 组成 `go build -x -v main`

  go install ××× 这里对应的并不是包名，而是路径名！！

  import ××× 这里使用的也不是包名，也是路径名

  ×××××.FunctionName() 调用使用的是包名！

  指定 ××× 路径名就代表了此目录下唯一的包，编译器连接器默认就会去生成或者使用它，而不需要我们手动指明！

  **一个目录下就只能有一个包存在(可以与目录名不一致)**

  对于调用有源码的第三方包，连接器在连接时，其实使用的并不是我们工作目录下的.a 文件，而是以该最新源码编译出的临时文件夹中的.a 文件

  对于调用没有源码的第三方包，上面的临时编译不可能成功，那么临时目录下就不可能有.a 文件，所以最后链接时就只能链接到工作目录下的.a 文件

  对于标准库，即便是修改了源代码，只要不重新编译 Go 源码，那么链接时使用的就还是已经编译好的\*.a 文件

- 包导入有三种模式：正常模式、别名模式、简便模式

  ```go
  //官方包导入 GOROOT 路径下  Go语言的标准库，他其实是去GOROOT下去加载该模块
  import(
      "fmt"
  )

  //相对路径
  //当前文件同一目录的model目录，但是不建议这种方式import
  import   "./model"

  //绝对路径
  //加载GOPATH/src/shorturl/model模块
  import   "shorturl/model"
  ```

  - 别名模式

  ```go
  import( f "fmt" )
  //别名操作调用包函数时前缀变成了重命名的前缀，
  //即f.Println(“hello world”)
  ```

  点操作 / \_操作 等操作

- go 显示所有 import 库信息 命令

  `go list -m -json all`

  - -json JSON 格式显示

  - all 显示全部库

### go 包名和目录名不一致时的用法

- **当 `包名` 和 `目录名` 不一致时，go 是使用 `目录名` 导入，代码调用时，需要使用 `包名` 进行调用**

- 举例如下

  - ~/目录名
    a.go 中

    ```go
    package 包名
    // 定义变量
    Arg:="a"

    ```

  - 调用时

    ```go
    import "~/目录名"
    // 引用变量
    a := 包名.Args
    ```

### go 包管理 不同版本的包导入

- 版本升级的引入方式
  在 Go module 时代，module 版本号要遵循语义化版本规范，即版本号格式为 v<major>.<minor>.<patch>，如 v1.2.3。当有不兼容的改变时，需要增加 major 版本号，如 v2.1.0。

  Go module 规定，如果 major 版本号大于 1，则 major 版本号需要显式地标记在 module 名字中，如 module github.com/my/mod/v2。这样做的好处是 Go module 会把 module github.com/my/mod/v2 和 module github.com/my/mod 视做两个 module，他们甚至可以被同时引用。

- 升级包的 major

  对包的作者而言，升级 major 版本号需要：

  升级 module 的根路径，增加 vN

  建立 vN.x.x 形式的 tag（可选，如果不打 tag，go 会在 consumer 的 go.mod 中使用伪版本号，比如：bitbucket.org/bigwhite/modules-major-branch/v2 v2.0.0-20190603050009-28a5b8da279e）

  如果 modules-major-branch 内部有相互的包引用，那么在升级 major 号的时候，这些包的 import 路径也要增加 vN，否则就会存在在高 major version 的代码中引用低 major version 包代码的情况，这也是包作者最容易忽略的事情。github.com/marwan-at-work/mod 是一个为 module 作者提供的升级/降级 major version 号的工具，它可以帮助包作者方便地自动修改项目内所有源文件中的 import path。有 gopher 已经提出希望 go 官方提供 upgrade/downgrade 的支持，但目前 core team 尚未明确是否增加。

  对于 consumer 而言，升级依赖包的 major 版本号，只需要在 import 包时在 import path 中增加 vN 即可，当然代码中也要针对不兼容的部分进行修改，然后 go 工具会自动下载相关包。

- go 目录规范

  go 官方目录建议

  https://github.com/golang-standards/project-layout
