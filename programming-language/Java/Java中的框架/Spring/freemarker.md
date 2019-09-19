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
<#if>

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
<#if listKey?? && (listKey?size > 0) >
    xxxx
<#else>
    xxxx
 </#if>
```

- 遍历list
```
<#list keyList as key>
    ${key}
        <#--是否还有元素判断-->
         <#if key_has_next>
            xxx
        </#if>
</#list>
```