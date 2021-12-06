<?php

/**
 * 字符串函数
 * https://www.runoob.com/php/php-ref-string.html
 */
class Task {

    public function __construct() {
    }

    /**
     * 测试任务
     */
    public function task() {
        echo "start ..." . PHP_EOL;
        $this->test();
        echo "end ..." . PHP_EOL;
    }

    public function test() {
        //拼接测试
        $res =  $this->join("a", "b");
        echo $res . PHP_EOL;
        print($res . PHP_EOL);
        //去掉空格
        $arr = array("", "  ", "      ", "   aa c  d dd bb    ", " a b c ", "a b c", "aabbcc");
        foreach ($arr as $item) {
            $res = $this->trim($item);
            echo "[$item] => [$res]" . PHP_EOL;
        }
    }

    // 字符串拼接
    public function join($str, $str1) {
        return $str . $str1;
    }
    // 字符串去掉空格
    public function trim($str) {
        return trim($str);
    }
    // 字符串为空判断
    // 字符串包含字符判断
}


$task = new Task;
$task->task();
