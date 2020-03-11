# Android项目结构

## 在android studio 项目结构

- 结构说明
    
    - .gradle： Gradle编译系统，版本由wrapper指定
    - .idea：IDE所需要的文件
    - app：开发项目的所有代码和资源文件
    - app/build：app模块编译输出的文件
    - app/libs： 放置引用的类库文件
    - app/src： 放置应用的主要文件目录
    - app/src/androidTest：单元测试目录

    - **app/src/main：主要的项目目录和代码**

    - app/src/main/assets：放置原生文件，里面的文件会保留原有格式，文件的读取需要通过流

    - **app/src/main/java：项目的源代码**

    - **app/src/main/res：**项目的资源**

    - app/src/main/res/anim：存放动画的XML文件
    - app/src/main/res/drawable：存放各种位图文件(.png，.jpg，.9png，.gif等)和drawable类型的XML文件
    - app/src/main/res/drawable-v24：存放自定义Drawables类（Android API 24 开始，可在XML中使用）
    - app/src/main/res/layout：存放布局文件
    - app/src/main/res/menu：存放菜单文件
    - app/src/main/res/mipmap-hdpi：存放高分辨率图片资源
    - app/src/main/res/mipmap-mdpi：存放中等分辨率图片资源
    - app/src/main/res/mipmap-xdpi：存放超高分辨率图片资源
    - app/src/main/res/mipmap-xxdpi：存放超超分辨率图片资源
    - app/src/main/res/mipmap-xxxdpi：存放超超超高分辨率图片资源
    - app/src/main/res/raw：存放各种原生资源(音频，视频，一些XML文件等)
    - app/src/main/res/values： 存放各种配置资源（颜色，尺寸，样式，字符串等）
    - app/src/main/res/values/attrs.xml：自定义控件时用的较多，自定义控件的属性
    - app/src/main/res/values/arrays.xml：定义数组资源
    - app/src/main/res/values/colors.xml：定义颜色资源
    - app/src/main/res/values/dimens.xml：定义尺寸资源
    - app/src/main/res/values/string.xml：定义字符串资源
    - app/src/main/res/values/styles.xml：定义样式资源
    - app/src/main/res/values-v11：在API 11+的设备上调用
    - app/src/main/res/values-v14：在API 14+的设备上调用
    - app/src/main/res/values-v21：在API 21+的设备上调用
    - app/src/main/res/AndroidManifest.xml：项目的清单文件（名称、版本、SDK、权限等配置信息）
    - app/src/.gitignore：忽略的文件或者目录
    - app/app.iml：app模块的配置文件
    - app/build.gradle：app模块的gradle编译文件
    - app/proguard-rules.pro：app模块的代码混淆配置文件
    - build：系统生成的文件目录


    - gradle: wrapper的jar和配置文件所在的位置
    - .gitattributes：用于设置文件的对比方式
    - .gitignore： 忽略的文件或者目录
    - build.gradle：项目的gradle编译文件
    - gradle.properties： gradle相关的全局属性设置
    - gradlew： 编译脚本，可以在命令行执行打包
    - gradlew.bat：windows下的gradle wrapper可执行文件
    - local.properties：配置SDK/NDK所在的路径
    - MyApplication.iml：保存该模块的相关信息
    - README.md：文本编辑器，记录一些相关信息
    - settings.gradle：设置相关的gradle脚本
    - External Libraries：项目依赖的库，编译时自动下载
    
