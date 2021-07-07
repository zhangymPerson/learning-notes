# php-debug

## 在执行的文件中添加如下函数

- debug 方式

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
