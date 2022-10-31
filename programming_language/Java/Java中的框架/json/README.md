# Json的处理

## 框架

- fastjson

    json格式化输出
    ```java
    Bean bean = new Bean();
    String formatStr = JSONObject.toJSONString(bean, SerializerFeature.PrettyFormat, SerializerFeature.WriteMapNullValue, SerializerFeature.WriteDateUseDateFormat);
    System.out.println(formatStr);
    ```
- gson

## 
