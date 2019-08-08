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

    [idea激活文章和教程](https://blog.csdn.net/shengshengshiwo/article/details/79599761)

- idea 修改文件字体

    file - setting - Editor - Font - 修改相关参数

- idea 全文查找字符

    菜单栏 edit -> find -> find in path  

- idea 标签栏多行设置

    setting - Editor - General - Editor tabs 
        
        反向勾选掉show tabs in single row
       
- idea 显示方法说明

    ctrl+q


- idea 修改默认的shell 为powershell 不用windows的cmd

    打开setting 然后找到Tools - Terminal - Shell path  

    cmd.exe 改成 powershell.exe
       
- idea显示类注解/方法注解

    搜索栏中输入Show quick documentation on mouse move 就搜索出来了

    或是在setting -> Editor -> General -> Other中都可以看到

- idea 显示占用内存  开启后显示位置在软件的右下角

    File-->Settings-->Apperance-->Window Options-->Show Memory indicator

- Ctrl+鼠标滚轴修改字体大小

    IDEA也支持向浏览器那样按住Ctrl+鼠标滚轴来改变编辑区的字体的大小，设置的开关在：File-->Settings-->Editor-->General

    Change font size (Zoom) with Ctrl + Mouse Wheel

- git/svn 提交人显示

    在行号位置  点击右键 - 选择 annotate

- 查看文件的本地历史记录

    鼠标选中文件，然后右键，在弹出的列表中选择Local History然后就可以看到文件的本地修改记录，即使没有版本控制工具也可以看到这些记录。

- idea 配置默认maven

    IDEA不像Eclipse那样可以在一个窗口中打开多个项目;
    
    IDEA每次打开一个新的项目都需要开一个新的窗口或者覆盖掉当前窗口，所以在打开多个项目的时候就需要开多个窗口，但是如果不设置好默认设置，每次打开一个新的窗口就要重新设置。例如：每次打开新的项目的时候maven的本地仓库地址都要重新设置。
    
    通过设置Other Settings就可以解决这类问题。File-->Other Settings-->Preferences for New Projects。然后在左上角的搜索框中搜maven，就能看到如下图所示配置了。