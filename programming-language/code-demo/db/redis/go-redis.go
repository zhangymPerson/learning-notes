package main

import (
	"fmt"
	"log"

	"github.com/gomodule/redigo/redis"
)

// 提示用户输入
func getArgs(info string) string {
	fmt.Println(info)
	res := ""
	fmt.Scanln(&res)
	return res
}

func getConn(host string, port int) redis.Conn {
	url := fmt.Sprintf("%v:%v", host, port)
	conn, err := redis.Dial("tcp", url)
	if err != nil {
		return nil
	}
	return conn
}

// 各种类型数据操作
// String: 字符串

func redisStrTest(conn redis.Conn) {
	// 写
	_, err := conn.Do("SET", "redis_str_test", "redis_str_test")
	if err != nil {
		log.Fatalln("写入key失败", err)
	}
	// 读
	str, err := redis.String(conn.Do("GET", "redis_str_test"))
	if err != nil {
		log.Fatalln("读取key失败", err)
	} else {
		log.Println(str)
	}
}

// Hash: 散列
func redisHashTest() {
	// 写
	// 读
}

// List: 列表
func redisListTest(conn redis.Conn) {
	// 写
	key := "redis_list_test"
	_, err := conn.Do("lpush", key, "one", 3, 4.5, true)
	conn.Do("lpush", key, "A")
	conn.Do("lpush", key, "B")
	conn.Do("lpush", key, "C")
	if err != nil {
		log.Fatalln("lpush 错误", err)
	}
	// 读
	value, err := redis.Values(conn.Do("lrange", key, 0, -1))
	if err != nil {
		log.Fatalln("lrange 错误", err)
	} else {
		for _, v := range value {
			fmt.Println(string(v.([]byte)))
		}
	}
}

// Set: 集合
func redisSetTest() {
	// 写
	// 读
}

// Sorted Set: 有序集合

func main() {
	host := "127.0.0.1"
	port := 6379
	conn := getConn(host, port)
	redisStrTest(conn)
	redisListTest(conn)
}
