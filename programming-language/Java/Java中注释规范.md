# Java 中注释规范

- [返回](./README.md)

### 包注释

- 包注解在工作中往往比较特殊，通过包注解可以快速知悉当前包下代码是用来实现哪些功能，强烈建议工作中加上，尤其是对于一些比较复杂的包，包注解一般在包的根目录下，名称统一为 package-info.java。

  ```java
  /**
  * 功能描述
  * 1. 用来解决什么问题
  * 主要用来封装数据库读取相关的mapping类
  *
  * 2. 如何实现
  * 根据数据库表结构实现
  *
  * 注意事项：
  * 需要引入jdbc依赖包才能使用
  * @author danao
  * @date 2021/1/27
  */
  package cn.danao.dao.mapping;
  ```

### 类

- 中文

  ```java
  /**
  * 文 件 名 :
  * CopyRright (c) 2008-xxxx:
  * 文件编号：
  * 创 建 人：
  * 日    期：
  * 修 改 人：
  * 日   期：
  * 描   述：
  * 版 本 号：
  */
  public class Test(){

  }
  ```

- 英文

  ```java
  /**
  * CopyRright (c)2008-xxxx:   <展望软件Forsoft >
  * Project:                     <项目工程名 >
  * Module ID:   <(模块)类编号，可以引用系统设计中的类编号>
  * Comments:  <对此类的描述，可以引用系统设计中的描述>
  * JDK version used:      <JDK1.6>
  * Namespace:           <命名空间>
  * Author：        <作者中文名或拼音缩写>
  * Create Date：  <创建日期，格式:YYYY-MM-DD>
  * Modified By：   <修改人中文名或拼音缩写>
  * Modified Date:  <修改日期，格式:YYYY-MM-DD>
  * Why & What is modified  <修改原因描述>
  * Version:                <版本号>
  */
  public class Test(){

  }
  ```

  - @see 用法

    注解@see 可以在注释中实现链接跳转.@see 可以指向包,类,方法,属性.

  ```java
  /**
  * Copyright (C), 2019-2020, Jann  balabala...
  *
  * 类的介绍：这是一个用来做什么事情的类，有哪些功能，用到的技术.....
  *
  * @author   类创建者姓名 保持对齐
  * @date     创建日期 保持对齐
  * @version  版本号 保持对齐
  */
  public class Test(){
      //在每个属性前面必须加上属性注释，通常有一下两种形式，至于怎么选择，你高兴就好，不过一个项目中要保持统一。
      /** 提示信息 */
      private String userName;/
      /**
      * 密码
      */
      private String password;

      /**
      * 构造方法的详细说明
      *
      * @param xxx      参数1的使用说明， 能否为null
      * @throws 异常类型   注明从此类方法中抛出异常的说明
      */
      public Test(){
          super();
      }
  }
  ```

- 个人使用 java 类注释

  ```java
  /**
  * 该类的作用是:<br/>
  * 1.****************<br/>
  * 2.****************<br/>
  * 3.****************<br/>
  * email zhangyanmingjiayou@163.com<br/>
  * date 2019-02-12 <br/>
  * @author zhangym
  * @version 1.0
  * @since 1.0
  */
  public class Test(){

  }
  ```

- 修改后的注释

  ```java
  /** 
  * @UpdateUser:   [${user}]   
  * @UpdateDate:   [${date} ${time}]   
  * @UpdateRemark: [说明本次修改内容]  
  * @Version:      [v1.0] 
  */
  ```

### 函数-方法

- 方法中的注释

  ```java
  /**
  * 该函数的作用是:
  * 1.***************
  * 2.***************
  * 3.***************
  * @param test 参数1的说明
  * @param num 参数2的说明
  * @return 返回值的说明
  */
  public String getBest(String test,int num){
      int id = 1; // 反例：不要使用行尾注释

      //反例：换行符与注释之间没有缩进
      int age = 18;
      // 正例：姓名
      String name;

      /**
      * 1. 多行注释
      *
      * 2. 对于不同的逻辑说明，可以用空行分隔
      */
      return "";
  }
  ```

  ```java
   /**
     * 方法的详细说明，能干嘛，怎么实现的，注意事项...
     *
     * @param test 参数1的使用说明， 能否为null
     * @return 返回结果的说明， 不同情况下会返回怎样的结果
     * @throws Exception 注明从此类方法中抛出异常的说明
     */
    public String getBest(String test, int num) throws Exception {
        return "";
    }
  ```

### 属性

### 常量

- idea 中配置类注释模板

  setting -> editor -> File and Code Templates - File - Class 中添加

  ```java
  /**
  * date ${DATE} ${TIME} <br/>
  * descriptionclass <br/>
  * @author danao
  * @version 1.0
  * @since 1.0
  */
  ```

## 其他注释方式
