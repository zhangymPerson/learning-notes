# git的配置文件

- 配置文件 .gitignore

    配置方式说明

    ```
    # 以'#'开始的行，被视为注释.

    # 忽略掉所有文件名是 foo.txt的文件.

    foo.txt

    # 忽略所有生成的 html文件,

    *.html

    # foo.html是手工维护的，所以例外.

    !foo.html

    # 忽略所有.o和 .a文件.

    *.[oa]
    配置语法：
    以斜杠“/”开头表示目录；
    以星号“*”通配多个字符；
    以问号“?”通配单个字符
    以方括号“[]”包含单个字符的匹配列表；
    以叹号“!”表示不忽略(跟踪)匹配到的文件或目录；
    ```



- demo 1

    ```gitignore

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
    *.iml
    *.iws
    
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
    ```
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


- 删除git中的需要过滤的文件


    git删除
    ```
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