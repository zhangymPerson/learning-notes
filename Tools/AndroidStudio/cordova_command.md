## cordova的命令和使用

- 创建项目

    跳转到你维护源代码的目录中，并创建你的cordova项目
    ```sh
    #创建测试app
    cordova create hello com.example.hello HelloWorld
    ```
    这将会为你的cordova应用创造必须的目录。默认情况下，cordova create命令生成基于web的应用程序的骨骼，项目的主页是 www/index.html 文件

- 项目结构

    ```
    myapp/
    |-- config.xml
    |-- hooks/
    |-- merges/
    | | |-- android/
    | | |-- windows/
    | | |-- ios/
    |-- www/
    |-- platforms/
    | |-- android/
    | |-- windows/
    | |-- ios/
    |-- plugins/
    |--cordova-plugin-camera/
    ```

- 添加平台

    所有后续命令都需要在项目目录或者项目目录的任何子目录运行:
    ```sh
    $ cd hello
    ```
    给你的App添加目标平台。我们将会添加'ios'和'android'平台，并确保他们保存在了config.xml中:
    ```sh
    $ cordova platform add ios --save
    $ cordova platform add android --save
    ```
    检查你当前平台设置状况:
    ```sh
    $ cordova platform ls
    ```
    运行add或者remove平台的命令将会影响项目 platforms的内容，在这个目录中每个指定平台都有一个子目录。

- 安装构建先决条件

    要构建和运行App，你需要安装每个你需要平台的SDK。另外，当你使用浏览器开发你可以添加 browser平台，它不需要任何平台SDK。

    检测你是否满足构建平台的要求:

    ```sh
    $ cordova requirements
    Requirements check results for android:
    Java JDK: installed .
    Android SDK: installed
    Android target: installed android-19,android-21,android-22,android-23,Google Inc.:Google APIs:19,Google Inc.:Google APIs (x86 System Image):19,Google Inc.:Google APIs:23
    Gradle: installed

    Requirements check results for ios:
    Apple OS X: not installed
    Cordova tooling for iOS requires Apple OS X
    Error: Some of requirements check failed
    ```

- 构建app

    默认情况下, cordova create生产基于web应用程序的骨架，项目开始页面位于www/index.html 文件。任何初始化任务应该在www/js/index.js文件中的deviceready事件的事件处理函数中。

    运行下面命令为所有添加的平台构建:
    ```sh
    $ cordova build
    ```
    你可以在每次构建中选择限制平台范围 - 这个例子中是'ios':
    ```sh
    $ cordova build ios
    ```