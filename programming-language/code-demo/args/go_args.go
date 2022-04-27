package main

import (
	"fmt"
	"os"
)

// main
// go run go-string.go
func main() {
	fmt.Println("start ...")
	// 获取参数
	s := os.Args
	fmt.Printf("参数个数%v\n", len(s))
	for _, ars := range s {
		fmt.Println(ars)
	}
	fmt.Println("end ...")
}
