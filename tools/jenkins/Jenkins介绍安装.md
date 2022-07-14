# jenkins 的介绍说明

- [返回](./README.md)

- [Jenkins 百度百科](https://baike.baidu.com/item/Jenkins/10917210)

- [Jenkins-官网](https://jenkins.io/)

- [github 地址](https://github.com/jenkinsci/jenkins)

## 安装部署

- 下载 war 包 (官网下载缓慢,可以找国内的镜像源地址,如清华大学的)

- 下载 tomcat 安装 tomcat

  [tomcat 安装](https://github.com/zhangymPerson/learning-notes/blob/v1.0/Tools/Tomcat/Tomcat%E4%BB%8B%E7%BB%8D%E5%AE%89%E8%A3%85.md)

- 将 war 包放入 tomcat 中 webapps 下

  `mv \*\*.tar.gz $TOMCAT_HOME/webapps/`

- 启动 tomcat

  `$TOMCAT_HOME/bin startup.sh`

- 访问 jenkins

  `http://host:port/jenkins`

  按照提示进行初始化配置

- 国内访问镜像慢的问题

  修改 `$user/.jenkins/updates/default.json`

  修改 `https://updates.jenkins.io/download` 搜索 update 查看 url,每个版本的配置可能不同 为国内镜像 如 `https://mirrors.tuna.tsinghua.edu.cn/jenkins/`

  在 页面操作 `Jenkins->Manage Jenkins->Manage Plugins`，点击 Available

  在 Manage Plugins 点击 Advanced，把 Update Site 改为国内插件下载地址 `https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json`

### 插件

- 搜索 chinese 可以安装汉化插件
