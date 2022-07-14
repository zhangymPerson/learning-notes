# cordova配置

## 配置文件

- 在项目的根目录下  `config.xml`

- config.xml 中的配置 最终在 android项目中的配置文件  `AndroidManifest.xml` (`${projectname}/platforms/android/app/src/main/`目录下) 体现  

## 配置文件内容

- 配置app进入后的首页内容


    - 静态页面

    默认是项目根目录下的 www 文件夹内 h5页面的 index.html文件 可修改其他页面
    ```xml
    <content src="index.html" />  
    ```

    - 远程页面 当成普通网页请求

    配置 指定的入口页面 如下
    ```xml
    <content src="http://www.baidu.com" />
    ```

    **注意：配置静态页面，则请求服务会有跨域问题，配置远程页面地址,默认会打开本地浏览器**

- 配置允许webview访问页面

    **否则app会拉动本地的浏览器(手机自带浏览器打开)显示内容。**

    ```xml
    <allow-navigation href="http://*/*" />  
    <allow-navigation href="https://*/*" />  
    <allow-navigation href="data:*" />  

    <access origin="*" />  
    <access origin="http://*/*" />  
    <access origin="https://*/*" />  
    ```
- 不能http访问 需配置

    ```xml
    <edit-config file="AndroidManifest.xml" target="/manifest/application" mode="merge">
    <!--配置允许使用http请求-->
    <activity android:usesCleartextTraffic="true" />        
    </edit-config>
    ```

    ```xml
    <platform name="android">
        <allow-intent href="market:*" />
        <edit-config file="AndroidManifest.xml" target="/manifest/application" mode="merge">
        <!--配置允许使用http请求-->
        <activity android:usesCleartextTraffic="true" />        
        </edit-config>
    </platform>
    ```

- 打开本地的浏览器 配置

    ```xml
    <allow-navigation href="http://*/*" />  
    <allow-navigation href="https://*/*" />  
    <allow-navigation href="data:*" />  

    <access origin="*" />  
    <access origin="http://*/*" />  
    <access origin="https://*/*" />
    ```

    配置位置 与
    ```xml
    <allow-intent href="http://*/*" />
    <allow-intent href="https://*/*" />
    ```
    同一级别

- 配置说明

    ```xml
    <widget id="com.example.hello" version="0.0.1"> 
        <name>HelloWorld</name> 
        <description> 
            A sample Apache Cordova application that responds to the deviceready event.  
        </description> 
        <author email="dev@callback.apache.org" href="http://cordova.io"> 
            Apache Cordova Team  
        </author> 
        <content src="index.html" /> 
        <access origin="*" /> 
    </widget> 
    ```

    widget：id填写app所有人的域名，version填写app的版本号
    
    name：app名称
    
    description：app描述，会在app stroe里显示
    
    author：app作者相关信息，会在app stroe里显示
    
    content：指定app开始指向页面
    
    access：指定app可进行通信的域名，*为所有
    
    preference：偏好设置，可针对不同平台进行个性化设置。

