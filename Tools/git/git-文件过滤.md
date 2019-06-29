# git的配置文件

- 配置文件 .gitignore

- demo 1
```

# Eclipse
.classpath
.project
.settings/
 
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