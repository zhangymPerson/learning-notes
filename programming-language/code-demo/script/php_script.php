<?php

/**
 * 执行任务
 */
class Task {
    /**
     * 执行内容
     */
    public function run() {
        echo "script";
        $a = $this->getInput("请输入 a 的值");
        echo $a . PHP_EOL;
        $b = $this->getInput("请输入 b 的值");
        echo $b . PHP_EOL;
    }

    /**
     * 获取用户输入
     * msg : 提示语
     */
    public function getInput($msg) {
        fwrite(STDOUT, $msg . PHP_EOL);
        // get input
        $input = trim(fgets(STDIN));
        echo "你输入的值为[$input]" . PHP_EOL;
        return $input;
    }
}

$task = new Task();
$task->run();
