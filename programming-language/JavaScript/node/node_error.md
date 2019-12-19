# 错误和异常

- Error: EACCES: permission denied, mkdir

官网解释：

If npm was invoked with root privileges, then it will change the uid to the user account or uid specified by the user config, which defaults to nobody. Set the unsafe-perm flag to run scripts with root privileges.

- 先清理

    npm cache clear --force


- 处理方案：在命令结尾加 

    --unsafe-perm： npm install --unsafe-perm

> 在package.json中添加：    
```json
"config": {

    "unsafe-perm":true
}
```

- unresolved function or method require() 问题

    在使用WebStorm工具搭建Node.js文件时，提示unresolved function or method require()的错误，并且提示配置Node.js 对应版本的Core modules，解决办法为：

    在WebStorm中的File菜单项中选择

    Setting -> Languages&Frameworks -> Javascript -> libraries -> Add添加Node.js v*** Core Modules项，

    配置 webstrom支持node.js语法检测及语法提示！   支持nodejs等语法提示和补全
    Setting -> Languages/Framework -> Node.js and NPM -> Coding assistance for Node.js