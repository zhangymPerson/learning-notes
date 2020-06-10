# go error note

- 模块路径问题

  执行 `go get -u -v github.com/Luxurioust/excelize` 命令报错如下

  ```
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
