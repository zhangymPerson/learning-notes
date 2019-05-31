# jenkins的介绍说明

- [Jenkins百度百科](https://baike.baidu.com/item/Jenkins/10917210)

- [Jenkins-官网](https://jenkins.io/)

## 安装部署

- 下载 war包

- 下载tomcat 安装tomcat

    [tomcat 安装](https://github.com/zhangymPerson/learning-notes/blob/v1.0/Tools/Tomcat/Tomcat%E4%BB%8B%E7%BB%8D%E5%AE%89%E8%A3%85.md)

- 将war包放入tomcat中webapps下

    mv  **.tar.gz $TOMCAT_HOME/webapps/

- 启动tomcat

    $TOMCAT_HOME/bin  startup.sh

- 访问jenkins

    http://host:port/jenkins

    按照提示进行初始化配置