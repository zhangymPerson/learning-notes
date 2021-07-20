# php-debug

## 在执行的文件中添加调试信息输出

### var_dump()

- [官方文档](https://www.php.net/var_dump)

  ```php
  // 使用 var_dump()
  var_dump($varname)
  // 使用print
  print_r($var);
  // echo
  echo $var;
  //使用die
  //结束运行
  die;
  ```

- 函数代码

  ```php
  /**
  * 格式化打印 dump内容
  */
  function dump($vars, $label = '', $return = false)
  {
      if (ini_get('html_errors')) {
          $content = "<pre>\n";
          if ($label != '') {
              $content .= "<strong>{$label} :</strong>\n";
          }
          $content .= htmlspecialchars(print_r($vars, true));
          $content .= "\n</pre>\n";
      } else {
          $content = $label . " :\n" . print_r($vars, true);
      }
      if ($return) {
          return $content;
      }
      echo $content;
      return null;
  }
  ```

- 使用方法

  ```php
  //在变量的位置
  $varname="test";
  $this->dump($varname);
  ```

### var_export($obj,true)

- 打印对象参数

  当要查看一个对象中的变量时，使用。

### file_put_contents()

- php 打印错误到指定文件的办法

  官方文档：<https://www.php.net/manual/zh/function.file-put-contents.php>

- 代码

  ```php
  $arr = array('a' => 'a','b'=> 'b');
  file_put_contents("logname.log",json_encode($arr).PHP_EOL,FILE_APPEND);
  ```

### json_encode()

- 打印非字符串的对象时可使用

  ```json
  // 对象转字符串
  $jsonStr = json_encode($obj);
  ```
