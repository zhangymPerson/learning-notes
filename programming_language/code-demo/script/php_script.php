<?php

/**
 * 脚本任务
 *
 * @param  void 
 * @return void
 * @throws null
 */
class Task {
    /**
     * 执行内容
     */
    public function run() {
        echo "script" . PHP_EOL;
    }
}

/**
 * 获取用户输入
 * msg : 提示语
 */
function getInput($msg) {
    fwrite(STDOUT, $msg . PHP_EOL);
    // get input
    $input = trim(fgets(STDIN));
    // echo "你输入的值为[$input]" . PHP_EOL;
    return $input;
}

$task = new Task();
$task->run();
$a = getInput("请输入参数");
error_log("[" . date('Y-m-d h:i:s', time()) . __CLASS__ . ":" . __METHOD__ . ":" . __LINE__ . "] ===> " . "[$a]");
