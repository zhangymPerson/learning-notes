# 安装gradle

- 前提

    环境中需要提前安装好java环境

        java -version

- 官网下载

    windows 下安装 zip文件包

    解压到指定位置

    配置环境变量

    GRADLE_HOME=安装目录

    PATH下添加 GRADLE_HOME/bin

    测试命令

        gradle -v

    查看安装是否成功，安装的版本号

- 修改本地仓库地址

    设置本地仓库目录

    GRADLE_USER_HOME=

- **重点注意**

    > GRADLE_HOME=安装目录 GRADLE_USER_HOME=本地仓库目录 的区别  GRADLE_HOME/bin 下指定的是可以执行的gradle的目录 ，而 GRADLE_USER_HOME 是 gradle的各种缓存文件和仓库文件的位置 还有 其他版本的 gradle 的下载包存放位置


- GRADLE_USER_HOME目录说明

    |目录	|描述
    |-|-
    |caches	|gradle缓存目录
    |daemon	|daemon日志目录
    |native	|gradle平台相关目录
    |wrapper|gradle-wrapper下载目录

    > wrapper 中存放每一个项目自定义配置的 $project_path/gradle/wrapper/gradle-wrapper.properties文件中的 distributionUrl=https\://services.gradle.org/distributions/gradle-\*.\*.\*-all.zip 其中\*.\*.\*代表gradle的版本

    > caches/modules-2/files-2.1存放着gradle项目中从maven仓库下载到本地jar包

- 修改gradle使用本地maven仓库

    需要在gradle的配置中添加 在项目最外层的build.gradle中修改添加
    ```gradle
    buildscript {
        
        repositories {
            //此处添加 mavenLocal()则会从本地的maven仓库中拉去相关的jar
            mavenLocal()
            google()
            jcenter()
        }
        dependencies {
            classpath 'com.android.tools.build:gradle:3.1.0'
            

            // NOTE: Do not place your application dependencies here; they belong
            // in the individual module build.gradle files
        }
    }

    allprojects {
        repositories {
            //此处也需添加
            mavenLocal()
            google()
            jcenter()
        }
    }

    task clean(type: Delete) {
        delete rootProject.buildDir
    }

    ```

    > mavenLocal()仓库的默认路径是：/home/user/.m2/repository(这是Linux系统下的，windows系统类似。

    > mavenLocal()配置maven的本地仓库后，gradle默认会按以下顺序去查找本地的仓库：USER_HOME/.m2/settings.xml >> M2_HOME/conf/settings.xml >> USER_HOME/.m2/repository。
    
    > 我的本地仓库放置在D:\maven_repository，而且在USER_HOME/.m2/目录下并没有放置配置文件，只有在maven的安装目录下有conf/settings.xml文件。所以才出现设置不管用的情况。

- 修改Gradle版本 

    在项目的gradle目录下

    wrapper目录下

    gradle-wrapper.properties 配置文件中

    修改 distributionUrl 参数路径 指定使用的gradle
    ```properties
    distributionUrl=https\://services.gradle.org/distributions/gradle-5.4.1-all.zip
    ```

    gradle 配置使用本地的zip包

    提前下载好zip包文件 然后指向即可

    ```properties
    distributionUrl=file\:/D:/zidingyipath/.gradle/wrapper/dists/gradle-2.10-all/a4w5fzrkeut1ox71xslb49gst/gradle-2.10-all.zip
    ```

### gradle 阿里云环境

- 单个项目的配置

    ```gradle
    buildscript {
        repositories {
            maven { url 'http://maven.aliyun.com/nexus/content/groups/public/' }
            maven { url 'http://maven.aliyun.com/nexus/content/repositories/jcenter' }
        }
        dependencies {
            //classpath 'com.android.tools.build:gradle:2.2.3'

            // NOTE: Do not place your application dependencies here; they belong
            // in the individual module build.gradle files
        }
    }

    allprojects {
        repositories {
            maven { url 'http://maven.aliyun.com/nexus/content/groups/public/' }
            maven { url 'http://maven.aliyun.com/nexus/content/repositories/jcenter' }
        }
    }
    ```

- 全局配置

    在${USER_HOME}/.gradle/下创建init.gradle文件

    ```gradle
    allprojects {
        repositories {
            def ALIYUN_REPOSITORY_URL = 'http://maven.aliyun.com/nexus/content/groups/public'
            def ALIYUN_JCENTER_URL = 'http://maven.aliyun.com/nexus/content/repositories/jcenter'
            all { ArtifactRepository repo ->
                if (repo instanceof MavenArtifactRepository) {
                    def url = repo.url.toString()
                    if (url.startsWith('https://repo1.maven.org/maven2')) {
                        project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_REPOSITORY_URL."
                        remove repo
                    }
                    if (url.startsWith('https://jcenter.bintray.com/')) {
                        project.logger.lifecycle "Repository ${repo.url} replaced by $ALIYUN_JCENTER_URL."
                        remove repo
                    }
                }
            }
            maven {
                url ALIYUN_REPOSITORY_URL
                url ALIYUN_JCENTER_URL
            }
        }
    }
    ```