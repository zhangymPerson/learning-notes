# 安装 gradle

- 前提

  环境中需要提前安装好 java 环境

        java -version

- 官网下载

  windows 下安装 zip 文件包

  解压到指定位置

  配置环境变量

  GRADLE_HOME=安装目录

  PATH 下添加 GRADLE_HOME/bin

  测试命令

        gradle -v

  查看安装是否成功，安装的版本号

- 修改本地仓库地址

  设置本地仓库目录

  GRADLE_USER_HOME=

- **重点注意**

  > GRADLE_HOME=安装目录 GRADLE_USER_HOME=本地仓库目录 的区别 GRADLE_HOME/bin 下指定的是可以执行的 gradle 的目录 ，而 GRADLE_USER_HOME 是 gradle 的各种缓存文件和仓库文件的位置 还有 其他版本的 gradle 的下载包存放位置

- GRADLE_USER_HOME 目录说明

  | 目录    | 描述                    |
  | ------- | ----------------------- |
  | caches  | gradle 缓存目录         |
  | daemon  | daemon 日志目录         |
  | native  | gradle 平台相关目录     |
  | wrapper | gradle-wrapper 下载目录 |

  > wrapper 中存放每一个项目自定义配置的 \$project_path/gradle/wrapper/gradle-wrapper.properties 文件中的 distributionUrl=https\://services.gradle.org/distributions/gradle-\*.\*.\*-all.zip 其中\*.\*.\*代表 gradle 的版本

  > caches/modules-2/files-2.1 存放着 gradle 项目中从 maven 仓库下载到本地 jar 包

- 修改 gradle 使用本地 maven 仓库

  需要在 gradle 的配置中添加 在项目最外层的 build.gradle 中修改添加

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

  > mavenLocal()仓库的默认路径是：/home/user/.m2/repository(这是 Linux 系统下的，windows 系统类似。

  > mavenLocal()配置 maven 的本地仓库后，gradle 默认会按以下顺序去查找本地的仓库：USER_HOME/.m2/settings.xml >> M2_HOME/conf/settings.xml >> USER_HOME/.m2/repository。

  > 我的本地仓库放置在 D:\maven_repository，而且在 USER_HOME/.m2/目录下并没有放置配置文件，只有在 maven 的安装目录下有 conf/settings.xml 文件。所以才出现设置不管用的情况。

- 修改 Gradle 版本

  在项目的 gradle 目录下

  wrapper 目录下

  gradle-wrapper.properties 配置文件中

  修改 distributionUrl 参数路径 指定使用的 gradle

  ```properties
  distributionUrl=https\://services.gradle.org/distributions/gradle-5.4.1-all.zip
  ```

  gradle 配置使用本地的 zip 包

  提前下载好 zip 包文件 然后指向即可

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

  在\${USER_HOME}/.gradle/下创建 init.gradle 文件

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

- gradle 项目配置本地的 jar 包

  在 build.gradle 目录下创建 libs 文件夹 (可以自定义名称)

  在配置文件中引入该文件夹

  ```gradle
  dependencies {
      implementation fileTree(dir: "libs", include: ["*.jar"])
  }
  ```
