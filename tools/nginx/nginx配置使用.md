# nginx 的配置使用

- 配置文件查找

  ```sh
  #查找配置文件位置
  nginx -t

  vim nginx.conf
  ```

- 常见问题

  **代理找不到页面 需要查看代理页面的路径**

  **代理找不到静态资源 可以直接配置到静态资源所在的位置**

  **找不到静态资源 可以将报 404 的路径配置到 nginx location{}中**

  如 `http://host:port/path/*.css` 等资源报错 404

  配置如下

  ```conf
  #找不到资源的路径 浏览器F12可查看相关内容
  location /path {
      proxy_pass http://代理ip:port;
  }
  ```

  多个路径的配置方法

  ```conf
  # 配置格式前必须加上 ~ 多个路径用 | 隔开
  # 后面配置要代理的路由
  location ~ /(stylesheets|javascripts|api|img)/ {
      proxy_pass http://ip:port;
  }
  ```

## nginx 配置 关键字说明 root / alias

- root

  location 和 root 组合相当于 在 root 指定目录下 进行 location 匹配，location 所匹配内容必须保证在 root 指定目录的子目录，否则配置无效，

  而且 location 只能向下匹配，不能匹配 location 指定目录上一级目录中的内容。

  eg:

  ```conf
  {
      listen 80;
      server_name loaction;
      location /root {
          alias /data/root;
      }
  }
  ```

  以上配置匹配的是 在 /data/root/root/ 目录及其子目录下 匹配文件

- alias

  location 与 alias 组合，需要保证 location 匹配目录与 alias 指定目录级别相同，否则配置无效，

  location 和 root 组合相同的是，location 所匹配内容也只能向下匹配。

  eg:

  静态资源配置参考：

  配置在这个 <http://host:port/root/file.name> 请求下请求静态文件

  假设 file.name 在 /data/alias/file.name 这个位置

  则配置如下

  ```conf
  server {
      listen 80;
      server_name location;
      # 此处配置需要注意
      # location 后面跟匹配的路由 alias后面跟资源所在目录
      # 如果 配置的是 /root/ 则 alias 配置为 /data/alias/
      # 如果 配置的是 /root  则 alias 配置为 /data/alias
      location /root {
          alias /data/alias;
      }
  }
  ```

  以上配置是在 /data/alias/ 目录及其子目录下 匹配文件

  > 相同点 ：都只能向下匹配
  > 不同点 查找`**.filetype`文件 root 指定的位置是在 `${root}/location/*下 匹配 **.filetype` 而 alias 匹配的是 `${alias}/* 下**.filetype` 文件

- 配置端口转发时 添加路由地址的配置

  假设请求 <http://127.0.0.1:4000> 下的 test 接口

  第一种配置

  ```conf
  location /git {
      proxy_pass http://127.0.0.1:4000;
      proxy_redirect default;
  }
  ```

  > 请求的位置是 <http://127.0.0.1:4000/>**git/test**

  第二种配置

  ```conf
  location /git {
      proxy_pass http://127.0.0.1:4000/;
      proxy_redirect default;
  }
  ```

  > 请求的位置是 <http://127.0.0.1:4000/>**test**

  两种去掉去掉请求前缀配置的方式

  - `proxy_pass`后面加根路径 '/' 可以去掉配置的请求路由前缀

  - 在`location{}`配置中添加`rewrite ^/git/(.*)$ /$1 break;`配置

    **区别： 配置转发路由时，如果末尾使用'/'结尾，则不添加 location 后面的参数，否则添加**

## 显示文件夹目录

- 配置说明

  ```conf
    {
      listen 80;
      server_name location;
      location /root {
          root /data/;  //指定实际目录绝对路径 root 匹配 /data/root/下文件
          autoindex on;  //开启目录浏览功能；
          autoindex_exact_size off; //关闭详细文件大小统计，让文件大小显示MB，GB单位，默认为b；
          autoindex_localtime on; //开启以服务器本地时区显示文件修改日期！
      }
  }
  ```

## 配置 nginx 获取真实的 IP

- 配置说明

  ```conf
  server {
      listen 80;
      server_name _;
      location / {
          ..................
          proxy_pass         http://127.0.0.1:8000/;
          # $host 变量，Host 为变量名
          proxy_set_header   host             $host;
          proxy_set_header   X-Real-IP        $remote_addr;
          proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;

      }
  }

  ```

- 获取真实 ip 的代码

## 配置文件解析

- 图片说明
  ![配置文件结构说明](../../Picture/nginx%E7%9A%84%E9%85%8D%E7%BD%AE%E5%9D%97%E8%AF%B4%E6%98%8E.png)

