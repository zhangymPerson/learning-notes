package main

import (
	"io"
	"log"
	"os"
)

func main() {
	// 配置输出文件名和行号
	log.SetFlags(log.Ldate | log.Ltime | log.Lshortfile)

	// 配置输出到控制台和文件
	logFileOut, err := os.OpenFile("log.log", os.O_CREATE|os.O_APPEND|os.O_RDWR, os.ModePerm)
	if err != nil {
		log.Fatal("日志生成异常,异常信息如下:", err)
	}

	defer logFileOut.Close()

	multiWriter := io.MultiWriter(os.Stdout, logFileOut)
	log.SetOutput(multiWriter)

	// test
	info := "testlog"
	log.Printf("%+v\n", info)
}
