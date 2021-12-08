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
            print "[$fileName] exists" . PHP_EOL;
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
        if (!$this->isExist($fileName)) {
            return;
        }
        $file = fopen($fileName, "r");
        while (!feof($file)) {
            $line_str = fgets($file);
            echo $line_str . PHP_EOL;
        }
        fclose($file);
    }

    /**
     * 写文件
     */
    public function writeFile($msg, $fileName) {
        file_put_contents($fileName, $msg, FILE_APPEND);
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
$task->removeFile($fileName);
$task->readFile($fileName);
// $task->removeFile($fileName);
