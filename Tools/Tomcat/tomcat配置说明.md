# Tomcat配置说明


## 配置文件

- catalina.policy


- catalina.properties


- context.xml


- jaspic-providers.xml


- jaspic-providers.xsd


- logging.properties


- server.xml


- tomcat-users.xml

    权限配置

    ~/tomcat目录下     /webapps/manager/META-INF 修改context.xml 文件  
    
    **不然只允许 本机访问**
   
    注释掉这个注释
  
   ```xml
     <!--<Valve className="org.apache.catalina.valves.RemoteAddrValve"
        allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />-->
    ```
    添加权限配置

    ```xml
        <role rolename="manager-gui"/>
    <user username="gui" password="tomcat" roles="standard,manager-gui"/>

    <role rolename="manager-script"/>
    <user username="script" password="tomcat" roles="standard,manager-script"/>

    <role rolename="manager-jmx"/>
    <user username="jmx" password="tomcat" roles="manager-jmx"/>

    <role rolename="manager-status"/>
    <user username="status" password="tomcat" roles="manager-status"/>

    <!--这个对应的是 Host Manager-->
    <role rolename="admin-gui"/>
    <user username="tomcat" password="tomcat" roles="admin-gui"/>

    <!--这个对应的是 Host Manager-->
    <role rolename="admin-gui"/>
    <user username="tomcat" password="tomcat" roles="admin-gui"/>
    <!--这个对应的是 Host Manager-->
    <role rolename="admin-gui"/>
    <user username="tomcat" password="tomcat" roles="admin-gui"/>
    ```
    tomcat管理页面一次只能登陆一个用户，要进入其他用户，需重新请求页面



- tomcat-users.xsd


- web.xml
