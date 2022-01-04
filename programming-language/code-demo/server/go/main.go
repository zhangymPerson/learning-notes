package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"
)

// 启动配置
const fileKey = "file"
const serverPort = 8889

// 文件上传服务脚本
// 搭建一个简单的文件服务脚本
func main() {
	// 提供一个文件上传服务脚本，方便直接上传文件，不用走跳板代理
	fmt.Println("文件上传服务")
	args := getArgs()
	port := ":" + args["port"]
	startServer(port)
}

// getArgs 获取参数
func getArgs() map[string]string {
	res := make(map[string]string)
	res["port"] = strconv.Itoa(serverPort)
	return res
}

// getIp
func getIp() string {
	cmd := exec.Command("bash", "-c", "hostname -i")
	b, err := cmd.Output()
	if err != nil {
		fmt.Println("获取ip错误，错误信息", err)
		return "127.0.0.1"
	}
	return string(b)

}

// 启动一个指定端口的服务
func startServer(port string) {
	http.HandleFunc("/", index)
	http.HandleFunc("/hi", Hi)
	http.HandleFunc("/upload", upload)
	log.Println("请求网址如下:")
	host, err := os.Hostname()
	if err != nil {
		fmt.Println("获取主机名错误")
	}
	log.Printf("http://%v%v/", host, port)
	ip := strings.Replace(getIp(), "\n", "", -1)
	log.Printf("http://%v%v/", ip, port)
	command := fmt.Sprintf(`curl --location --request POST '%v%v/upload' --form '%v=@"%v"'
	`, host, port, fileKey, "/home/work/filename")
	log.Printf("命令行工具\n%v", command)
	err1 := http.ListenAndServe(port, nil)
	if err1 != nil {
		log.Fatalf("服务启动异常,异常信息:%v", err.Error())
	}
	log.Println("服务启动成功!")
}

// hi 测试
func Hi(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "文件上传服务")
}

// 文件上传页面
func index(w http.ResponseWriter, r *http.Request) {
	tpl := fmt.Sprintf(`
	<html>

	<head>
		<title>上传文件</title>
		<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
		<!-- CSS only -->
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
		<!-- JavaScript Bundle with Popper -->
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
	</head>
	
	<body>
		<div class="container">
			<form enctype="multipart/form-data" action="/upload" method="post">
				<label for="formFileMultiple" class="form-label">简易文件上传服务</label>
				<div class=" mb-3">
					<input class="form-control" type="file" id="formFileMultiple" name="%v" multiple>
				</div>
				<button type="submit" class="btn btn-primary">提交文件</button>
				<button type="reset" class="btn btn-primary">取消</button>
			</form>
		</div>
	</body>
	
	</html>
	`, fileKey)
	w.Write([]byte(tpl))
}

// 上传文件处理逻辑
func upload(w http.ResponseWriter, r *http.Request) {
	r.ParseMultipartForm(32 << 20)
	errRes := GetError("非Post请求")
	// 判断是否是post请求
	if r.Method != "POST" {
		fmt.Fprintln(w, errRes.ToJson())
		return
	}
	file, handler, err := r.FormFile(fileKey)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()
	name := handler.Filename
	var f *os.File
	// 多次上传文件覆盖的问题
	// 多次时，使用 时间戳 + _ 作为前缀 创建新文件保存
	if _, err := os.Stat(name); os.IsNotExist(err) {
		f, _ = os.OpenFile(name, os.O_WRONLY|os.O_CREATE, 0666)
	} else {
		log.Printf("文件[%v]已经存在", name)
		name = strconv.FormatInt(time.Now().Unix(), 10) + "_" + name
		f, _ = os.OpenFile(name, os.O_WRONLY|os.O_CREATE, 0666)
	}
	if err != nil {
		log.Printf("保存文件[%v]失败", f.Name())
		fmt.Println(err)
		return
	}
	defer f.Close()
	_, err1 := io.Copy(f, file)
	if err1 != nil {
		log.Println("保存异常，异常信息", err1)
		return
	}
	log.Printf("保存文件[%v]到当前文件夹成功", f.Name())
	msg := GetSuccessResult("保存成功")
	fmt.Fprintln(w, msg.ToJson())
}

//Result 统一错误返回格式
type Result struct {
	Code   int         `json:"code"`
	Msg    string      `json:"msg"`
	Result interface{} `json:"result"`
}

//ToJson 错误返回json字符串
func (r *Result) ToJson() string {
	if r != nil {
		json, err := json.Marshal(r)
		if err != nil {
			log.Fatal("r对象转json异常", err.Error())
		}
		return string(json)
	} else {
		errR := Result{
			Code:   500,
			Msg:    "r不能为null",
			Result: "fail",
		}
		json, err := json.Marshal(errR)
		if err != nil {
			log.Fatal("errR转json异常", err.Error())
			return "r is null and error not change json"
		}
		return string(json)
	}
}

// 成功返回信息
func GetSuccessResult(data interface{}) Result {
	return Result{
		Code:   200,
		Msg:    "success",
		Result: data,
	}
}

// 错误返回信息
func GetError(data interface{}) Result {
	return Result{
		Code:   500,
		Msg:    "fail",
		Result: data,
	}
}
