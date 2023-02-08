package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"
)

func init() {
	// 配置输出文件名和行号
	log.SetFlags(log.Ldate | log.Ltime | log.Lshortfile)
}

func main() {
	route()
	port := 9999
	log.Printf("创建一个 web 测试服务,端口:[%v]\n", port)
	log.Printf("curl http://127.0.0.1:%v \n", port)
	err := http.ListenAndServe(fmt.Sprint(":", port), nil)
	if err != nil {
		log.Printf("err is [%+v]\n", err)
	}
}

//  函数的作用是: 路由
func route() {
	http.HandleFunc("/", greet)
	http.HandleFunc("/test", getTest)
	http.HandleFunc("/post", handlePostJson)
}

func greet(w http.ResponseWriter, r *http.Request) {
	log.Printf("r is [%+v]\n", r)
	fmt.Fprintf(w, "%v => Hello World! \n", time.Now().Format("2006-01-02 15:04:05"))
}

func getTest(w http.ResponseWriter, r *http.Request) {
	log.Printf("请求的路由:/%v \n", r.RequestURI)
	fmt.Fprintf(w, "test response")
}

// handlePostJson 函数的作用是:测试 post json 请求
// curl -X 'POST'   'http://127.0.0.1:9999/post'   -H 'accept: */*'   -H 'Content-Type: application/json'   -d '{ "username": "username", "password": "password" }'
func handlePostJson(w http.ResponseWriter, r *http.Request) {
	// 根据请求body创建一个json解析器实例
	rc := r.Body
	decoder := json.NewDecoder(rc)
	// 用于存放参数key=value数据
	var params map[string]string
	// 解析参数 存入map
	decoder.Decode(&params)
	log.Println("日志输出======>", &params)
	log.Printf("POST json: username=%v, password=%v\n", params["username"], params["password"])
	res := make(map[string]interface{})
	res["code"] = 200
	res["msg"] = "success"
	res["data"] = "success"
	// 对象转json格式化 则替换 res
	jsonBytes, _ := json.MarshalIndent(res, "", "    ")
	log.Printf("json格式化如下:\n%+v\n", string(jsonBytes))
	fmt.Fprintf(w, string(jsonBytes))
}
