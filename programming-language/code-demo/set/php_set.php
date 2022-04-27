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
        echo "end ..." . PHP_EOL;
    }
}


$task = new Task;
$task->task();
