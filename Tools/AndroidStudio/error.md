# 使用error记录

- 第一次安装android studio时候弹出unable to access android sdk add-on list解决方法

    原因是你电脑没有SDK而且你下载的android studio又是不带SDK的；

    解决方法：在自己安装的目录下找到：bin\idea.properties打开这个文件末尾添加一行disable.android.first.run=true