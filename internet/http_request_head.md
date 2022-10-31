# http 请求的 head 参数解析

> 按照浏览器中的调试的顺序 进行分析理解

> 打开浏览器，请求网站资源 按 F12 可以看到调试框， network -> 点开任意一个请求 -> Headers

## General

- Request URL

  请求地址: 如：https://ip:port/path/_/_

- Request Method

  请求方式

  如 GET POST PUT ...

- Status Code

  本次请求结果状态码

  如 200 请求成功

- Remote Address

  远程请求地址 ip:port

- Referrer Policy

  referrer 是 HTTP 请求 header 的报文头，用于指明当前流量的来源参考页面。

  当用户在浏览器上点击一个链接时，会产生一个 HTTP 请求，用于获取新的页面内容，而在该请求的报头中，会包含一个 Referrer;

  用以指定该请求是从哪个页面跳转页来的，常被用于分析用户来源等信息。

  **但是也有成为用户的一个不安全因素，比如有些网站直接将 sessionid 或是 token 放在地址栏里传递的，会原样不动地当作 Referrer 报头的内容传递给第三方网站。**

  所以就有了 Referrer Policy，用于过滤 Referrer 报头内容，目前是一个候选标准，不过已经有部分浏览器支持该标准。具体的可查看这里。

## Response Headers

- Bdpagetype

- Bdqid

- Connection

- Content-Encoding

- Content-Length

- Content-Type

  返回头中 表示

  客户端实际返回内容的类型

- Date

  请求时间

- Is_status

- Server

  后台服务名称 常见的如 nginx/apache 等

- Set-Cookie

- Strict-Transport-Security:

- Traceid

- Vary

- X-Ua-Compatible

## Request Headers

- Accept

- Accept-Encoding

- Accept-Language

- Connection

- Cookie

- Host

  请求服务的 IP:port

- is_referer

- is_xhr

- **Referer**

  [百度百科](https://baike.baidu.com/item/HTTP_REFERER)

  HTTP Referer 是 header 的一部分，当浏览器向 web 服务器发送请求的时候，一般会带上 Referer，告诉服务器该网页是从哪个页面链接过来的，服务器因此可以获得一些信息用于处理。

- Sec-Fetch-Mode

- Sec-Fetch-Site

- User-Agent

- X-Requested-With

- Content-Type

  请求头中 表示

  客户端要请求的内容的类型

## Query String Parameters

    当发起一次GET请求时，参数会以url string的形式进行传递。即?后的字符串则为其请求参数，并以&作为分隔符。

## Request Payload

    当发起一次POST请求时;若content-type为application/json;则参数会以Request Payload的形式进行传递（显然的，数据格式为JSON）

## Form Data

    当发起一次POST请求时，若未指定content-type，则默认content-type为application/x-www-form-urlencoded。即参数会以Form Data的形式进行传递，不会显式出现在请求url中。

- 注意

  首部属性 contentType 可以改变请求的数据提交方式：application/json(payload)，application/x-www-form-urlencoded(formData)

  **服务端的响应方式决定客户端的提交方式**

### 响应数据乱码的几种情形

1.返回的值不是 utf-8 的时候，会出现乱码

2.返回类型是 **Content-Encoding: gzip** , 这个时候出现 postman 请求正常解析，curl 命令/编程语言代码是乱码的问题/

curl 命令 curl \*\*\*(正常请求的参数) | gunzip | more
