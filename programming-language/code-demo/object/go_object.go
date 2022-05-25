package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println("hello world")
	// 类型转换
	n := "100a"
	var num int
	num, err := strconv.Atoi(n)
	if err != nil {
		panic(err)
	}
	fmt.Println(num)
}
