# go error note


- 模块路径问题

    执行 `go get -u -v github.com/Luxurioust/excelize` 命令报错如下

    module declares its path as: github.com/360EntSecGroup-Skylar/excelize
                but was required as: github.com/Luxurioust/excelize

- 解决办法

    在你当前的项目下的`go.mod`文件中加入  

    `replace github.com/Luxurioust/excelize => github.com/360EntSecGroup-Skylar/excelize v1.4.1 // indirect`

- 说明


    **不是所有的包都能直接用go get获取到，这时我们就需要使用go modules的replace功能了。**

    使用replace替换package
    replace顾名思义，就是用新的package去替换另一个package，他们可以是不同的package，也可以是同一个package的不同版本。看一下基本的语法：
    `go mod edit -replace=old[@v]=new[@v]`
    **old是要被替换的package，new就是用于替换的package。**