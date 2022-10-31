# 规则文件的编写

## 整体结构

### package package-name

- package

    是一系列rule或其他相关构件如imports, globals的容器。这个成员之间相互关联，一个package代表了一个命名空间，其中的每个rule的名字都是唯一的，package名字本身就是命名空间，与实际的文件和文件夹没有任何关系。常见的结构是，一个文件包含多个rule的文件就定义成一个包。

    **注意：包名需要和文件路径一致**

### import

java中的导入，规则中需要使用类的时候需要导入

### global

- 全局变量 可以通过代码注入

    代码调用规则时，可以注入
    ```java
    List list = new ArrayList();
    KieSession kieSession = kiebase.newKieSession();
    kieSession.setGlobal( "list", list );
    ```

    ```drl
    global java.util.List list;
    rule "test"
    when
        //规则
    then
        //操作全局变量
        list.add( "test" );
    end
    ```

### function

- 可以在drl规则文件中添加自定义函数;如下

    ```drl
    function String print(String str) {
        System.out.println(str);
    }

    rule "using a static function"
    when
        //规则
    then
        //调用自定义函数
        print("test");
    end
    ```
### querie

### rules

- 规则（Rule）组成

    一个简单的规则结构如下所示：

    ```java
    //单行注释
    /*
     多行注释
    */
    rule "name"
        attributes
        when
            //eval( true ) 表示永远为真的规则
            LHS
        then
            RHS
    end

    rule "<name>"
        <attribute> *
        when
            <conditional element> *
        then
            <action> *
    end
    ```
    通常，规则文件中是不需要标点符号的。即使是规则名“name”上的双引号也是可选的。attributes展示规则的执行方式，也是可选的。
    
    LHS是规则的条件部分，遵循一个固定的语法规则;

    RHS通常是一个可以本地执行的代码块。

>复杂的可以去网上找相关的资料阅读