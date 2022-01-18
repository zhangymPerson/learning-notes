<?php

/**
 * 任务
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
        $map = array();
        $map['name'] = '张三1';
        $map['name'] = '张三2';
        $map['age'] = 12;
        $map['a'] = 12.12;
        echo var_dump($map) . PHP_EOL;
        echo $map['a'] . PHP_EOL;
        echo $map["name"] . PHP_EOL;

        //遍历
        foreach ($map as $key => $value) {
            echo "{$key}==>{$value}" . PHP_EOL;
        }
    }
}


$task = new Task;
$task->task();
