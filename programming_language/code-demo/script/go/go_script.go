package main

import (
	"fmt"
	"log"
)

// 提示用户输入
func getArgs(info string) string {
	fmt.Println(info)
	res := ""
	fmt.Scanln(&res)
	return res
}

func useArgs()  {
    fmt.Println("script start")
	info := getArgs("请输入")
	fmt.Printf("输入的值是[%v]\n", info)
	fmt.Println("script stop") 
}

// go 脚本的读写输入
// go 单个脚本执行时 如果不创建 module 需要执行 go env -w GO111MODULE=auto
func main() {
    useArgs()
    useCommand()
}

func useCommand(){
    s := execCommand("ls -al")
    log.Printf("s is [%+v]\n", s)
}




//  execCommand 执行系统命令
func execCommand(command string) string {
	log.Printf("command is [%+v]\n", command)
	res := ""
    
	return res
}
