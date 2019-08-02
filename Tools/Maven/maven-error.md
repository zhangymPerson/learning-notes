# 错误记录

- 跳过test编译

    **windows下必须加引号**
     mvn clean package -D'maven.test.skip=true'


- maven 项目多模块打包时报错，找不到子模块问题

    log: Failed to execute goal on project/Could not resolve dependencies for project

    解决方法：

        maven 工程，父子类关系，子类关系互相引用时，必须先父类工程install一下，才能编译子类模块
        
        需要把parent工程，也就是package是pom的那个工程先install一下；之后再install公共引入的模块，最后就可以单独编译子模块。

        不用install，直接编译parent项目；这种方式只能在parent项目下进行，不能单独编译子模块。