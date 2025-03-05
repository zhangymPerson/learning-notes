#! /bin/bash
# 镜像中执行: ./bin/elasticsearch-users useradd admin -p 123456 -r superuser 添加用户
# 索引管理
# 创建索引

USERNAME="admin"
PASSWORD="123456"
ES_URL="http://${USERNAME}:${PASSWORD}@127.0.0.1:9200"
echo "$ES_URL"

# 查看所有索引
echo "查看所有索引"
echo "curl -X GET \"${ES_URL}/_cat/indices?format=json&h=health,status,index,docs.count\""

echo "新建索引"
echo "curl -X PUT \"${ES_URL}/index_name\" -H \"Content-Type: application/json\" -d '{\"settings\":{\"number_of_shards\":1,\"number_of_replicas\":1},\"mappings\":{\"properties\":{\"id\":{\"type\":\"keyword\"},\"username\":{\"type\":\"text\"},\"email\":{\"type\":\"keyword\"},\"created_at\":{\"type\":\"date\"},\"status\":{\"type\":\"integer\"}}}}'"

echo "删除索引"
echo "curl -X DELETE \"${ES_URL}/index_name\""

echo "查看索引"
echo "curl -X GET \"${ES_URL}/_cat/indices?format=json&h=health,status,index,docs.count\""

# 文档管理
# 创建文档（自动ID）
echo "创建文档（自动ID）"
echo "curl -X POST \"${ES_URL}/index_name/_doc\" -H \"Content-Type: application/json\" -d '{\"id\":1001,\"username\":\"john_doe\",\"email\":\"john@example.com\",\"created_at\":\"2025-03-05T11:44:00Z\",\"status\":1}'"

# 查询文档根据id
echo "查询文档根据id"
echo "curl -X GET \"${ES_URL}/index_name/_doc/文档ID\""

# 查看文档全部
echo "查看文档全部"
echo "curl -X GET \"${ES_URL}/index_name/_search\" -H \"Content-Type: application/json\" -d '{\"query\":{\"match_all\":{}},\"from\":0,\"size\":10}'"

# 全量更新文档
echo "全量更新文档"
echo "curl -X PUT \"${ES_URL}/index_name/_doc/文档ID\" -H \"Content-Type: application/json\" -d '{\"id\":1001,\"username\":\"updated_name\",\"email\":\"new@example.com\",\"created_at\":\"2025-03-05T11:44:00Z\",\"status\":2}'"

# 删除文档
echo "删除文档"
echo "curl -X DELETE \"${ES_URL}/index_name/_doc/文档ID\""