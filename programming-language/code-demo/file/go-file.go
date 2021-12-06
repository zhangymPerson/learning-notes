package main

import (
	"fmt"
	"io/fs"
	"io/ioutil"
	"log"
	"os"
)

/**
 * 判断文件是否存在
 * 存在返回 true 不存在返回false
 */
func IsExist(filename string) bool {
	var exist = true
	if _, err := os.Stat(filename); os.IsNotExist(err) {
		exist = false
	}
	return exist
}

// 读文件
func ReadFile(fileName string) {
	content, err := ioutil.ReadFile(fileName)
	if err != nil {
		log.Fatal(err.Error())
	}
	// 字节转数组
	fmt.Println(string(content))
}

// 写文件
func WriteFile(msg string, fileName string) {
	if !IsExist(fileName) {
		os.Create(fileName)
	}
	// 不能追加
	err := ioutil.WriteFile(fileName, []byte(msg), fs.ModeAppend)
	if err != nil {
		log.Fatal(err.Error())
	}
}

// 追加写入
func AppendFile(msg string, fileName string) {
	if !IsExist(fileName) {
		os.Create(fileName)
	}
	f, err := os.OpenFile(fileName, os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	_, err2 := f.WriteString(msg)
	if err2 != nil {
		log.Fatal(err2.Error())
	}
}

// 删除文件
func RemoveFile(fileName string) {
	err := os.Remove(fileName)
	if err != nil {
		fmt.Println(err.Error())
	} else {
		fmt.Printf("删除[%v]成功 \n", fileName)
	}
}

// main
// go run go-string.go
func main() {
	fmt.Println("start ...")
	fileName := "go-test.log"
	WriteFile("write test", fileName)
	WriteFile("write test", fileName)
	WriteFile("write test", fileName)
	AppendFile("append test", fileName)
	AppendFile("append test", fileName)
	AppendFile("append test", fileName)
	ReadFile(fileName)
	RemoveFile(fileName)
	fmt.Println("end ...")
}
