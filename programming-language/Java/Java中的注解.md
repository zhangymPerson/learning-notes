#  Java中的注解

### 编写自定义注解需要的基础知识，

- 编写自定义注解需要使用的Java元注解，有四种元注解：@Retention、@Inherited、@Documented、@Target

- @Retention

    注解的保留位置（枚举RetentionPolicy），RetentionPolicy可选值：

        SOURCE：注解仅存在于源码中，在class字节码文件中不包含
        CLASS：默认的保留策略，注解在class字节码文件中存在，但运行时无法获得
        RUNTIME：注解在class字节码文件中存在，在运行时可以通过反射获取到

- @Inherited
  
    声明子类可以继承此注解，如果一个类使用此注解，则该类的子类也继承此注解；

- @Documented

    声明注解能够被javadoc等识别;

- @Target

    用来声明注解范围（枚举ElementType），ElementType可选值：

        TYPE：接口、类、枚举、注解
        FIELD：字段、枚举的常量
        METHOD：方法
        PARAMETER：方法参数
        CONSTRUCTOR：构造函数
        LOCAL_VARIABLE：局部变量
        ANNOTATION_TYPE：注解
        PACKAGE：包

- 注解的使用

    注解通过反射来获取和使用
   
- demo

```java
/**
 * @author danao
 * @version 1.0
 * @classname Self
 * @descriptionclass
 * 1.自定义注解
 * @Target(ElementType.METHOD)指明了我们的注解是作用在方法上的
 * @Retention(RetentionPolicy.RUNTIME)表示注解在程序运行时期也会存在，即注解信息也会加载到虚拟机VM中，所以可以通过反射来获取注解的相关信息：
 * RUNTIME表示注解在运行时能被获取到
 * @since 1.0
 */
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Self {

    public String id() default "001";

    public String key();

    public String value();

}
```

