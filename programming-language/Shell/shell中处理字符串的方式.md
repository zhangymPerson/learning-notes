# 字符串处理

[返回](./README.md)

## shell 中字符串的问题

- 1.定义变量时,key=value 中间不能有空格

- 2.定义函数是,参数不能有空格,有空格需要注意

  变量定义后 如果是用 `var='a b'` 定义的带空格的字符串 需要用 "${var}" "$var" 否则取到的字符串会丢失

  ```sh
  #!/usr/bin/bash

  #测试shell函数
  function doStrTest() {
      echo "第一个参数="$1,"第二个参数"$2
  }
  json='{"key":"value","two": "value" }'

  # json={"key":"value","two": "value" }
  echo json=$json

  # 第一个参数=one,第二个参数two
  doStrTest one two

  # 第一个参数=one one,第二个参数{"key":"value","two":
  # 字符串发生丢失情况
  doStrTest 'one one' $json

  # 第一个参数=one one,第二个参数$json
  doStrTest 'one one' '$json'

  # 第一个参数=one one,第二个参数${json}
  doStrTest 'one one' '${json}'

  # 第一个参数=one,第二个参数{"key":"value","two": "value" }
  doStrTest one "$json"

  # 第一个参数=one,第二个参数{"key":"value","two": "value" }
  doStrTest one "${json}"

  # 第一个参数=one one,第二个参数{" key ": " value "," two ": "value" }
  doStrTest 'one one' '{" key ": " value "," two ": "value" }'

  # 第一个参数=one one,第二个参数two two
  doStrTest "one one" 'two two'
  ```
