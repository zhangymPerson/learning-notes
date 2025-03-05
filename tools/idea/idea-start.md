# idea 配置

## 代码模板

- live template

### file and code templates

- 配置位置：Editor > File and Code Templates 配置

- Class 中配置

```java
/**
*
* date ${DATE} ${TIME} <br/>
* description class ${NAME}<br/>
* ${description}
*
* @author zym
*/
```

- interface 中配置

```java
/**
 * date ${DATE} ${TIME} <br/>
 * description interface ${NAME}<br/>
 * ${description}
 *
 * @author zym
 * /
```

- enum 中配置

```java
/**
 *
 * date ${DATE} ${TIME} <br/>
 * description enum ${NAME}<br/>
 * ${description}
 *
 * @author zym
 * /
```

### live template 配置

- 配置位置：Settings > Editor > Live Templates 配置

  新增 Template Group > self-template

  然后找到对应操作系统的 self-template.xml 文件,复制到对应文件中，重启 idea

### 演示模式

- 配置位置：Settings > Appearance & Behavior > Presentation Assistant

  `Show action names and shortcuts in popup` 配置项选中
