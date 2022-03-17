<?php

/**
 * 是否是NUll判断
 * 常用的  
 *  empty()  任何一个未初始化的变量、值为 0 或 false 或 空字符串"" 或 null的变量、空数组、没有任何属性的对象，都将判断为empty==true
 *  isset功能：判断变量是否被初始化
 */
function isNull($obj = null) {
    // 检测变量是否为"null"，同时变量的类型也必须是"null"
    if ($obj === null) {
        echo "obj === null => true" . PHP_EOL;
    }
    if (is_null($obj)) {
        echo "is_null(obj) => true" . PHP_EOL;;
    }
    if ($obj == null) {
        echo  "obj == null => true" . PHP_EOL;;
    }
    if (empty($obj)) {
        echo  "empty(obj) => true" . PHP_EOL;;
    }
    if (!isset($obj)) {
        echo  "!isset(obj) => true" . PHP_EOL;;
    }
    return false;
}

function testIsNull() {
    $objs = array(null, 0, 1, 1.1, '', '  ', ' s ', array(), array(1, 2, "2"));

    foreach ($objs as $item) {
        echo "===测试对象[$item]" . PHP_EOL;
        isNull($item);
        echo "=================" . PHP_EOL;
    }
}

/**
 * 获取/判断 类型 
 */
// function getType($obj = null) {
//     return gettype($obj);
// }

function testGetType() {
    $objs = array(null, 0, 1, 1.1, '', '  ', ' s ', array(), array(1, 2, "2"));

    foreach ($objs as $item) {
        $type = getType($item);
        echo "===测试对象[$item] type = [$type]" . PHP_EOL;
        echo "=================" . PHP_EOL;
    }
}



testIsNull();
testGetType();
