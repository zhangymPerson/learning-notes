package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"time"

	_ "github.com/go-sql-driver/mysql"
)

// getDb 获取连接
func getDb() *sql.DB {
	db, err := sql.Open("mysql", "root:123456@tcp(127.0.0.1:3306)/img_approve_test")
	if err != nil {
		panic(err)
	}
	// See "Important settings" section.
	db.SetConnMaxLifetime(time.Minute * 3)
	db.SetMaxOpenConns(10)
	db.SetMaxIdleConns(10)
	return db
}

// getAllTable() 获取当前库下的所有的表
func getAllTable(db *sql.DB) []string {
	res := []string{}
	rows, err := db.Query("show tables;")
	if err != nil {
		fmt.Printf("err: %v\n", err)
	}
	defer rows.Close()
	for rows.Next() {
		var tableName string
		err := rows.Scan(&tableName)
		if err != nil {
			log.Fatal(err)
		}
		res = append(res, tableName)
	}
	err = rows.Err()
	if err != nil {
		log.Fatal(err)
	}
	return res
}

// 将 query 结果改成 map 结构
func queryResultAsMap(db *sql.DB, tables []string) {
	if len(tables) < 1 {
		return
	}
	for _, tableName := range tables {
		sql := fmt.Sprintf("select * from %v limit 10", tableName)
		fmt.Println(sql)
		rows, err := db.Query(sql)
		if err != nil {
			log.Fatal("异常,异常信息如下:", err)
		}
		RowsToJson(rows)
	}
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
		jsonBytes, _ := json.MarshalIndent(data, "", "    ")
		fmt.Printf("json格式化如下:\n%+v\n", string(jsonBytes))
	}
}

func main() {
	fmt.Println("hello word")
	db := getDb()
	tables := getAllTable(db)
	for i := 0; i < len(tables); i++ {
		println("表名是:", tables[i])
	}
	queryResultAsMap(db, tables)
}
