<?php

/**
 * 任务
 */
class Task {

    public function __construct() {
    }

    public function arrayTest() {
        // 建数组
        $arr = array();
        $cars = array("Volvo", "BMW", "Toyota");
        // 长度
        echo count($cars);

        // 遍历
        for ($x = 0; $x < count($cars); $x++) {
            echo $cars[$x] . PHP_EOL;
        }

        // 增加
        array_push($cars, "1", 1, 1.2, "hahah");
        echo json_encode($cars) . PHP_EOL;

        // 删除
        unset($cars[0]);
        echo "删除后" . PHP_EOL;
        $cars = array_values($cars);
        echo json_encode($cars) . PHP_EOL;

        // 查 判断是否存在
        if (in_array(1, $cars)) {
            echo "1 存在" . PHP_EOL;
        } else {
            echo "1 不存在" . PHP_EOL;
        }
    }

    /**
     * 测试任务
     */
    public function task() {
        echo "start ..." . PHP_EOL;
        $this->arrayTest();
        echo "end ..." . PHP_EOL;
    }
}


$task = new Task;
$task->task();
