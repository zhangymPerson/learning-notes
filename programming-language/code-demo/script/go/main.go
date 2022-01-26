package main

import "fmt"

// 提示用户输入
func getArgs(info string) string {
    fmt.Println(info)
    res := ""
    fmt.Scanln(&res)
    return res
}

func main() {
    fmt.Println("script start")
    info := getArgs("请输入")
    fmt.Printf("输入的值是[%v]\n", info)
    fmt.Println("script stop")
}
