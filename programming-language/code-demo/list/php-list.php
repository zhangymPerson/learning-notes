<?php

/**
 * 任务
 */
class Task {

    public function __construct() {
    }

    /**
     * list 测试
     */
    public function listTest() {
        // list 增删改查
        // 构造一个list
        $list = array();
        // 增加
        array_push($list, "1", 1, 1.2, "hahah");
        print_r($list);

        // 删除
        unset($list[1]);
        print_r($list);

        // 查 判断是否存在
        if (in_array(1, $list)) {
            echo "1 存在" . PHP_EOL;
        } else {
            echo "1 不存在" . PHP_EOL;
        }

        // 反转
        print_r($list);
        $newList = array_reverse($list);

        print_r($newList);

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
    }

    /**
     * json/list 互转
     */
    public function jsonAndList() {
        // $arrJsonStr = "[\"测试\",\"query\",\"haha\",\"nihao\",\"Json\",\"好的\",\"\",\"12\",\"false\",\"1.0\",\"\t\",\"EOL\",\"\",\"\"]";
        // php不能解析带 \t 的json串
        $arrJsonStr = "[\"测试\",\"query\",\"haha\",\"nihao\",\"Json\",\"好的\",\"\",\"12\",\"false\",\"1.0\",\"EOL\",\"\",\"\"]";
        echo $arrJsonStr . PHP_EOL;
        // josn 转 list
        $arr = json_decode($arrJsonStr);
        echo gettype($arr) . PHP_EOL;
        foreach ($arr as $item) {
            echo $item . PHP_EOL;
        }

        // list转json 中文乱码问题
        $arrStr = json_encode($arr, JSON_UNESCAPED_UNICODE);
        echo $arrStr . PHP_EOL;
    }

    public function listMerge() {
        $arr = [1, 2, 3];
        $brr = ["hello", "word"];
        $crr = array_merge($arr, $brr);
        echo "arr = " . count($arr) . PHP_EOL;
        echo "brr = " . count($brr) . PHP_EOL;
        echo "crr = " . count($crr) . PHP_EOL;
    }

    /**
     * 测试任务
     */
    public function task() {
        echo "start ..." . PHP_EOL;
        // $this->listTest();
        $this->jsonAndList();
        $this->listMerge();
        echo "end ..." . PHP_EOL;
    }
}


$task = new Task;
$task->task();
