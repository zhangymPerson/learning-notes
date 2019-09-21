### java 中的日志系统

- slf4j

    slf4j提供了门面日志系统的接口

    其实slf4j原理很简单，他只提供一个核心slf4j api(就是slf4j-api.jar包)，这个包只有日志的接口，并没有实现，所以如果要使用就得再给它提供一个实现了些接口的日志包，比 如：log4j,common logging,jdk log日志实现包等，但是这些日志实现又不能通过接口直接调用，实现上他们根本就和slf4j-api不一致，因此slf4j又增加了一层来转换各日志实现包的使 用，当然slf4j-simple除外。其结构如下： 

    slf4j-api(接口层,封装日志相关方法规范，但没有实现) > 各日志实现包的连接层( slf4j-jdk14, slf4j-log4j 主要是将各种日志的实现转换成slf4j的接口规范，便于使用) > 各日志具体实现的jar包，如log4j.xx.jar等 

    **在这里还需要注意的是，连接层的jar包和实现的jar的版本要一致。**

    附jar说明：
    slf4j-api-1.6.1.jar         -->  slf4j核心接口包
    slf4j-simple-1.6.1.jar      -->  slf4j Simple Logger日志实现包
    slf4j-nop-1.6.1.jar         -->
    slf4j-migrator-1.6.1.jar    -->
    slf4j-log4j12-1.6.1.jar     -->  slf4j调用log4j的实现包
    slf4j-jdk14-1.6.1.jar       -->  slf4j调用jdk java.util.logging的实现包
    slf4j-jcl-1.6.1.jar         -->  Jakarta Commons Logging
    slf4j-ext-1.6.1.jar         -->
    log4j-over-slf4j-1.6.1.jar  -->
    jul-to-slf4j-1.6.1.jar      -->
    jcl-over-slf4j-1.6.1.jar    -->

- slf4j+log4j组合使用模式：

    slf4j-api-1.5.11.jar 

    slf4j-log4j12-1.5.11.jar 

    log4j-1.2.15.jar 

    log4j.properties(也可以是 log4j.xml，本例中用 log4j.propertes) 

- JCL+Log4J组合使用模式：

    commons-logging-1.1.jar

    log4j-1.2.15.jar

    log4j.properties