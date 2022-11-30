package main

import (
	"fmt"
	"log"
	"os"
)

// main
// go run go_args.go
func main() {
	fmt.Println("start ...")
	// 获取参数
	s := os.Args
	fmt.Printf("参数个数%v\n", len(s))
	for _, ars := range s {
		fmt.Println(ars)
	}
	input := GetUserInput("测试用户输入")
	log.Printf("input is [%+v]\n", input)
	fmt.Println("end ...")
}

// GetUserInput
// info 用户输入提醒词
// res 返回用户输入内容
func GetUserInput(info string) (res string) {
	log.Println(info)
	fmt.Scanln(&res)
	return
}
