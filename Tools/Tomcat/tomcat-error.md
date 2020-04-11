## tomcat 问题记录

### 启动慢

- 在Tomcat环境中解决

    可以通过配置JRE使用非阻塞的Entropy Source。

    在catalina.sh中加入这么一行：-Djava.security.egd=file:/dev/./urandom 即可。


- 在JVM环境中解决

    打开$JAVA_PATH/jre/lib/security/java.security这个文件，找到下面的内容：

    `securerandom.source=file:/dev/urandom`

    替换成

    `securerandom.source=file:/dev/./urandom`

- tomcat 启动windows启动脚本一闪而过

     在 .bat 脚本文件后面添加该命令
     则脚本运行完后不直接退出
     `PAUSE`