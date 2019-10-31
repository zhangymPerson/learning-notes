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