- 配置 demo

  ```conf
  #运行用户
  user www-data; 
  #启动进程,通常设置成和cpu的数量相等
  worker_processes 1;
   
  #全局错误日志及PID文件
  error_log /var/log/nginx/error.log;
  pid    /var/run/nginx.pid;
   
  #工作模式及连接数上限
  events {
    use  epoll;       #epoll是多路复用IO(I/O Multiplexing)中的一种方式,但是仅用于linux2.6以上内核,可以大大提高nginx的性能
    worker_connections 1024;#单个后台worker process进程的最大并发链接数
    # multi_accept on;
  }
   
  #设定http服务器，利用它的反向代理功能提供负载均衡支持
  http {
     #设定mime类型,类型由mime.type文件定义
    include    /etc/nginx/mime.types;
    default_type application/octet-stream;
    #设定日志格式
    access_log  /var/log/nginx/access.log;
   
    #sendfile 指令指定 nginx 是否调用 sendfile 函数（zero copy 方式）来输出文件，对于普通应用，
    #必须设为 on,如果用来进行下载等应用磁盘IO重负载应用，可设置为 off，以平衡磁盘与网络I/O处理速度，降低系统的uptime.
    sendfile    on;
    #tcp_nopush   on;
   
    #连接超时时间
    #keepalive_timeout 0;
    keepalive_timeout 65;
    tcp_nodelay    on;
     
    #开启gzip压缩
    gzip on;
    gzip_disable "MSIE [1-6]\.(?!.*SV1)";
   
    #设定请求缓冲
    client_header_buffer_size  1k;
    large_client_header_buffers 4 4k;
   
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
   
    #设定负载均衡的服务器列表
     upstream mysvr {
    #weigth参数表示权值，权值越高被分配到的几率越大
    #本机上的Squid开启3128端口
    server 192.168.8.1:3128 weight=5;
    server 192.168.8.2:80 weight=1;
    server 192.168.8.3:80 weight=6;
    }
   
   
    server {
    #侦听80端口
      listen    80;
      #定义使用www.xx.com访问
      server_name www.xx.com;
      #设定本虚拟主机的访问日志
      access_log logs/www.xx.com.access.log main;
    #默认请求
    location  {
       root  /root;   #定义服务器的默认网站根目录位置
       index index.php index.html index.htm;  #定义首页索引文件的名称
   
       fastcgi_pass www.xx.com;
       fastcgi_param SCRIPT_FILENAME $document_root/$fastcgi_script_name;
       include /etc/nginx/fastcgi_params;
      }
   
    # 定义错误提示页面
    error_page  500 502 503 504 /50x.html;
      location = /50x.html {
      root  /root;
    }
   
    #静态文件，nginx自己处理
    location ~ ^/(images|javascript|js|css|flash|media|static)/ {
      root /var/www/virtual/htdocs;
      #过期30天，静态文件不怎么更新，过期可以设大一点，如果频繁更新，则可以设置得小一点。
      expires 30d;
    }
    #PHP 脚本请求全部转发到 FastCGI处理. 使用FastCGI默认配置.
    location ~ \.php$ {
      root /root;
      fastcgi_pass 127.0.0.1:9000;
      fastcgi_index index.php;
      fastcgi_param SCRIPT_FILENAME /home/www/www$fastcgi_script_name;
      include fastcgi_params;
    }
    #设定查看Nginx状态的地址
    location /NginxStatus {
      stub_status      on;
      access_log       on;
      auth_basic       "NginxStatus";
      auth_basic_user_file conf/htpasswd;
    }
    #禁止访问 .htxxx 文件
    location ~ /\.ht {
      deny all;
    }
      
     }
  }
  ```

- nginx 配置服务端口指向另一个端口

  监听 8080 指向 8888 端口的服务;

  ```conf
  server{
      listen 8080;
      location / {
          proxy_pass http://127.0.0.1:8888;
          proxy_redirect default;
      }
  }
  ```

  - nginx 默认配置文件

  ```conf

  # For more information on configuration, see:
  #   * Official English Documentation: http://nginx.org/en/docs/
  #   * Official Russian Documentation: http://nginx.org/ru/docs/

  user nginx;
  worker_processes auto;
  error_log /var/log/nginx/error.log;
  pid /run/nginx.pid;

  # Load dynamic modules. See /usr/share/nginx/README.dynamic.
  include /usr/share/nginx/modules/*.conf;

  events {
      worker_connections 1024;
  }

  http {
      log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

      access_log  /var/log/nginx/access.log  main;

      sendfile            on;
      tcp_nopush          on;
      tcp_nodelay         on;
      keepalive_timeout   65;
      types_hash_max_size 2048;

      include             /etc/nginx/mime.types;
      default_type        application/octet-stream;

      # Load modular configuration files from the /etc/nginx/conf.d directory.
      # See http://nginx.org/en/docs/ngx_core_module.html#include
      # for more information.
      include /etc/nginx/conf.d/*.conf;

      server {
          listen       80 default_server;
          listen       [::]:80 default_server;
          server_name  _;
          root         /usr/share/nginx/html;

          # Load configuration files for the default server block.
          include /etc/nginx/default.d/*.conf;

          location / {
          }

          error_page 404 /404.html;
              location = /40x.html {
          }

          error_page 500 502 503 504 /50x.html;
              location = /50x.html {
          }
      }

  # Settings for a TLS enabled server.
  #
  #    server {
  #        listen       443 ssl http2 default_server;
  #        listen       [::]:443 ssl http2 default_server;
  #        server_name  _;
  #        root         /usr/share/nginx/html;
  #
  #        ssl_certificate "/etc/pki/nginx/server.crt";
  #        ssl_certificate_key "/etc/pki/nginx/private/server.key";
  #        ssl_session_cache shared:SSL:1m;
  #        ssl_session_timeout  10m;
  #        ssl_ciphers HIGH:!aNULL:!MD5;
  #        ssl_prefer_server_ciphers on;
  #
  #        # Load configuration files for the default server block.
  #        include /etc/nginx/default.d/*.conf;
  #
  #        location / {
  #        }
  #
  #        error_page 404 /404.html;
  #            location = /40x.html {
  #        }
  #
  #        error_page 500 502 503 504 /50x.html;
  #            location = /50x.html {
  #        }
  #    }

  }
  ```
