# elasticsearch 中的常用 api 调用

> 本笔记基于 elasticsearch 的 7.X 版本

## 索引相关的 `api` 调用

## 查看所有的索引

  ```sh
  #不带第一行
  http://127.0.0.1:9002/_cat/indices
  #带第一行
  http://127.0.0.1:9200/_cat/indices?v
  ```

### 创建索引

- 请求路由

  ```sh
  #其中indexName是要创建的索引名
  #es 7.0以后没有type的概念
  http://127.0.0.1:9200/indexName
  ```

- 请求方式 **PUT**

- 请求参数 Json

  **注意：7.0 中索引没有 type 的概念，所以 `mappings` 中无 `typeName`,之前的版本创建索引时，需要使用 `type`**

  ```json
  {
    "settings": {
      "index": {
        "number_of_shards": "5",
        "number_of_replicas": "1"
      }
    },
    "mappings": {
      "properties": {
        "id": {
          "type": "long",
          "store": true
        },
        "name": {
          "type": "text",
          "store": true
        },
        "age": {
          "type": "integer",
          "store": true
        },
        "info": {
          "type": "text",
          "store": true
        }
      }
    }
  }
  ```

- 成功返回

  ```json
  {
    "acknowledged": true,
    "shards_acknowledged": true,
    "index": "indexName"
  }
  ```

### 获取索引信息

- 请求路由

  http://127.0.0.1:9200/indexName

- 请求方式 **GET**

- 返回成功

  ```json
  {
    "hellotwo": {
      "aliases": {},
      "mappings": {},
      "settings": {
        "index": {
          "creation_date": "1591596860180",
          "number_of_shards": "5",
          "number_of_replicas": "1",
          "uuid": "-fZNqr29SDGznr479MtlhQ",
          "version": {
            "created": "7060099"
          },
          "provided_name": "indexName"
        }
      }
    }
  }
  ```

### 删除索引信息

- 请求路由

  http://127.0.0.1:9200/indexName

- 请求方式 **DELETE**

- 返回成功

  ```json
  {
    "acknowledged": true
  }
  ```

### 关闭索引

> 如果索引被关闭，那么关于这个索引的所有读写操作都会被阻断。索引的关闭也很简单，请求方式如下：

- 请求路由 /<index>/\_close

  http://127.0.0.1:9200/indexName/_close

- 请求方式 **POST**

### 打开索引

> 关闭索引相对应的是打开索引，请求方式如下：

- 请求路由

  http://127.0.0.1:9200/indexName/_open

- 请求方式 **POST**

### 冻结索引

> 冻结索引和关闭索引类似，关闭索引是既不能读，也不能写。而冻结索引是可以读，但是不能写。冻结索引的请求方式如下：

- 请求路由
  http://127.0.0.1:9200/indexName/_freeze
- 请求方式 **POST**

### 解冻索引

> 与冻结索引对应的是解冻索引，方式如下：

- 请求路由

  http://127.0.0.1:9200/indexName/_unfreez

- 请求方式 **POST**

### 索引字段类型查看和设置

#### 在索引中创建映射

#### 在创建索引的时候可以同时创建映射

- 请求方式/路由 **PUT** /indexName

- 请求参数

  ```json
  {
    "mappings": {
      "properties": {
        "age": { "type": "integer" },
        "email": { "type": "keyword" },
        "name": { "type": "text" }
      }
    }
  }
  ```

#### 在存在的映射中添加字段补充额外的字段

- 请求方式和路由 **PUT** /indexName/\_mapping

  ```json
  {
    "properties": {
      "employee-id": {
        "type": "keyword",
        "index": false
      }
    }
  }
  ```

  请求路由为 索引名称/动作 indexName/\_mapping ，请求体中是需要新添加的映射字段，

  我们指定了字段的类型为 keyword，index 索引为 false，说明这个字段只用于存储，不会用于搜索，搜索这个字段是搜索不到的。

  **在更新字段时候，是不能修改字段的类型的。**

  如果我们要修改字段的类型，需要**新建一个新的字段，指定正确的类型，然后再更新索引**

  以后只需要查询这个新增的字段就可以了

#### 查看索引中的字段映射

> 如果我们要查看已知索引的字段映射，可以向 ES 发送如下的请求：

- 请求方式和路由 GET /indexName/\_mapping
  请求的方法是 GET，请求的路径是我们索引的名称 indexName，再加上一个\_mapping，得到的返回结果如下：

  ```json
  {
    "indexName": {
      "mappings": {
        "properties": {
          "age": {
            "type": "integer"
          },
          "email": {
            "type": "keyword"
          },
          "employee-id": {
            "type": "keyword",
            "index": false
          },
          "name": {
            "type": "text"
          }
        }
      }
    }
  }
  ```

