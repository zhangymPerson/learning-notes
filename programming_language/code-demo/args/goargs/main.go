package main

import (
	"flag"
	"fmt"
)

// flag包实现了命令行参数的解析。
func main() {

	/*
	   定义变量接收控制台参数
	*/

	// 用户
	var username string
	// 密码
	var password string
	// 主机名
	var host string
	// 端口号
	var port int

	// StringVar用指定的名称、控制台参数项目、默认值、使用信息注册一个string类型flag，并将flag的值保存到p指向的变量
	flag.StringVar(&username, "u", "", "用户名,默认为空")
	flag.StringVar(&password, "p", "", "密码,默认为空")
	flag.StringVar(&host, "h", "127.0.0.1", "主机名,默认 127.0.0.1")
	flag.IntVar(&port, "P", 3306, "端口号,默认为空")

	// 从arguments中解析注册的flag。必须在所有flag都注册好而未访问其值时执行。未注册却使用flag -help时，会返回ErrHelp。
	flag.Parse()

	// 打印
	fmt.Printf("username=%v password=%v host=%v port=%v", username, password, host, port)
}
