package main

import (
	"fmt"
)

// 创建 map
func create() {
	// 定义 声明一个
	var mapA map[string]string
	// 构造
	mapA = make(map[string]string)
	mapA["a"] = "aa"
	fmt.Printf("%v \n", mapA)

	mapB := make(map[string]interface{})
	mapB["a"] = 1
	mapB["a"] = 2
	mapB["b"] = "good"
	mapB["c"] = 12.2
	mapB["d"] = true
	mapB["e"] = 12.2
	fmt.Printf("%v \n", mapB)

	mapC := map[string]string{"France": "Paris", "Italy": "Rome", "Japan": "Tokyo", "India": "New delhi"}
	mapC["Italy"] = "test"
	mapC["hello"] = "word"
	// 删除
	delete(mapC, "")
	delete(mapC, "hello")
	delete(mapC, "hello")
	delete(mapC, "hello")
	fmt.Printf("%v \n", mapC)

	// 遍历
	for k, v := range mapC {
		fmt.Printf("key = %v value = %v\n", k, v)
	}

}

func test() {
	create()
}

// main
// go run go-string.go
func main() {
	fmt.Println("start ...")
	test()
	fmt.Println("end ...")
}
