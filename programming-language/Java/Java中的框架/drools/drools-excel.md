# drools中使用决策表

### 决策表配置


- 全局配置部分

    RuleSet		：定义包名 
    Import		：指定导入的class，包括类方法 
    Variables	：指定全局变量 
    Notes		：输入任何内容 
    Functions	：本地方法
    | 关键字           | 说明                                                         | 是否必须                 |
    | ---------------- | ------------------------------------------------------------ | ------------------------ |
    | RuleSet          | 在单元格中和drl文件中的package一样                           | 必须                     |
    |                  |                                                              | 只能有一个               |
    |                  |                                                              | （如果为空则使用默认值） |
    | Sequential       | 右边的单元格是否可以为true或者false                          | 可选                     |
    |                  | true:代表从表格从上到下，依次执行                            |                          |
    |                  | false:乱序                                                   |                          |
    | import           | 要导入规则库中的类列表，逗号分隔                             | 可选                     |
    | functions        | 紧挨着的右边单元格，可以包含函数，可以用在规则片段中         | 可选                     |
    |                  | drools支持在drl文件中定义函数，并且写到规则中，不用硬代码改变，小心使用，与drl文件中一样。 |                          |
    |                  | 有返回值，无返回值两种，定义多个函数，逗号分隔写多个函数     |                          |
    | Variables        | 紧挨着的右边单元格，可以包含Global声明，格式：类型 变量名（多个变量，逗号分隔） | 可选                     |
    | Queries          | 紧挨着的右边单元格，可以包含drools支持的全局声明，格式：类型 查询名称 | 可选                     |
    | RuleTable        | 规则名称 格式：RuleTable 规则名称                            | 必填                     |

- RuleTable 部分

    CONDITION	：	指定单个规则的条件，条件不写的话默认就是== 
    ACTION		：		指定rule的结果 
    PRIORITY	：		指定rule的 salience属性 
    No-loop		：		指定rule的no-loop熟悉

    | 关键字           | 说明                                                         | 是否必须                 |
    |-|-|-|
    | condition        | 指明该列将被用于规则条件,condition代表条件相当于drl文件中的when | 每个规则表至少一个       |
    | action           | 指明该列将被用于推论，简单理解为结果，相遇drl的then，action与condition是平行的 | 每个规则表至少一个       |
    | priority         | 指明该列将被设置规则行的salience值，覆盖Sequential标志，如果在ruleSet设置覆盖了sequential值为true,则priority不起作用，如果squential设置为false或者不设置，则priority生效 | 可选                     |
    | duration         | 指明该列的值将被设置为该规则行的期限值，延迟作用和drl文件中一样 | 可选                     |
    | name             | 指明该列的值将被设置为从哪行产生的规则名字                   | 可选                     |
    | no-loop          | 指明这个规则不允许循环，为了这个选项正常运行，这里该单元格中必须是让该选项生效的一个值（true或者false），如果该单元格保持为空，那么这个选项将不会为该行设置 | 可选                     |
    | activation-group | 在这个列的单元格中的值，指定该规则属于特定的XOR/活动组，一个活动组意味着哪个明明组的规则只有一条会被引发 | 可选                     |
    | agenda-group     | 一组只有一个执行                                             | 可选                     |
    | ruleflow-group   | 指出该规则属于特定的规则流组                                 | 可选                     |

- demo

    当前目录下的 [user.xls](./user.xls) 文件