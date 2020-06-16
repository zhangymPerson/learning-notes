# 错误和异常

- Error: EACCES: permission denied, mkdir

- 官网解释：

  ```
  If npm was invoked with root privileges, then it will change the uid to the user account or uid specified by the user config, which defaults to nobody. Set the unsafe-perm flag to run scripts with root privileges.
  ```

- npm 清理缓存的命令

  `npm cache clear --force`

* 处理方案：在命令结尾加

  --unsafe-perm： npm install --unsafe-perm

- 在 package.json 中添加：

  ```json
  "config": {
      "unsafe-perm":true
  }
  ```

- unresolved function or method require() 问题

  在使用 WebStorm 工具搭建 Node.js 文件时，提示 unresolved function or method require()的错误，并且提示配置 Node.js 对应版本的 Core modules，解决办法为：

  在 WebStorm 中的 File 菜单项中选择

  Setting -> Languages&Frameworks -> Javascript -> libraries -> Add 添加 Node.js v\*\*\* Core Modules 项，

  配置 webstrom 支持 node.js 语法检测及语法提示！ 支持 nodejs 等语法提示和补全
  Setting -> Languages/Framework -> Node.js and NPM -> Coding assistance for Node.js

- npm 报错 4084

  ```
  npm ERR! errno -4048，Error: EPERM: operation not permitted,syscall unlink
  ```

- 解决 需要切换到管理员下执行 linux 需要 sudo windows 使用管理员权限打开 cmd

  尝试使用 cnpm（基本可以解决）

  `npm install -g cnpm --registry=https://registry.npm.taobao.org`

  或者清除缓存

  `npm cache clean --force`

  然后再执行

  `npm install --registry=https://registry.npm.taobao.org -g`

- npm 报错

  ```
  npm WARN tar ENOENT: no such file or directory,
  ```

- 解决办法

  删除 package-lock.josn

  `npm install`
