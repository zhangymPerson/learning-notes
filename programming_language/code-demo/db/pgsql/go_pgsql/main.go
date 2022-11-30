// main.go
// info: 操作 postgresql
// date : 2022-11-29 15:12:34
// auth : danao
// version : 0.1

package main

import (
	"database/sql"
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"

	_ "github.com/jackc/pgx/v5/stdlib"
)

var (
	// 用户名
	username string
	// 密码
	password string
	// 连接的数据库
	host string
	// 连接的端口
	port int
	// 数据库
	databaseName string
	// 需要执行的 sql
	execSql string
	debug   bool
)

func main() {
	log.Printf("pgsql 执行脚本启动...")
	flag.StringVar(&username, "u", "root", "用户名,默认为 [root]")
	flag.StringVar(&password, "p", "123456", "密码,默认为 [123456]")
	flag.StringVar(&host, "h", "127.0.0.1", "主机名,默认 127.0.0.1")
	flag.IntVar(&port, "P", 5432, "端口号,默认为空")
	flag.StringVar(&execSql, "sql", "", "要执行的 sql 语句")
	flag.StringVar(&databaseName, "d", "database_name", "数据库名，默认为 [database_name]")
	flag.BoolVar(&debug, "debug", false, "是否启用debug")
	// 参数生效
	flag.Parse()
	if debug {
		log.Printf("用户名:[%v],密码[%v],host[%v],port[%v],数据库名[%v]\n", username, password, host, port, databaseName)
		log.Printf("要执行的sql:[%+v]\n", execSql)
	}
	url := fmt.Sprintf("postgres://%v:%v@%v:%v/%v", username, password, host, port, databaseName)
	if debug {
		log.Printf("url is [%+v]\n", url)
	}
	execPostgreSql(url, execSql)
	log.Printf("脚本执行完成!")
}

// execPostgreSql 执行sql
// urlExample := "postgres://username:password@localhost:5432/database_name"
func execPostgreSql(databaseUrl, execSql string) {

	db, err := sql.Open("pgx", databaseUrl)
	if err != nil {
		log.Fatalln("连接数据库失败", databaseUrl, err)
		os.Exit(1)
	}
	defer db.Close()
	if debug {
		// 测试
		var greeting string
		testSql := "select 'Hello, world!'"
		err = db.QueryRow(testSql).Scan(&greeting)
		if err != nil {
			log.Fatalln("查询数据库失败", databaseUrl, err)
			os.Exit(1)
		}
		log.Printf("testSql = [%+v], 执行成功[%v]\n", testSql, greeting)
	}
	if strings.Contains(execSql, "delete") {
		log.Printf("execSql is [%+v]\n", execSql)
		input := GetUserInput("是否确认执行删除操作!确认请输入 'true'")
		if !strings.EqualFold("true", strings.ToLower(input)) {
			os.Exit(0)
		}
	}
	rows, err := db.Query(execSql)
	if err != nil {
		log.Fatalf("执行sql[%v]失败，错误原因\n%v", execSql, err)
	} else {
		log.Printf("用户输入的sql:[%+v]执行成功!\n", execSql)
		// log.Printf("执行结果:\n[%+v]\n", rows)
		RowsToJson(rows)
	}
}

// GetUserInput
// info 用户输入提醒词
// res 返回用户输入内容
func GetUserInput(info string) (res string) {
	log.Println(info)
	fmt.Scanln(&res)
	return
}

// 数据库查询到的数据转成json打印
func RowsToJson(rows *sql.Rows) {
	// 查询列信息
	columns, err := rows.Columns()
	if err != nil {
		log.Fatal("解析rows异常,异常信息如下:", err)
	}
	count := len(columns)
	values := make([]interface{}, count)
	scanArgs := make([]interface{}, count)
	// rows.Scan 需要传入 对象的地址 的数组
	// 所以不能直接传入values 需要用 scanArg转成 &values 的地址值
	for i := range values {
		scanArgs[i] = &values[i]
	}
	for rows.Next() {
		// 将取到的值赋值到 values 中
		err := rows.Scan(scanArgs...)
		if err != nil {
			log.Fatal("接收对象异常,异常信息如下:", err)
		}
		// 构建一个map
		data := make(map[string]interface{}, count)
		for k, v := range values {
			// fmt.Printf("k: %+v =>", columns[k],v)
			data[columns[k]] = v
		}
		jsonBytes, _ := json.Marshal(data)
		fmt.Printf("json格式化如下:\n%+v\n", string(jsonBytes))
	}
}
