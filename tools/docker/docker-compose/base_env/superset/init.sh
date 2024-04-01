#!/bin/bash

# Create admin user
superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin
            
# 初始化数据库
superset db upgrade

# 加载示例数据
# superset load_examples

# superset 初始化
superset init 

echo "----------------"
echo "web https://localhost:8080"
echo "Starting successful"
bash /usr/bin/run-server.sh