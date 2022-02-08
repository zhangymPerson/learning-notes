package main

import (
    "encoding/json"
    "fmt"
    "io"
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
const fileKey = "file"
const pathKey = "path"
const serverPort = 8889

// 文件上传服务脚本
// 搭建一个简单的文件服务脚本
func main() {
    // 指定服务时间，自动退出服务
    secondNum := 10 * 60
    //新建计时器，一秒后触发
    timer := time.NewTimer(time.Second * time.Duration(secondNum))
    //新开启一个线程来处理触发后的事件
    go func() {
        //等触发时的信号
        <-timer.C
        log.Printf("本次服务[%v]s,已经结束\n", secondNum)
        os.Exit(0)
    }()

    // 提供一个文件上传服务脚本，方便直接上传文件，不用走跳板代理
    fmt.Println("文件上传服务")
    args := getArgs()
    port := args["port"]
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
    http.HandleFunc("/upload/path", uploadPath)
    log.Println("请求网址如下:")
    host, err := os.Hostname()
    if err != nil {
        fmt.Println("获取主机名错误")
    }
    log.Printf("http://%v:%v/", host, port)
    ip := strings.Replace(getIp(), "\n", "", -1)
    log.Printf("http://%v:%v/", ip, port)
    pwd, err := os.Getwd()
    if pwd == "" {
        pwd = "/home/work"
    }
    // 上传到当前文件夹下
    commandHost := fmt.Sprintf(`curl -XPOST -F '%s=@%s' %s:%s/upload`, fileKey, pwd, host, port)
    commandIp := fmt.Sprintf(`curl -XPOST -F '%s=@%s' %s:%s/upload`, fileKey, pwd, ip, port)
    splitStr := "===================================================================================="
    log.Println(splitStr)
    log.Printf("命令行工具 file 要上传文件的位置\n%v", commandHost)
    log.Printf("命令行工具 file 要上传文件的位置\n%v", commandIp)
    log.Println(splitStr)
    // 指定目录上传命令
    commandPathHost := fmt.Sprintf(`curl -XPOST -F '%s=@%s' -F '%s=%s' %s:%s/upload/path`, fileKey, pwd, pathKey, pwd, host, port)
    commandPathIp := fmt.Sprintf(`curl -XPOST -F '%s=@%s' -F '%s=%s' %s:%s/upload/path`, fileKey, pwd, pathKey, pwd, ip, port)
    log.Printf("命令行工具 file 要上传文件的位置 path 上传到服务器的位置\n%v", commandPathHost)
    log.Printf("命令行工具 file 要上传文件的位置 path 上传到服务器的位置\n%v", commandPathIp)
    log.Println(splitStr)
    // 客户端别名命令
    aliasStr := fmt.Sprintf("alias pushFile='pushFile(){curl -XPOST -F %s=@$1 -F %s=%s %s:%s/upload/path;};  pushFile'", fileKey, pathKey, pwd, host, port)
    log.Printf("客户端起别名命令\n%v\n使用方式 [pushFile fileName] \n", aliasStr)
    log.Println(splitStr)
    err1 := http.ListenAndServe(":"+port, nil)
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
    pwd, err := os.Getwd()
    if err != nil {
        pwd = "/home/work"
    }
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
            <form enctype="multipart/form-data" action="/upload/path" method="post">
                <label for="formFileMultiple" class="form-label">简易文件上传服务</label>
                <div class=" mb-3">
                    <input class="form-control" type="file" id="formFileMultiple" name="%v" multiple>
                </div>
                <div class="input-group mb-3">
                    <span class="input-group-text" id="basic-addon1">保存的文件夹位置</span>
                    <input type="text" class="form-control" name="%v" placeholder="%v" value="%v" aria-describedby="basic-addon1">
                </div>
                <button type="submit" class="btn btn-primary">提交文件</button>
                <button type="reset" class="btn btn-primary">取消</button>
            </form>
        </div>
    </body>
    
    </html>
    `, fileKey, pathKey, pwd, pwd)
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
    msg := GetSuccessResult("保存成功")
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
