#!/bin/bash

echo "start"

function moreTask {
    # array 使用空格分割，不是 , 分割
    arr=(20220215 20220216 20220217 20220218 20220219 20220220)
    echo "数组元素个数为: ${#arr[*]}"
    echo "数组元素个数为: ${#arr[@]}"

    # 遍历
    echo "-------FOR循环遍历输出数组--------"
    for i in ${arr[@]}; do
        #  shell 执行成功 命令执行结果是否成功判断
        # 执行命令
        echo $(date) $i
        if [ $? -eq 0 ]; then
            echo "command success"
        else
            echo "fail"
        fi
    done

    echo "-------::::WHILE循环输出 使用 let i++ 自增:::::---------"
    j=0
    while [ $j -lt ${#arr[@]} ]; do
        echo ${arr[$j]}
        let j++
    done
}

function main {
    echo "start"
    moreTask
    echo "end"
}

main $#

arr=(20200402 20200403 20200404 20200405 20200406)