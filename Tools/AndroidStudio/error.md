# 使用 error 记录

- 第一次安装 android studio 时候弹出 unable to access android sdk add-on list 解决方法

  原因是你电脑没有 SDK 而且你下载的 android studio 又是不带 SDK 的；

  解决方法：在自己安装的目录下找到：bin\idea.properties 打开这个文件末尾添加一行 disable.android.first.run=true

- 安卓生成 keystore 命令乱码问题 win10 命令行乱码

  解决办法 在命令行运行

  `chcp 936`
