# cordova配置

## 配置文件位置

    在项目的根目录下  config.xml
## 配置文件内容


- 配置app进入后的首页内容


    默认是项目根目录下的 www 文件夹内 h5页面的 index.html文件 可修改其他页面
    ```xml
    <content src="index.html" />  
    ```

    ```xml
    <content src="http://192.168.8.21:8787/" />
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