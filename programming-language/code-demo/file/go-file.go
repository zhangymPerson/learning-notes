package main

import (
	"encoding/json"
	"fmt"
	"io/fs"
	"io/ioutil"
	"log"
	"os"

	"gopkg.in/yaml.v2"
)

// =============================读取配置====================================
// 读取json配置文件
func getJsonConf(fileName string) map[string]interface{} {
	res := make(map[string]interface{})
	// 读取文件
	b, err := ioutil.ReadFile(fileName)
	if err != nil {
		log.Fatalln(err)
	}
	// 转json
	err2 := json.Unmarshal(b, &res)
	if err2 != nil {
		log.Println("解析数据异常")
		log.Fatalln(err2)
	}
	return res
}

// 读取  properties 配置
func getPropertiesConf(fileName string) map[string]interface{} {
	res := make(map[string]interface{})
	// 读取文件
	_, err := ioutil.ReadFile(fileName)
	if err != nil {
		log.Fatalln(err)
	}
	return res
}

//  读取 yaml 配置
func getYamlConf(fileName string) map[string]interface{} {
	res := make(map[string]interface{})
	// 读取文件
	b, err := ioutil.ReadFile(fileName)
	if err != nil {
		log.Fatalln(err)
	}
	//yaml文件内容影射到结构体中
	err1 := yaml.Unmarshal(b, &res)
	if err1 != nil {
		log.Fatalln(err)
	}
	return res

}

// =============================读取配置====================================

// =================================================================
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

// 文件读写 测试
func test() {
	fileName := "go-test.log"
	WriteFile("write test", fileName)
	WriteFile("write test", fileName)
	WriteFile("write test", fileName)
	AppendFile("append test", fileName)
	AppendFile("append test", fileName)
	AppendFile("append test", fileName)
	ReadFile(fileName)
	RemoveFile(fileName)
}

// testConf 测试读取配置文件
func testConf() {
	fileName := "./conf/t-json.json"
	jsonConf := getJsonConf(fileName)
	log.Println(jsonConf)
	yamlConf := getYamlConf("./conf/t-yaml.yaml")
	log.Println(yamlConf)

}

// main
// go run go-string.go
func main() {
	fmt.Println("start ...")
	// test()
	testConf()
	fmt.Println("end ...")
}
