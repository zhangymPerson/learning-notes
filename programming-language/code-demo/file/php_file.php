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

    /**
     * 文件是否存在
     */
    public function isExist($fileName) {
        if (file_exists($fileName)) {
            // 获取文件路径的
            print realpath($fileName) . " is exists" . PHP_EOL;
            return true;
        } else {
            print "[$fileName] no exists" . PHP_EOL;
            return false;
        }
    }

    /**
     * 读文件
     */
    public function readFile($fileName) {
        # code...
        if (!file_exists($fileName)) {
            return;
        }
        $file = fopen($fileName, "r");
        $i = 0;
        while (!feof($file)) {
            $line_str = fgets($file);
            echo $i++ . " = [" .  trim($line_str) . "]" . PHP_EOL;
        }
        fclose($file);
    }

    /**
     * 写文件
     */
    public function writeFile($msg, $fileName) {
        // 按行写入
        file_put_contents($fileName, $msg . PHP_EOL, FILE_APPEND);
    }

    /**
     * 删除文件
     */
    public function removeFile($fileName) {
        if (!unlink($fileName)) {
            echo ("Error deleting [$fileName]" . PHP_EOL);
        } else {
            echo ("Deleted $fileName" . PHP_EOL);
        }
    }
}



$task = new Task;
$task->task();
$fileName = "php.log";
$task->writeFile("test,test", $fileName);
$task->writeFile("one,test", $fileName);
$task->writeFile("two,test", $fileName);
$task->writeFile("three,test", $fileName);
$task->writeFile("fore,test", $fileName);
$task->readFile($fileName);
// $task->removeFile($fileName);
