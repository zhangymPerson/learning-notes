# openapi 代码生成使用教程

- 使用方式
- 启动 docker-compose 镜像

  访问 `http://127.0.0.1:8080`

- 定义 openapi.yaml 文件

  输入 openapi.yaml 文件的位置生成对应的代码

- openapi-geenrate 生成代码

  生成代码

- 使用 `docker` 启动 `openapi-generator-online` 服务
  
  `docker compose up -d`

  ```shell
  # 获取所以支持的客户端
  curl -X GET "http://127.0.0.1:8080/api/gen/clients" -H "Accept: */*"

  # 根据 openapi.yaml 或者 openapi.json 生成代码
  # 举例如下 地址为:http://localhost/api/swagger/doc.json 客户端语言为: client-language 可以设置 为 java/go/markdown 等 
  curl -X POST "http://127.0.0.1:8080/api/gen/clients/{client-language}" -H "Accept: */*" -H "Content-Type: application/json" -d "{ \"openAPIUrl\": \"http://localhost/api/swagger/doc.json\"}"
  ```