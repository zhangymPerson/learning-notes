# 获取登录 token 

- 获取登录 token
  
  ```shell
  curl --location --request POST 'http://127.0.0.1:8080/api/v1/security/login' \
    --header 'User-Agent: Apifox/1.0.0 (https://apifox.com)' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer ' \
    --data-raw '{
        "username": "admin",
        "password": "admin",
        "refresh": true,
        "provider": "db"
    }'
  ```

- 获取分享图表的 token
  
  ```shell
  curl --location --request POST 'http://127.0.0.1:8080/api/v1/security/guest_token/' \
    --header 'User-Agent: Apifox/1.0.0 (https://apifox.com)' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer ${上面接口获取的 token}' \
    --data-raw '{
        "user": {
            "username": "admin",
            "first_name": "",
            "last_name": ""
        },
        "resources": [
            {
                "type": "dashboard",
                "id": "${Embed 图表的 ID}"
            }
        ],
        "rls": []
    }'
  ```