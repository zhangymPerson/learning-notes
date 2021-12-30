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
        // list 增删改查
        // 构造一个list
        $list = array();
        // 增加
        array_push($list, "1", 1, 1.2, "hahah");
        print_r($list);

        // 删除
        unset($list[1]);
        print_r($list);

        // 判断是否存在
        if (in_array(1, $list)) {
            echo "1 存在" . PHP_EOL;
        } else {
            echo "1 不存在" . PHP_EOL;
        }

        echo "数组长度 = " . count($list) . PHP_EOL;
        echo "数组长度 = " . sizeof($list) . PHP_EOL;

        for ($i = 0; $i < count($list) + 1; $i++) {
            # code...
            if ($list[$i] == 1) {
                continue;
            } else {
                echo $list[$i] . PHP_EOL;
            }
        }

        echo "end ..." . PHP_EOL;
    }
}


$task = new Task;
$task->task();
