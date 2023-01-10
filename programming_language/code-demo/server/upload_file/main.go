package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"mime/multipart"
	"net/http"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"
)

// 启动配置
const fileKey string = "file"
const pathKey string = "path"
const upload_server_port int = 8888
const download_server_port int = 8889

var (
	host string
	ip   string
	err  error
)

func init() {
	host, err = os.Hostname()
	if err != nil {
		fmt.Println("获取主机名错误")
	}
	ip = getIp()
	// log.SetFlags(log.Ltime | log.Lshortfile)
}

// 文件上传服务脚本
// 搭建一个简单的文件服务脚本
func main() {
	// 指定服务时间，自动退出服务 指定总秒数
	secondNum := 3 * 10
	//新建计时器，一秒后触发
	timer := time.NewTimer(time.Second * time.Duration(secondNum))
	//新开启一个线程来处理触发后的事件
	go func() {
		//等触发时的信号
		<-timer.C
		log.Printf("本次服务[%v]s,已经结束\n", secondNum)
		os.Exit(0)
	}()
	go startDownloadServer(download_server_port)
	fmt.Println("文件上传服务")
	startServer(upload_server_port)
}

// 启动一个文件下载服务
func startDownloadServer(port int) {
	log.Println("启动文件下载服务")
	command := fmt.Sprintf("python3 -m http.server  %v", port)
	log.Println("[文件下载服务地址]")
	log.Printf("文件下载地址: http://%v:%d/", host, port)
	log.Printf("文件下载地址: http://%v:%d/", ip, port)
	GetCommandLinuxCon(command)
}

// 启动一个指定端口的服务
func startServer(port int) {
	http.HandleFunc("/", index)
	http.HandleFunc("/hi", Hi)
	http.HandleFunc("/upload", upload)
	http.HandleFunc("/upload/path", uploadPath)

	log.Println("[文件页面上传服务地址]")
	log.Printf("文件上传页面: http://%v:%d/", host, port)
	log.Printf("文件上传页面: http://%v:%d/", ip, port)
	err = http.ListenAndServe(":"+strconv.Itoa(port), nil)
	if err != nil {
		log.Fatalf("服务启动异常,异常信息:%v", err.Error())
	}
}

// hi 测试
func Hi(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "文件上传服务")
}

