# java中注释规范

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

    - @see用法
    
        注解@see可以在注释中实现链接跳转.@see可以指向包,类,方法,属性.

- 个人使用 java类注释

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
		return "";
	}
    ```

### 属性




### 常量


- idea 中配置类注释模板

    setting -> editor -> File and Code Templates - File - Class中添加

    ```java
    /**
    * date ${DATE} ${TIME} <br/>
    * descriptionclass <br/>
    * @author danao
    * @version 1.0
    * @since 1.0
    */
    ```