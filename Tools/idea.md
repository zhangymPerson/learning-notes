# idea使用

- idea添加插件

    file - settings - Plugins

- [修改Intellij IDEA模板注解@author变量user内容](https://jingyan.baidu.com/article/0202781138ab5e1bcc9ce531.html)

    打开setting 查找 File | Settings | Editor | File and Code Templates 位置下， 修改响应的参数即可
    模板如下
    ```sh
    /**
    * @classname ${NAME}
    * @descriptionclass 
    * 1.类的作用
    * 2.其他说明
    * @createdate ${DATE} ${TIME}
    * @author <a href="mailto:you-email@163.com">${USER}</a>
    * @version 1.0
    * @since 1.0
    */
    ```


- idea maven 项目读取不到配置文件 application.properties

    ```java
    //todo 未解决
    BUG:
    No active profile set, falling back to default profiles: default
    ```
   
- compiler

    Java Compiler 下的版本选择和当前的jdk版本一致


- idea下载maven源码 

- idea查看maven的依赖关系

    ![idea查看maven结构和源码](https://github.com/zhangymPerson/springboot-learing/blob/master/picture/idea%E7%9A%84%E4%BD%BF%E7%94%A8%E6%96%B9%E5%BC%8F.jpg)

- idea查看单个类的方式

    ![idea查看单个类的继承关系](https://github.com/zhangymPerson/springboot-learing/blob/master/picture/idea%E6%9F%A5%E7%9C%8B%E7%B1%BB%E7%9A%84%E7%BB%93%E6%9E%84%E5%85%B3%E7%B3%BB.jpg)

- idea 激活

    ![idea激活文章和教程](https://blog.csdn.net/shengshengshiwo/article/details/79599761)