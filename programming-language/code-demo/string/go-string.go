package main

import (
	"fmt"
	"strings"
)

// main
// go run go-string.go
func main() {
	fmt.Println("start ...")
	// test()
	strFormat()
	replace()
	fmt.Println("end ...")
}

func test() {
	c := join("a", "b", "c", "d")
	fmt.Println(c)
	strs := []string{"", "  ", "      ", "   aa c  d dd bb    ", " a b c ", "a b c", "aabbcc"}
	for _, v := range strs {
		res := trim(v)
		fmt.Printf("截取前 [%s],去空格后 [%s] \n", v, res)
	}

	for _, v := range strs {
		fmt.Printf("字符[%s]是否为空[%v] \n", v, isEmpty(v))
	}
}

// 字符串拼接
// join  字符串拼接
func join(arg string, args ...string) string {
	if len(args) > 0 {
		for _, v := range args {
			// 字符串拼接方式
			arg = arg + v
		}
	}
	return arg
}

// 字符串拼接替换
func strFormat() {
	//字符串拼接
	str := fmt.Sprintf("%s %s %s", "format", "string", "by fmt.Sprintf")
	print(str)
}

// 字符串去掉空格
func trim(str string) string {
	if str == "" {
		return str
	}
	// 只截取字符两边的空格
	res := strings.Trim(str, " ")
	return res
}

// 字符串为空判断
func isEmpty(str string) bool {
	if str == "" {
		return true
	}

	trim := strings.Trim(str, " ")
	return trim == ""
}

func replace() {
	str := "this is  danao \ntest\n doc"
	fmt.Println("-------- 原字符串 ----------")
	fmt.Println(str)
	// 去除空格
	str = strings.Replace(str, " ", "", -1)
	// 去除换行符
	str = strings.Replace(str, "\n", "", -1)
	fmt.Println(str)
}

// 字符串包含字符判断
