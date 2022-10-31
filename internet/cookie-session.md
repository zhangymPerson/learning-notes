# cookie-session

## cookie 

- Cookie 介绍

    [百度百科](https://baike.baidu.com/item/cookie/1119)

    Cookie的主要内容包括：名字，值，过期时间，路径和域。key:value格式；
    
    浏览器提供了一种叫cookie的机制，保存当前会话的唯一标识。每次HTTP请求，客户端都会发送相应的Cookie信 息到服务端。客户端第一次请求，由于cookie中并没有携 带sessionid，服务端会创建一个sessionid，写入到客户端 的 cookie 中。以后每次请求，都会携带这个 id 给到服务 器端。这样一来，便解决了无状态的问题。[如果客户端浏 览器禁用了cookie，一般会通过URL重写的方式来进行会 话会话嗯个总，也就是在url中携带sessionid] 

    Cookie 是在 HTTP 协议下，服务器或脚本可以维护客户工作站上信息的一种方式。Cookie 是由 Web 服务器保存在用户浏览器（客户端）上的小文本文件，它可以包含有关用户的信息。无论何时用户链接到服务器，Web 站点都可以访问 Cookie 信息；

## session

- Session介绍

    [session-百度百科](https://baike.baidu.com/item/session/479100)

    Http协议本身是无状态的，客户端只需要简单的向服务器 请求下载某些文件，无论是客户端还是服务器都没必要记 录彼此过去的行为，每一次请求之间是独立的 然后我们很快发现如果能够提供一些按照需要生成的动态信息会使web变得更加有用。比如我们做了一个需要登录 授权才能执行的动作，但是因为http协议没办法保存这个 登录的用户的状态，因此当下一次再执行一个需要授权操 作时，还需要再次登录。这将导致用户体验非常差。因此 需要一种机制能够识别每次请求的用户，来实现会话保存 的目的。

    Session 服务端提供了一种叫 Session 的机制，对于每个用户的请 求，会生成一个唯一的标识。当程序需要为某个客户端的 请求创建一个 session 的时候，服务器首先检查这个客户 端的请求是否包含了一个session标识- session id； 如果已包含一个session id 则说明以前已经为客户端创建 过session，服务器就按照session id 把这个session检索 出来使用（如果检索不到，会新建一个）； 如果客户端请求不包含sessionid，则为此客户端创建一个 session 并且生成一个与此 session 相关联的 session id， session id的值是一个既不会重复，又不容易被找到规律的 仿造字符串。 

## Session共享问题

- 集群和负载

    如果网站请求流量较大，那么单个服务器是无法承接这些流量的，这个时候就需要开始对服务器做集群。
 
    关于负载均衡 
    负载均衡的主要目的是：把用户的请求分发到多台后端的 设备上，用以均衡服务器的负载。我们可以把负载均衡器 划分为两大类：硬件负载均衡器和软件负载均衡器。 

    硬件负载 
    最常用的硬件负载设备有 F5 和 netscaler、Redware，F5 是基于4层负载，netscaler是7层负载。 

    软件负载 
    比较主流的开源软件负载技术有: lvs、HAProxy、Nginx等，

- 负载均衡算法 

    轮询算法及加权轮询算 

    最小连接数

    随机算法 

    哈希算法 

- session共享


    session sticky 

    session sticky(粘性) , 保证同一个会话的请求都在同一个 web 服务器上处理，这样的话，就完全不需要考虑到会话 的问题了。比如前面说的负载均衡算法中，哈希算法就是 一个典型的实现手段。


    session replication 

    session复制，通过相关技术实现session复制，使得集群 中的各个服务器相互保存各自节点存储的 session 数据。 tomcat本身就可以实现session复制的功能，基于IP组播 放方式。

    session 统一存储 
    
    集群中的各个节点的 session 数据，统一存储到一个存储 设备中。那么每个节点去拿session的时候，就不是从自己 的内存中去获得，而是从相应的第三方存储中去拿。对于 这个方案来说，无论是哪个节点新增或者修改了session数 据，最终都会发生在这个集中存储的地方。 这个存储设备可以是redis、也可以是mysql。 

    Cookie Based 

    Cookie Based 方法，简单来说，就是不依赖容器本身的 Session机制。 而是服务端基于一定的算法，生成一个token给到客户端， 客户端每次请求，都会携带这个token。 当服务端收到 token 以后，先验证 token 是否有效，再解密这个token获取关键数据进行处理  

## cookie和session区别

- 区别
    
    存储数据量方面：session 能够存储任意的 java 对象，cookie 只能存储 String 类型的对象，数据对象大小限制

    一个在客户端一个在服务端。因Cookie在客户端所以可以编辑伪造，不是十分安全。cookie不可信

    Session过多时会消耗服务器资源，大型网站会有专门Session服务器，Cookie存在客户端没问题。session 共享问题

    域的支持范围不一样，比方说a.com的Cookie在a.com下都能用，而www.a.com的Session在api.a.com下都不能用，解决这个问题的办法是JSONP或者跨域资源共享。

    cookie数据存放在客户的浏览器上，session数据放在服务器上

    cookie不是很安全，别人可以分析存放在本地的cookie并进行cookie欺骗，考虑*到安全应当使用session

    session会在一定时间内保存在服务器上，当访问增多，会比较占用你服务器的性能，考虑到减轻服务器性能方面，应当使用cookie

    单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie

    建议将登录信息等重要信息存放为session，其他信息如果需要保留，可以放在cookie中

    session保存在服务器，客户端不知道其中的信息；cookie保存在客户端，服务器能够知道其中的信息

    session中保存的是对象，cookie中保存的是字符串

    session不能区分路径，同一个用户在访问一个网站期间，所有的session在任何一个地方都可以访问到，而cookie中如果设置了路径参数，那么同一个网站中不同路径下的cookie互相是访问不到的

