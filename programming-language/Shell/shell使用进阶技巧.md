# shell 编写注意事项和技巧

[返回](./README.md)

## 脚本安全

- 脚本开始就需要定义

  ```sh
  #下面含义一样;当你使用未初始化的变量时，让bash自动退出。
  set -u
  set -o nounset

  #下面含义一样;bash一但有任何一个语句返回非真的值，则退出bash。
  set -e
  set -o errexit
  ```

- 函数的使用

  在 bash 里你可以定义函数，它们就跟其它命令一样，可以随意的使用；它们能让你的脚本更具可读性：

  脚本中多使用函数，增加程序可读性

  尽可能的把你的 bash 代码移入到函数里，仅把全局变量、常量和对“main”调用的语句放在最外层。

- 变量注解

  Bash 里可以对变量进行有限的注解。最重要的两个注解是：

  local(函数内部变量)

  ```sh
  function func()                             #定义函数func1
  {
      local hello="var2"                    #定义内部变量hello
      echo $hello

  }
  ```

  - readonly(只读变量)

    ```sh
    #!/bin/bash
    myUrl="http://www.w3cschool.cc"
    # 只读变量不能修改
    readonly myUrl

    ```

  - 删除变量

    ```sh
    #删除变量。不能删除只读变量
    unset variable_name
    ```

  - 注意

    **尽量对你 bash 脚本里的所有变量使用 local 或 readonly 进行注解。**

- 用$()代替反单引号(`)

  $() 进行命令调用 不使用 ``

  反单引号很难看，在有些字体里跟正单引号很相似。$()能够内嵌使用，而且避免了转义符的麻烦。

  ```sh
  # both commands below print out: A-B-C-D
  echo "A-`echo B-\`echo C-\\\`echo D\\\`\``"
  echo "A-$(echo B-$(echo C-$(echo D)))"
  ```

- 用[[]] (双层中括号)替代[]

  使用[[]]能避免像异常的文件扩展名之类的问题，而且能带来很多语法上的改进，而且还增加了很多新功能：

  | 操作符       | 功能说明                                                   |
  | ------------ | ---------------------------------------------------------- |
  | &#124;&#124; | 逻辑 or(仅双中括号里使用)                                  |
  | &&           | 逻辑 and(仅双中括号里使用)                                 |
  | <            | 字符串比较(双中括号里不需要转移)                           |
  | -lt          | 数字比较                                                   |
  | =            | 字符串相等                                                 |
  | ==           | 以 Globbing 方式进行字符串比较(仅双中括号里使用，参考下文) |
  | =~           | 用正则表达式进行字符串比较(仅双中括号里使用，参考下文)     |
  | -n           | 非空字符串                                                 |
  | -z           | 空字符串                                                   |
  | -eq          | 数字相等                                                   |
  | -ne          | 数字不等                                                   |

  ```sh

  单中括号：

  [ "${name}" \> "a" -o ${name} \< "m" ]

  双中括号

  [[ "${name}" > "a" && "${name}" < "m"  ]]
  ```

  - 正则表达式/Globbing

    shell 字符串比较

    使用双中括号带来的好处用下面几个例子最能表现：

    ```sh
    t="abc123"
    [[ "$t" == abc* ]]
    # true (globbing比较)
    [[ "$t" == "abc*" ]]
    # false (字面比较)
    [[ "$t" =~ [abc]+[123]+ ]]
    # true (正则表达式比较)
    [[ "$t" =~ "abc*" ]]
    # false (字面比较)
    ```

- 避免使用临时文件

  有些命令需要以文件名为参数，这样一来就不能使用管道。这个时候?<()?就显出用处了，它可以接受一个命令，并把它转换成可以当成文件名之类的什么东西：

  ```sh
  # 下载并比较两个网页
  diff <(wget -O - url1) <(wget -O - url2)
  ```

  还有一个非常有用处的是”here documents”，它能让你在标准输入上输入多行字符串。下面的’MARKER’可以替换成任何字词。

  ```sh
  #任何字词都可以当作分界符
  command  << MARKER
  ...
  ${var}
  $(cmd)
  ...
  MARKER
  ```

  如果文本里没有内嵌变量替换操作，你可以把第一个 MARKER 用单引号包起来：

  ```sh
  command << 'MARKER'
  ...
  no substitution is happening here.
  $ (dollar sign) is passed through verbatim.
  ...
  MARKER
  ```

- 字符串操作

  Bash 里有各种各样操作字符串的方式，很多都是不可取的。

  基本用户

  ```sh
  f="path1/path2/file.ext"
  len="${#f}" # = 20 (字符串长度)
  # 切片操作: ${<var>:<start>} or ${<var>:<start>:<length>}
  slice1="${f:6}"
  # = "path2/file.ext"
  slice2="${f:6:5}"
  # = "path2"
  slice3="${f: -8}"
  # = "file.ext"(注意："-"前有空格)
  pos=6
  len=5
  slice4="${f:${pos}:${len}}"
  # = "path2"
  ```

- 替换操作(使用 globbing)
  ```sh
  f="path1/path2/file.ext"
  single_subst="${f/path?/x}"
  # = "x/path2/file.ext"
  global_subst="${f//path?/x}"
  # = "x/x/file.ext"
  # 字符串拆分
  readonly DIR_SEP="/"
  array=(${f//${DIR_SEP}/ })
  second_dir="${arrray[1]}"
  # = path2
  ```
- 删除头部或尾部(使用 globbing)
  ```sh
  f="path1/path2/file.ext"
  # 删除字符串头部
  extension="${f#*.}"  # = "ext"
  # 以贪婪匹配方式删除字符串头部
  filename="${f##*/}"  # = "file.ext"
  # 删除字符串尾部
  dirname="${f%/*}"
  # = "path1/path2"
  # 以贪婪匹配方式删除字符串尾部
  root="${f%%/*}"
  # = "path1"
  ```
- 内置变量

  | 变量 | 说明                                                |
  | ---- | --------------------------------------------------- |
  | $0   | 脚本名称                                            |
  | $n   | 传给脚本/函数的第 n 个参数                          |
  | $$   | 脚本的 PID                                          |
  | $!   | 上一个被执行的命令的 PID(后台运行的进程)            |
  | $?   | 上一个命令的退出状态(管道命令使用${PIPESTATUS})     |
  | $#   | 传递给脚本/函数的参数个数                           |
  | $@   | 传递给脚本/函数的所有参数(识别每个参数)             |
  | $\*  | 传递给脚本/函数的所有参数(把所有参数当成一个字符串) |

  - 提示

    使用$\*很少是正确的选择。

    $@能够处理空格参数，而且参数间的空格也能正确的处理。

    使用$@时应该用双引号括起来，像”$@”这样。

- 调试

  对脚本进行语法检查：

  ```sh
  bash -n myscript.sh
  ```

  跟踪脚本里每个命令的执行：

  ```sh
  bash -v myscripts.sh
  ```

  跟踪脚本里每个命令的执行并附加扩充信息：

  ```sh
  bash -x myscript.sh
  ```

  你可以在脚本头部使用 set -o verbose 和 set -o xtrace 来永久指定-v 和-o。

  当在远程机器上执行脚本时，这样做非常有用，用它来输出远程信息。

- 什么时候不应该使用 bash 脚本

  你的脚本太长，多达几百行

  你需要比数组更复杂的数据结构

  出现了复杂的转义问题

  有太多的字符串操作

  不太需要调用其它程序和跟其它程序管道交互

  担心性能

  这个时候，你应该考虑一种脚本语言，比如 Python 或 Ruby。
