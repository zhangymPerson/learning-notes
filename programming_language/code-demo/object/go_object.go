package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println("hello world")
	// 类型转换
	n := "100"
	var num int
	// 字符转int
	num, err := strconv.Atoi(n)
	if err != nil {
		panic(err)
	}
	fmt.Println(num)

	// int 转字符
	i := 100
	str := strconv.Itoa(i)
	fmt.Printf("str: %+v\n", str)

	// interface 转 字符串
	var obj interface{} = "aaa"
	s := obj.(string)
	fmt.Printf("s: %+v\n", s)
}
