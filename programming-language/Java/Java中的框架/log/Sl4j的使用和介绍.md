### java 中的日志系统

- slf4j

    [官网说明](https://www.slf4j.org/manual.html)

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

    log4j.properties

- 完整的maven添加slf4j的pom.xml配置

    使用slf4j,注解@Slf4j 加log.info();使用
    ```java
    package cn.danao;
    import lombok.extern.slf4j.Slf4j;
    /**
    * @author danao
    * @version 1.0
    * @classname Application
    * @descriptionclass 1.使用Slf4j的方式
    * @createdate 2019/9/25 16:22
    * @since 1.0
    */
    @Slf4j
    public class Application {

        public static void main(String[] args) {
            log.info("test");
        }

    }
    ```

    slf4j + slf4j-simple
    
    测试可用 使用需注意jar包之间的版本兼容
    ```xml

    <dependencies>
        <!--支持@Slf4j注解-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.2</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>1.7.26</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/org.slf4j/slf4j-simple -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-simple</artifactId>
            <version>1.7.26</version>
        </dependency>
    </dependencies>

    ```

    slf4j + log4j
    ```xml
    <dependencies>
        <!--支持@Slf4j注解-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.2</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>1.7.26</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
            <version>1.7.10</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/log4j/log4j -->
        <dependency>
            <groupId>log4j</groupId>
            <artifactId>log4j</artifactId>
            <version>1.2.17</version>
        </dependency>
    </dependencies>
    ```
    log4j.properties
    ```properties
    #日志配置
    log4j.rootLogger=info,consoles
    ##自定义日志输出样式
    #%p 输出优先级，即DEBUG，INFO，WARN，ERROR，FATAL
    #%r 输出自应用启动到输出该log信息耗费的毫秒数
    #%c 输出所属的类目，通常就是所在类的全名
    #%t 输出产生该日志事件的线程名
    #%n 输出一个回车换行符，Windows平台为“rn”，Unix平台为“n”
    #%d 输出日志时间点的日期或时间，默认格式为ISO8601，也可以在其后指定格式，比如：%d{yyy MMM dd HH:mm:ss,SSS}，输出类似：2002年10月18日 22：10：28，921
    #%l 输出日志事件的发生位置，包括类目名、发生的线程，以及在代码中的行数。举例：Testlog4.main(TestLog4.java:10)
    #%m 输出代码中指定的讯息，如log(message)中的message
    log4j.appender.CONSOLE.Encoding=UTF-8
    ##输出到控制台日志配置
    log4j.appender.consoles=org.apache.log4j.ConsoleAppender
    ##设置输出样式
    log4j.appender.consoles.layout=org.apache.log4j.PatternLayout
    ##日志打印样式
    log4j.appender.consoles.layout.ConversionPattern= [%p] [%-d{yyyy-MM-dd HH:mm:ss}] (%l):%m%n
    ```


- JCL+Log4J组合使用模式：

    commons-logging-1.1.jar

    log4j-1.2.15.jar

    log4j.properties