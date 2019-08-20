# spring中使用mongo


> **注意** spring 中的两种方式，当id的长度为24位的时候，会将普通的id强制转换成Object("id") 对象，在使用时需要注意 

- 两种方式


- 继承

    先定义实体映射bean类对象
    ```java
    //其中 value对应mongo中的集合名(表名) 
    @Document(value = "collection_name")
    public class DocumentBean implements Serializable {

        @Transient
        public Map<String,BlockGraph> blockGraphsMap;

        @Transient
        private List<Path> paths = new LinkedList<>();//答题路径

        /**
         * 主键
         */
        @Id
        private String id;

        @Field(value = "su_name")
        private String suName;//问卷名称

        @Field(value = "su_describe")
        private String suDescribe;//问卷描述
    }
    ```

    继承MongoRepository 接口 可以使用其中默认的查询方法
    ```java
    package org.med.bot.dao;

    import org.med.entity.DocumentBean;
    import org.springframework.data.mongodb.repository.MongoRepository;

    /**
    * @Descroption:
    * DocumentBean 需要使用注解
    **/
    public interface SurveyDao extends MongoRepository<DocumentBean,String> {
        //自定义实现，需自己实现
        Survey findBySuName(String suName);
    }

    ```
- mongoTemplate

    ```java
    // 引入
    @Autowired
    MongoTemplate mongoTemplate;
    //调用举例
    DocumentBean bean = mongoTemplate.findById("5d5a79520d2ef4dc0729e47d00000",DocumentBean.class);
    Map<String,Object> findMap = mongoTemplate.findById("5d5a79520d2ef4dc0729e4", Map.class,"collection_name");
    ```

- mongClient 

    引入相关jar包，制作工具类

    使用mongo的驱动包制作工具类  直接操作  Document 对象，类似map对象操作