// 文件上传页面
func index(w http.ResponseWriter, r *http.Request) {
	pwd, err := os.Getwd()
	if err != nil {
		pwd = "/home/work"
	}
	link := fmt.Sprintf("http://%v:%d/", ip, download_server_port)
	linkDesc := "文件下载页跳转连接"
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
            <form enctype="multipart/form-data" action="/upload/path" method="post" target="submit">
                <label for="formFileMultiple" class="form-label">简易文件上传服务</label>
                <div class=" mb-3">
                    <input class="form-control" type="file" id="formFileMultiple" name="%v" multiple>
                </div>
                <div class="input-group mb-3">
                    <span class="input-group-text" id="basic-addon1">保存的文件夹位置</span>
                    <input type="text" class="form-control" name="%v" placeholder="%v" value="%v"
                        aria-describedby="basic-addon1">
                </div>
                <button type="submit" class="btn btn-primary">提交文件</button>
                <button type="reset" class="btn btn-primary">取消</button>
            </form>
        </div>
        <div class="container">
     		<div class=" mb-3">
				%v 
				<a href="%v">
					<button type="button" class="btn btn-primary">点击跳转到下载页面</button>
				<a>
            </div>
        </div>
        <div class="container">
            <iframe src="" frameborder="1" name="submit" height="30%%" width="100%%" >
        </iframe>
    </div>
    </body>
    
    </html>
    `, fileKey, pathKey, pwd, pwd, linkDesc, link)
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
		fmt.Println(err.Error())
		fmt.Fprintf(w, "获取文件失败,异常信息:%s", err)
		return
	}
	msg := saveFile("", handler.Filename, file)
	fmt.Fprintln(w, msg)
}

// 上传文件指定保存路径
func uploadPath(w http.ResponseWriter, r *http.Request) {
	r.ParseMultipartForm(32 << 20)
	errRes := GetError("非Post请求")
	// 判断是否是post请求
	if r.Method != "POST" {
		fmt.Fprintln(w, errRes.ToJson())
		return
	}
	// 是否有path
	path := r.FormValue(pathKey)
	fmt.Printf("path = [%s]", path)
	if path == "" {
		upload(w, r)
		return
	}
	file, handler, err := r.FormFile(fileKey)
	if err != nil {
		fmt.Fprintf(w, "获取文件失败,异常信息:%s", err)
		return
	}
	filename := handler.Filename
	msg := saveFile(path, filename, file)
	fmt.Fprintln(w, msg)
}

// 保存文件
func saveFile(path string, filename string, file multipart.File) string {
	defer file.Close()
	name := fmt.Sprintf("%s/%s", path, filename)
	if path == "" {
		name = filename
	}
	fmt.Printf("name = [%s]\n", name)
	var f *os.File
	// 文件存在时,则重命名 并备份
	if _, err := os.Stat(name); !os.IsNotExist(err) {
		log.Printf("文件[%v]已经存在", name)
		oldFile, err := os.Open(name)
		if err != nil {
			log.Println("备份文件失败,失败信息", err.Error())
		}
		defer oldFile.Close()
		filename = strconv.FormatInt(time.Now().Unix(), 10) + "_" + filename
		backName := fmt.Sprintf("%s/%s", path, filename)
		backFile, _ := os.OpenFile(backName, os.O_WRONLY|os.O_CREATE, 0666)
		defer backFile.Close()
		// 备份旧文件
		io.Copy(backFile, oldFile)
	}
	f, err := os.OpenFile(name, os.O_WRONLY|os.O_CREATE, 0666)
	if err != nil {
		log.Printf("请检查路径 [%s] 是否存在,错误信息:%s", path, err)
		errInfo := GetError(fmt.Sprintf("无法创建 [%s] \n错误信息:%s", name, err))
		return errInfo.ToJson()
	}
	defer f.Close()
	_, err1 := io.Copy(f, file)
	if err1 != nil {
		log.Println("保存异常,异常信息", err1)
		errInfo := GetError(fmt.Sprintf("保存文件异常,异常信息:%s", err1))
		return errInfo.ToJson()
	}
	log.Printf("保存文件[%v]到当前文件夹成功", f.Name())
	msg := GetSuccessResult(fmt.Sprintf("保存文件[%v]到[%v]成功", filename, path))
	return msg.ToJson()
}

//Result 统一错误返回格式
type Result struct {
	Code   int         `json:"code"`
	Msg    string      `json:"msg"`
	Result interface{} `json:"result"`
}

//ToJson 错误返回json字符串
func (r *Result) ToJson() string {
	var jsonStr []byte
	var err error
	if r != nil {
		jsonStr, err = json.Marshal(r)
		if err != nil {
			log.Fatal("r对象转json异常", err.Error())
		}
	} else {
		errR := Result{
			Code:   500,
			Msg:    "r不能为null",
			Result: "fail",
		}
		jsonStr, err = json.Marshal(errR)
		if err != nil {
			log.Fatal("errR转json异常", err.Error())
			return "r is null and error not change json"
		}
	}
	// 格式化 json
	var out bytes.Buffer
	err = json.Indent(&out, jsonStr, "", "  ")
	if err != nil {
		log.Fatalln(err)
	}
	return out.String()
}

// 成功返回信息
func GetSuccessResult(data interface{}) *Result {
	return &Result{
		Code:   200,
		Msg:    "success",
		Result: data,
	}
}

// 错误返回信息
func GetError(data interface{}) *Result {
	return &Result{
		Code:   500,
		Msg:    "fail",
		Result: data,
	}
}

func GetCommandLinuxCon(commandLinux string) []byte {
	//需要执行命令： commandLinux
	cmd := exec.Command("/bin/bash", "-c", commandLinux)
	// 获取输入
	output, err := cmd.StdoutPipe()
	if err != nil {
		fmt.Println("无法获取命令的标准输出管道", err.Error())
		return nil
	}
	// 执行Linux命令
	if err := cmd.Start(); err != nil {
		fmt.Println("Linux命令执行失败，请检查命令输入是否有误", err.Error())
		return nil
	}
	// 读取输出
	bytes, err := ioutil.ReadAll(output)
	if err != nil {
		fmt.Println("打印异常，请检查")
		return nil
	}
	if err := cmd.Wait(); err != nil {
		fmt.Println("Wait", err.Error())
		return nil
	}
	return bytes
}

// 字符串为空判断
func isEmpty(str string) bool {
	if str == "" {
		return true
	}

	trim := strings.Trim(str, " ")
	return trim == ""
}

// getIp
func getIp() string {
	command := "hostname -i"
	byteStr := GetCommandLinuxCon(command)
	ipStr := string(byteStr)
	if isEmpty(ipStr) {
		ipStr = "127.0.0.1"
	}
	ipStr = strings.Replace(ipStr, "\n", "", -1)
	return ipStr
}
