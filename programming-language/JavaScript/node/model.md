# nodejs中的模块概念

## 模块

> 模块成员大致分三类 核心模块 第三方模块 用户自定义模块

- 核心模块：
    
    随着Node.js的安装包，一同安装到本地的模块，叫做核心模块；

    例如：fs，path等模块，都是由Node.js官方提供的核心模块；

    只要大家在计算机中，安装了Node这个应用程序，那么，我们的计算机中就已经安装了所有的 核心模块；

    调用核心模块：require('核心模块标识符'）

- 第三方模块：

    非官方提供的模块，叫做第三方模块；

    第三方模块，需要网络搜索和下载才能使用；

    管理工具 npm [网址](https://www.npmjs.com/)

    使用 require('第三方模块的名称标识符')来导入这个模块

    具体使用 依据 官方文档相关说明
- 自定义开发模块：

    自己项目中写的 Javascript 文件，和创建的项目；

    使用自定义模块：require('路径标识符')

## nodejs创建自定义模块 (类似Java中的jar包概念)

- 创建项目目录

    `mkdir mypackage`

- 创建配置文件 package.json 文件

    `cd mypackage`
    `npm init` 输入相应的内容

    自动生成 package.json文件

- package.json文件说明

    name：项目/模块名称，长度必须小于等于214个字符，不能以"."(点)或者"_"(下划线)开头，不能包含大写字母。

    version：项目版本。

    author：项目开发者，它的值是你在https://npmjs.org网站的有效账户名，遵循“账户名<邮件>”的规则，例如：zhangsan zhangsan@163.com。

    description：项目描述，是一个字符串。它可以帮助人们在使用npm search时找到这个包。

    keywords：项目关键字，是一个字符串数组。它可以帮助人们在使用npm search时找到这个包。

    private：是否私有，设置为 true 时，npm 拒绝发布。

    license：软件授权条款，让用户知道他们的使用权利和限制。

    bugs：bug 提交地址。

    contributors：项目贡献者 。

    repository：项目仓库地址。

    homepage：项目包的官网 URL。

    dependencies：生产环境下，项目运行所需依赖。

    devDependencies：开发环境下，项目所需依赖。

    scripts：执行 npm 脚本命令简写，比如 “start”: “react-scripts start”, 执行 npm start 就是运行 “react-scripts start”。

    bin：内部命令对应的可执行文件的路径。

    main：项目默认执行文件，比如 require(‘webpack’)；就会默认加载 lib 目录下的 webpack.js 文件，如果没有设置，则默认加载项目跟目录下的 index.js 文件。

    module：是以 ES Module(也就是 ES6)模块化方式进行加载，因为早期没有 ES6 模块化方案时，都是遵循 CommonJS 规范，而 CommonJS 规范的包是以 main 的方式表示入口文件的，为了区分就新增了 module 方式，但是 ES6 模块化方案效率更高，所以会优先查看是否有 module 字段，没有才使用 main 字段。

    eslintConfig：EsLint 检查文件配置，自动读取验证。

    engines：项目运行的平台。

    browserslist：供浏览器使用的版本列表。

    style：供浏览器使用时，样式文件所在的位置；样式文件打包工具parcelify，通过它知道样式文件的打包位置。

    files：被项目包含的文件名数组。

- 项目目录

    bin目录 可执行的内容;

    lib目录 源码;

    doc目录 文档;

    test目录 测试;

- 每个js文件中添加

    ```js
    //将本js文件对外提供
    module.exports = filename;
    ```

    创建main.js
    ```js
    const filenameA = require("./filenameA")
    const filenameB = require("./filenameB")
    const filenameC = require("./filenameC")

    module.exports = {
        filenameA,
        filenameB,
        filenameC
    }
    ```
## 加载模块规则
> JS中，一个模块加载另一个模块有两套规范：CommonJS规范和AMD规范。

## CommonJS规范

    加载模块是同步的，也就是说，只有加载完成，才能执行后面的操作。
    
## AMD规范则

    是非同步加载模块，允许指定回调函数。
    
### 规范选择

- 由于Node.js主要用于服务器编程，模块文件一般都已经存在于本地硬盘，所以加载起来比较快，不用考虑非同步加载的方式，所以CommonJS规范比较适用。

- 如果是浏览器环境，要从服务器端加载模块，这时就必须采用非同步模式，因此浏览器端一般采用AMD规范。
