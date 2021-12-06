package main

import (
	"fmt"
	"sort"
)

// main
// go run go-string.go
func main() {
	fmt.Println("start ...")
	// testListCreate()
	testList()
	fmt.Println("end ...")
}

// test 测试 list 结构
func testListCreate() {
	// 不指定长度就是切片
	// 默认是nil
	var list []int
	var list1 []int = make([]int, 0)
	var list2 []int = make([]int, 1, 2)
	list3 := make([]int, 1, 2)
	fmt.Printf("list = [%v] len = [%v] cap = [%v]\n", list, len(list), cap(list))
	fmt.Printf("list1 = [%v] len = [%v] cap = [%v]\n", list1, len(list1), cap(list1))
	fmt.Printf("list2 = [%v] len = [%v] cap = [%v]\n", list2, len(list2), cap(list2))
	fmt.Printf("list3 = [%v] len = [%v] cap = [%v]\n", list3, len(list3), cap(list3))

	// 添加
	list = append(list, 1)
	list = append(list, 1)
	list1 = append(list1, 1)
	list1 = append(list1, 1)
	list2 = append(list2, 1)
	list2 = append(list2, 1)
	list2 = append(list2, 1)
	list2 = append(list2, 1)
	list2 = append(list2, 1)
	list2 = append(list2, 1)
	list2 = append(list2, 1)
	list2 = append(list2, 1)

	fmt.Printf("list = [%v] len = [%v] cap = [%v]\n", list, len(list), cap(list))
	fmt.Printf("list1 = [%v] len = [%v] cap = [%v]\n", list1, len(list1), cap(list1))
	fmt.Printf("list2 = [%v] len = [%v] cap = [%v]\n", list2, len(list2), cap(list2))
}

func testList() {
	strs := make([]string, 0)
	strs = append(strs, "a", "a", "a", "c", "b", "aaa", "h", "", " ", "", "\t")
	testStr := []string{"a", "hh", "a", " a ", "nn", "n", "\t", "h"}
	for _, v := range testStr {
		fmt.Printf("strs 包含 [%v] => [%v]\n", v, contains(v, strs))
	}

	for _, v := range testStr {
		fmt.Printf("strs = [%v]\n", String(strs))
		remove(v, &strs)
		fmt.Printf("remove [%v] 后 \nstrs = [%v]\n", v, String(strs))
		fmt.Println()
	}

}

// contains 判断切片中是否包含某个值
func contains(key string, list []string) bool {
	if len(list) == 0 {
		return false
	}
	// 先排序 在查找
	sort.Strings(list)
	i := sort.SearchStrings(list, key)
	return i < len(list) && list[i] == key
}

// remove 移除指定元素
// go 默认是值传递,使用引用传递需要使用指针对象
func remove(key string, list *[]string) {
	if len(*list) == 0 {
		return
	}
	for i := 0; i < len(*list); i++ {
		if key == (*list)[i] {
			// go list 删除元素
			*list = append((*list)[:i], (*list)[i+1:]...)
			// 必须 -- 不然不元素 出错
			i--
		}
	}
}

// string 输出切片
func String(list []string) string {
	if len(list) == 0 {
		return ""
	}
	info := ""
	for _, v := range list {
		info = info + fmt.Sprintf("[%v]", v)
	}
	res := fmt.Sprintf("len = [%v],value = %v", len(list), info)
	return res
}
