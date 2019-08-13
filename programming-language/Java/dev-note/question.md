# 开发问题记录

- Json转有序Map-基于fastjson

    ```java
        //json转有序maps
        String jsonStr
        JSONObject jsonObject = JSONObject.parseObject(jsonStr, Feature.OrderedField);
    ```