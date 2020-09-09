# linux 下关闭进程的脚本

- 脚本示例

  ```sh
  #!/bin/sh
  #$1为脚本后面的参数，可以直接指定
  NAME=$1
  echo "要杀掉的进程关键字:[$NAME]"
  ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
  echo "查到相关的进程号是[$ID]"
  for id in $ID
  do
  kill -9 $id
  echo "killed $id"
  done
  echo "相关进程全部kill"
  ```
