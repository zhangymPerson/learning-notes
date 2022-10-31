package main

import (
	"log"
	"os"
	"syscall"
)

func main() {
	dirName := "./test/test/test/test"
	createDir(dirName)
	IsDir(dirName)
	// RemoveDir(dirName)
	// IsDir(dirName)
}

// 目录是否存在
func IsDir(dirName string) bool {
	s, err := os.Stat(dirName)
	if err != nil {
		log.Printf("检查目录是否存在异常,异常信息如下:%s", err)
		return false
	}
	return s.IsDir()
}

// 创建目录
func createDir(dirName string) bool {
	if IsDir(dirName) {
		return true
	}
	// 创建目录权限不够的问题
	syscall.Umask(0)
	err := os.MkdirAll(dirName, 0755)
	if err != nil {
		log.Fatal("创建文件夹异常,异常信息如下:", dirName, err)
		return false
	}
	log.Printf("dirName is [%+v]\n", dirName)
	return true
}

// 删除目录
func RemoveDir(dirName string) bool {
	if !IsDir(dirName) {
		return true
	}
	err := os.RemoveAll(dirName)
	if err != nil {
		log.Fatal("删除文件异常,异常信息如下:", dirName, err)
		return false
	}
	return true
}
