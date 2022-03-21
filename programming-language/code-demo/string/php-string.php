<?php

/**
 * 判断是否是空字符串
 */
function isEmpty($str = null) {
    if (isString($str)) {
        return false;
    }
    if (empty($str)) {
        return true;
    }
    return false;
}

function testIsEmpty() {
    $objs = array(null, 0, 1, 1.1, '', '  ', ' s ', array(), array(1, 2, "2"));
    foreach ($objs as $item) {
        $res =  isEmpty($item);
        echo "===测试对象[$item] isEmpty is [$res]" . PHP_EOL;
        echo "=================" . PHP_EOL;
    }
}

/**
 * 判断一个变量是否是字符串
 */
function isString($obj = null) {
    $type = getType($obj);
    // echo $type;
    return $type === 'string';
}

function testIsString() {
    $objs = array(null, 0, 1, 1.1, '', '  ', ' s ', array(), array(1, 2, "2"));
    foreach ($objs as $item) {
        $res =  isString($item);
        echo "===测试对象[$item] isString is [$res]" . PHP_EOL;
        echo "=================" . PHP_EOL;
    }
}

/**
 * 去掉字符串空格
 * php原生支持
 */
function trimStr($str) {
    return trim($str);
}

function testTrim() {
    // 测试对象
    $objs = array(null, 0, -1, 1.1, false, "", "  ", "a b c ", " aa cc dd ");
    foreach ($objs as $item) {
        $nStr = trimStr($item);
        echo "[$item] trim 后 [$nStr]" . PHP_EOL;
    }
}

/**
 * split 字符串切割
 */
function split($pattern, $str) {
    $arr = explode($pattern, $str);
    echo  "[$str] 按照 [$pattern] 切割后 " . json_encode($arr) . PHP_EOL;
}

function testSplit() {
    split("\t", "aa	bb	cc");
    split(".", "1.3.3.3.3");
}
// testIsEmpty();
// testIsString();
// testTrim();
testSplit();
