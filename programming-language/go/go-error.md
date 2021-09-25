# go error note

- 模块路径问题

  执行 `go get -u -v github.com/Luxurioust/excelize` 命令报错如下

  ```sh
  module declares its path as: github.com/360EntSecGroup-Skylar/excelize
  but was required as: github.com/Luxurioust/excelize
  ```

- 解决办法

  在你当前的项目下的`go.mod`文件中加入

  `replace github.com/Luxurioust/excelize => github.com/360EntSecGroup-Skylar/excelize v1.4.1 // indirect`

- 说明

  **不是所有的包都能直接用 go get 获取到，这时我们就需要使用 go modules 的 replace 功能了。**

  使用 replace 替换 package
  replace 顾名思义，就是用新的 package 去替换另一个 package，他们可以是不同的 package，也可以是同一个 package 的不同版本。看一下基本的语法：

  `go mod edit -replace=old[@v]=new[@v]`

  **old 是要被替换的 package，new 就是用于替换的 package。**

- 使用了 go mod 后，产生冲突导致无法提示 vscode go 代码智能提示问题

  经过多种资料和测试无效后，我看到了这么一句话：The "inferGopath" setting is disabled for this workspace because Go modules are being used.

  原因：要使用 go mod,便于下载各种依赖包，就会添加两个环境变量 GOPROXY 和 GO111MODULE，这两个是为了下载到不能下的包，但是使用了他之后，就默认禁用了 inferGopath 这个属性（为什么我还不知道），这个属性开启才能启动智能提示，这里冲突了。

  设置命令 `go env -w GO111MODULE=on`

- 解决办法：将 GO111MODULE 环境变量改为 off 即可,代码的智能提示就有了。每次需要下载依赖包时，再把这个环境变量改为 on，记得下完改回来，或者使用 auto 试试
