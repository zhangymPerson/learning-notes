# git 的配置文件

- [git 过滤配置文件-github 官方项目](https://github.com/github/gitignore)

  `https://github.com/github/gitignore`

- [github 的过滤文件查询网站，输入关键字直接查询](https://www.gitignore.io/)

  git 过滤文件的

  `https://www.gitignore.io/`

- 配置文件 .gitignore

  配置方式说明

  ```conf
  # 以'#'开始的行，被视为注释.

  # 忽略掉所有文件名是 foo.txt的文件.
  foo.txt
  # 忽略所有生成的 html文件,
  *.html
  # foo.html是手工维护的，所以例外.
  !foo.html
  # 忽略所有.o和 .a文件.
  *.[oa]
  # 配置语法：
  # 以斜杠“/”开头表示目录；
  # 以星号“*”通配多个字符；
  # 以问号“?”通配单个字符
  # 以方括号“[]”包含单个字符的匹配列表；
  # 以叹号“!”表示不忽略(跟踪)匹配到的文件或目录；
  ```

  过滤 mac 和 vscode

  ```conf
  # mac and vscode - plug - Local History
  */.DS_Store
  .history
  # vscode 目录
  .vscode
  ```

- demo 1

  ```conf
  # Eclipse
  .classpath
  .project
  .settings/

  # eclipse and vscode
  *.prefs
  *.factorypath
  *.json

  # Intellij
  .idea/
  _.iml
  _.iws

  # Mac
  .DS_Store

  # Maven
  log/
  target/
  pom.xml.tag
  pom.xml.releaseBackup
  pom.xml.versionsBackup
  pom.xml.next
  release.properties
  dependency-reduced-pom.xml
  buildNumber.properties
  ```

- demo 2

  ```sh
  # Created by .ignore support plugin (hsz.mobi)
  ### Maven template
  target/
  pom.xml.tag
  pom.xml.releaseBackup
  pom.xml.versionsBackup
  pom.xml.next
  release.properties
  dependency-reduced-pom.xml
  buildNumber.properties
  .mvn/timing.properties

  # idea
  .idea/

  ## File-based project format:
  *.iws
  *.iml
  *.ipr

  ## Plugin-specific files:

  # IntelliJ
  /out/

  # mpeltonen/sbt-idea plugin
  .idea_modules/

  # JIRA plugin
  atlassian-ide-plugin.xml

  # Crashlytics plugin (for Android Studio and IntelliJ)
  com_crashlytics_export_strings.xml
  crashlytics.properties
  crashlytics-build.properties
  fabric.properties
  ```

- 删除 git 中的需要过滤的文件

  git 删除

  ```sh
  $ git rm -h

      用法：git rm [<选项>] [--] <文件>...

  -n, --dry-run         演习
  -q, --quiet           不列出删除的文件
  --cached              只从索引区删除
  -f, --force           忽略文件更新状态检查
  -r                    允许递归删除
  --ignore-unmatch      即使没有匹配，也以零状态退出
  ```

- 删除 .idea
