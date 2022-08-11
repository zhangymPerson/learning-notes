// show_docker_tag.go
// info: 获取docker镜像的tag列表
// date : 2022-07-15 11:35:19
// auth : danao
// version : 0.1
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main() {
	url := "https://registry.hub.docker.com/v2/repositories/library/"
	args := os.Args
	if len(args) == 1 {
		log.Fatalf("请输入要查询的镜像名,如 mysql \n %v mysql", args[0])
		return
	}
	for i := 1; i < len(args); i++ {
		repoName := args[i]
		log.Printf("查询的镜像名[%+v]\n", repoName)
		tagUrl := fmt.Sprintf("%s%s/tags/", url, repoName)
		log.Printf("查询路由[%v]\n", tagUrl)
		res := getInfo(tagUrl)
		// log.Printf("res is [%+v]\n", res)
		jsonMap := make(map[string]interface{})
		// log.Printf("jsonMap is [%+v]\n", jsonMap)
		err := json.Unmarshal([]byte(res), &jsonMap)
		if err != nil {
			log.Fatal("异常,异常信息如下:", err)
		}

		if results, ok := jsonMap["results"].([]interface{}); ok {
			for _, v := range results {
				res := v.(map[string]interface{})
				log.Printf("res is [%+v:%+v]\n", repoName, res["name"])
			}
		} else {
			log.Fatalf("没有查找到[%+v]的镜像版本信息", repoName)
		}
	}
}

func getInfo(url string) string {
	method := "GET"

	client := &http.Client{}
	req, err := http.NewRequest(method, url, nil)

	if err != nil {
		log.Fatal("异常,异常信息如下:", err)
	}
	res, err := client.Do(req)
	if err != nil {
		log.Fatal("异常,异常信息如下:", err)
	}
	defer res.Body.Close()
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatal("异常,异常信息如下:", err)
	}
	return string(body)
}
