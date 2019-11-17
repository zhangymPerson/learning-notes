# html学习笔记

- 基本标签学习

    ```html
    <!--前端页面 格式声明 大小写均可-->
    <!doctype html>
    <!--<!DOCTYPE html>-->
    <!--文档根标签-->
    <html>
    <!--文档头标签 可以引用脚步文件、指定样式表、书写代码逻辑块、提供元信息-->
    <head>
    <!--  mete是元标签字符编码-->
    <meta charset="utf-8"/>

    <!--  文档tag标题标签，设置文档tag的标题内容 -->
    <title>浏览器上显示页面的名称</title>

    <!--  link（链接标签）-->
    <!--  外联样式表-->
    <link rel="stylesheet" type="text/css" href="style.css"/>
    <!--  文档tag图标-->
    <link rel="shortcut icon" type="image/x-icon" href="http://www.baidu.com/favicon.ico"/>

    <!--  内联样式表-->
    <style></style>

    <!--脚本标签-->
    <script type="text/javascript"></script>
    </head>
    <!--文档主体标签 页面内容部分 包含文档所有文本与超文本内容-->
    <body>
    <!--  <hn>: n的取值范围是1~6; 从大到小. 用来表示标题.-->
    <!--  <p>: 段落标签. 包裹的内容被换行.并且也上下内容之间有一行空白.-->
    <!--  <b> <strong>: 加粗标签.-->
    <!--  <strike>: 为文字加上一条中线.-->
    <!--  <sup>和<sub>: 上角标 和 下角表.-->
    <!--  <br>:换行.-->
    <!--  <hr>:水平线-->
    <!--  <div>只是一个块级元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现.-->
    <div>
    <!--  最多到h6.无h7和h8-->
    <h1>H1标题</h1>
    <h2>H2标题</h2>
    <h3>H3标题</h3>
    <h4>H4标题</h4>
    <h5>H5标题</h5>
    <h6>H6标题</h6>
    <h7>H7标题</h7>
    <h8>H8标题</h8>
    </div>

    <div>
    <!--  标签定义超链接，用于从一个页面链接到另一个页面。-->
    <!--  <a> 元素最重要的属性是 href 属性，它指定链接的目标。-->
    <a href="https://github.com/zhangymPerson">我的GitHub地址链接地址</a>
    </div>
    </body>
    </html>
    ```