package main

import (
	"fmt"
	"log"
)

// main
// go run go-string.go
func main() {
	fmt.Println("start ...")
	// test()
	GetSubArr()
	fmt.Println("end ...")
}

// GetSubArr 截取数组子串
func GetSubArr() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8}
	log.Printf("arr is [%+v]\n", arr)
	brr := arr[0:2]
	log.Printf("brr is [%+v]\n", brr)
	log.Printf("arr is [%+v]\n", arr)
	for i := 0; i < 10; i++ {
		GetSubArrNum(arr, i)
	}
}

//
func GetSubArrNum(arr []int, num int) {
	if len(arr) == 0 {
		return
	}
	if num == 0 {
		return
	}
	if len(arr) < num {
		return
	}
	mod := len(arr) / num
	if len(arr)%num != 0 {
		mod = mod + 1
	}
	var res = make([][]int, mod)
	for i := 0; i < mod; i++ {
		if ((i + 1) * num) < len(arr) {
			res[i] = arr[i*num : (i+1)*num]
		} else {
			res[i] = arr[i*num:]
		}
	}
	log.Printf("num = [%+v],mod = [%+v],res is [%+v]\n", num, mod, res)

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
