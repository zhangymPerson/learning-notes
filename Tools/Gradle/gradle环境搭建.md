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