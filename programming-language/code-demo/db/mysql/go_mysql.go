package main

import (
	"database/sql"
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
			log.Println(err)
		}
		cols, err := rows.Columns()
		if err != nil {
			log.Println(err)
		}
		num := len(cols)
		for rows.Next() {
			data := make([]interface{}, num)
			for n := range data {
				var a interface{}
				data[n] = a
			}
			err := rows.Scan(data...)
			if err != nil {
				log.Println(err)
			}
			for _, value := range data {
				fmt.Printf("%v", value)
			}
			fmt.Println()
		}
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
