package main

import "fmt"

// main
// go run go-string.go
func main() {
	fmt.Println("start ...")
	test()
	fmt.Println("end ...")
}

func test() {
	// 定义数组 三种方式
	var arr [3]int
	var arr1 = [4]int{1, 2, 3, 4}
	arr2 := [...]int{123, 234, 232, 242, 42, 42}
	fmt.Printf("arr = [%v] arr len = [%v] \n", arr, len(arr))
	fmt.Printf("arr1 = [%v] arr1 len = [%v] \n", arr1, len(arr1))
	fmt.Printf("arr2 = [%v] arr2 len = [%v] \n", arr2, len(arr2))
	num := arr2[3]
	fmt.Println(num)
}
