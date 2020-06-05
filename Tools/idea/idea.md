# idea使用

- idea添加插件

    file - settings - Plugins

- [修改Intellij IDEA模板注解@author变量user内容](https://jingyan.baidu.com/article/0202781138ab5e1bcc9ce531.html)

    打开setting 查找 File | Settings | Editor | File and Code Templates 位置下， 修改响应的参数即可
    模板如下
    ```sh
    /**
    * @class name ${NAME}
    * @description class 
    * 1.类的作用
    * 2.其他说明
    * @create date ${DATE} ${TIME}
    * @author <a href="mailto:you-email@163.com">${USER}</a>
    * @version 1.0
    * @since 1.0
    */
    ```

    ```
    /**
    * date ${DATE} ${TIME} <br/>
    * description class <br/>
    *
    * @author ${USER} 
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

    File-->Settings-->Appearance-->Window Options-->Show Memory indicator

    idea2020.1版本设置方式
    菜单栏 view -> Appearance -> status bar widgets -> memory indicator

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

- idea无法从控制台输入的问题 
    
    例如:
    ```java
    @Test
    public void testScanner() {
        Scanner scanner = new Scanner(System.in);
        String arg = "";
        System.out.println("请输入：");
        if (scanner.hasNext()) {
            /**
                * 使用netLine 读到下一行为止 如果使用next 则读到 空格为止
                */
            arg = scanner.nextLine();
        }
        System.out.println("输入值为:" + arg);
    }
    ```

    解决办法： 在 启动 idea.exe位置 找到idea.exe.vmoptions和idea64.exe.vmoptions这两个文件

    添加 
    ```conf
    -Deditable.java.test.console=true
    ```

- idea的修改内存的方法

    首先，我们需要找到 idea.vmoptions 文件的位置，这个不同的平台，估计名称可能有些差别

    ```
    -Xms128m
    -Xmx384m
    -XX:ReservedCodeCacheSize=240m
    -XX:+UseConcMarkSweepGC
    -XX:SoftRefLRUPolicyMSPerMB=50
    -ea
    -Dsun.io.useCanonCaches=false
    -Djava.net.preferIPv4Stack=true
    -Djdk.http.auth.tunneling.disabledSchemes=""
    -XX:+HeapDumpOnOutOfMemoryError
    -XX:-OmitStackTraceInFastThrow
    -javaagent:C:\Program Files\JetBrains\IntelliJ IDEA 2018.2.5\bin\JetbrainsCrack-3.1-release-enc.jar
    -Deditable.java.test.console=true
    ```
    - Xms128m,最小内存
    - Xmx750m,最大内存
    - 预留代码缓存的大小
    - UseConcMarkSweepGC,设置年老代为并发收集

    在idea上直接修改的方式：

    help->Edite Custom Vm Options
    打开配置文件修改相应的参数

    ```
    -Xms1024m
    -Xmx2048m
    -XX:ReservedCodeCacheSize=1024m
    ```
    修改完重启idea,即可完成相应的修改;
   
- idea 查看静态html页面的端口 


    默认是：63342

    修改配置方式：

    File ->setting ->  Debugger -> port 

    默认访问路径

        ```py
        #访问路径为项目名 + 静态文件所在的项目下全路径名
        http:localhost:63342/${project_name}/***/**.html
        ```

- Intellij IDEA中默认所有 scope 为 provided 的依赖不会被加入到 classpath

    报错：Caused by: java.lang.ClassNotFoundException: javax.servlet.ServletContext

    解决办法：
    
    菜单栏 -> Run -> Edit Configurations

    Run/Debug Configurations -> Application -> Configuration -> 勾选：include dependencies with "Provided" scope 

- idea 配置项目启动一次 实例化一次， 多次 run 为 restart

    找到项目配置位置 Run/Debug Configurations  勾选     Single instance only 实例化一次

- idea 修改jdk版本时，需要修改的几个位置

    - 菜单栏中 file - Project structure - project -  project sdk 修改为 指定jdk安装目录
    - 菜单栏中 file - Project structure - project -  project language level 修改为 指定的jdk版本
    - 菜单栏中 file - Project structure - modules -  language level 修改为 指定的jdk版本
    - 菜单栏中 file - settings - build,execution,deployment - compiler - Java Compiler - project bytecode version 修改为指定版本 

- idea-vim中的 ctrl+c /ctrl+v 处理

    idea中启用vim插件之后，ctrl+c/ctrl+v失效

    解决办法

    file -> settings -> editor -> vim -> vim emulation

    配置ctrl+c/ctrl+v handler 由vim改为IDE

- idea中文乱码的解决办法

    设置文件格式

    settings -> Eidtor -> File Encodings 里面设置字体编码格式， 全部位置 都设置 UTF-8

    配置idea启动项配置 

    在安装目录 `~\JetBrains\IdeaIC***` 下 
    
    或者在编辑器内直接打开 
    
    方式 菜单栏 help -> `Edit Custom VM Options` 和 `Edit Custom Properties` 
    
    在 `idea64.exe.vmoptions` 和 `idea.properties`(文件不存在则手动创建) 配置文件中添加如下配置

    `-Dfile.encoding=UTF-8` (主要解决控制台输出乱码的问题)

- idea 断点调试 - 跳过断点问题 

    **提示信息 `Skipped breakpoint *** because it happened inside debugger evaluation`**

    解决办法

    打开 `idea` 配置 `Settings`
    
    去掉 这行 `Enable 'toString()' object view`

    不行 就去掉 `Enable alternative view for Collections classes`

    `idea` 默认在用户调试之前先执行 `toString` 方法，然后回显数据，也就是“预知”功能。但有时候会影响判断，但可以设置那些类中 `toString` 方法是是可以做“预知”。