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


    tomcat用户权限说明

    以下是Tomcat Manager 4种角色的大致介绍(下面URL中的*为通配符)：

    - manager-gui
    
        允许访问html接口(即URL路径为/manager/html/*)
    - manager-script
    
        允许访问纯文本接口(即URL路径为/manager/text/*)
    - manager-jmx
    
        允许访问JMX代理接口(即URL路径为/manager/jmxproxy/*)
    - manager-status
    
        允许访问Tomcat只读状态页面(即URL路径为/manager/status/*)

    权限配置(允许远程机器访问管理页面)

    ~/tomcat目录下     
    
        ~/webapps/manager/META-INF 修改context.xml 文件  
    
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

    <!-- 打不开 server staus -->
    <!--这个对应的是 页面 Host Manager 按钮的权限-->
    <role rolename="admin-gui"/>
    <user username="tomcat" password="tomcat" roles="admin-gui"/>
    <!-- 最大权限 -->
    <user username="root" fullname="tomcat" password="tomcat"  roles="manager-gui,manager-script,manager-jmx,manager-status,admin-gui,admin-script"/>
    ```
    tomcat管理页面一次只能登陆一个用户，要进入其他用户，需重新请求页面

    **注意：tomcat管理权限的用户登陆以后，除非用户名密码一致，否则需要重新请求页面（关闭浏览器，重启浏览器且不保存密码才行）**



- tomcat-users.xsd


- web.xml
