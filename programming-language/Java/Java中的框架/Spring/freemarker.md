# FreeMarker 

### 文档说明和介绍

[freemarker-百度百科](https://baike.baidu.com/item/freemarker/9489366?fr=aladdin)

[FreeMarker 中文手册](http://freemarker.foofun.cn/)

### ftl文档中的基本使用

注释格式

```
<#--注释: -->
```

null判断
```
<#--加上括号，感叹号解决对象导航为空的问题-->
value=${(map.name)!"map为null或者name为null"

<#if (variable!"defaultValue") == "targetValue">
是
<#else >
否
</#if>

<#--注释: 判断key是否为null -->
<#if key??>
   ......
<#else>
   ......
</#if>
```


if 判断
```
<#if student_index % 2 == 0>
    xxxx
<#else>
    xxxx
</#if>
```

集合为空判断
```

<#--注释: 判断集合是否存在且长度大于0-->
<#if listKey?? && (listKey?size > 0) >
    xxxx
<#else>
    xxxx
 </#if>

<#--注释: 判断集合是否存在且长度大于0 判断集合第一位元素的值是否为defaule-->
 <#if listKey?? && (listKey?size > 0) && (listKey[0] = "default") >
    xxxx
<#else>
    xxxx
 </#if>
```

- 遍历list
```
<#list keyList as key>
    ${key}
    <#--获取list的下标 使用 key_index即可,下标是从0开始的-->
    <#if key_index = 0>
        ${key}
    <#else >
        ${key?substring(2,4)}
    </#if>
        <#--keyList在key之后是否还有元素判断-->
         <#if key_has_next>
            xxx
        </#if>
</#list>
```

- freemarker字符截取

```
<#--截取第2-4位的字符-->
${key?substring(2,4)}
```


### freemark读取方式

- 读取方式

```java

#主要依赖的连个类
import freemarker.template.Configuration;
import freemarker.template.Template;


    /**
     * 
     * TODO
     * <br>
     * @author kangxu2 2016-11-23
     *
     * @param fltFile  flt文件名
     * @param templatePath flt文件路径   src/template
     * @param datas 数据集合
     * @return
     */
    public static String geneFileStr(String fltFile,String templatePath,Map<String, Object> datas){
        #配置类
        Configuration cfg = new Configuration();
        try {
            #文件夹位置 
            cfg.setDirectoryForTemplateLoading(new File(templatePath));
            #编码格式 和文件
            Template template = cfg.getTemplate(fltFile,Constants.ENCODING);
            template.setEncoding(Constants.ENCODING);
            StringWriter out = new StringWriter();  
            template.process(datas, out);  
            out.flush();
            out.close();
            return out.getBuffer().toString();
        } catch (Exception e) {
            e.printStackTrace();
        } 
        
        return null;
        
    }

```