package main

// 可以使用 go get github.com/huandu/xstrings 库处理字符串中的问题

import (
	"encoding/json"
	"fmt"
	"log"
	"reflect"
	"strconv"
	"strings"
	"time"
)

// main
// go run go-string.go
func main() {
	fmt.Println("start ...")
	// test()
	toByte()
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

// 字符串变 byte
func toByte() {
	// string与byte转化
	str := "hello word"
	bt := []byte(str)
	strs := string(bt)
	fmt.Println(str, bt, strs)
}

// StringVal 各种类型转string
func StringVal(value interface{}) string {
	var key string
	if value == nil {
		return "NULL"
	}
	fmt.Printf("value: %+v\n", value)
	fmt.Printf("type: %+v\n", reflect.TypeOf(value))
	switch value.(type) {
	case float64:
		ft := value.(float64)
		key = strconv.FormatFloat(ft, 'f', -1, 64)
	case float32:
		ft := value.(float32)
		key = strconv.FormatFloat(float64(ft), 'f', -1, 64)
	case int:
		it := value.(int)
		key = strconv.Itoa(it)
	case uint:
		it := value.(uint)
		key = strconv.Itoa(int(it))
	case int8:
		it := value.(int8)
		key = strconv.Itoa(int(it))
	case uint8:
		it := value.(uint8)
		key = strconv.Itoa(int(it))
	case int16:
		it := value.(int16)
		key = strconv.Itoa(int(it))
	case uint16:
		it := value.(uint16)
		key = strconv.Itoa(int(it))
	case int32:
		it := value.(int32)
		key = strconv.Itoa(int(it))
	case uint32:
		it := value.(uint32)
		key = strconv.Itoa(int(it))
	case int64:
		it := value.(int64)
		key = strconv.FormatInt(it, 10)
	case uint64:
		it := value.(uint64)
		key = strconv.FormatUint(it, 10)
	case string:
		key = value.(string)
	case []byte:
		key = string(value.([]byte))
	case time.Time:
		key = value.(time.Time).Format("2006-01-02 15:04:05")
	// 未知的type json兜底
	default:
		newValue, err := json.Marshal(value)
		if err != nil {
			log.Fatal("类型转json异常,异常信息如下:", err)
		}
		key = string(newValue)
	}
	return key
}
