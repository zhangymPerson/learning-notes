package main

import (
    "fmt"
    "sort"
)

// go中list 类比是 slice
// crud 增删改查
func crud() {
    // ===============================
    //定义
    var s0 []int
    fmt.Println(s0)
    // 空切片
    s1 := []int{}
    // 初始化带值的切片
    s2 := []int{1, 2, 3}

    fmt.Println(s1, s2)

    //指定长度
    s3 := make([]int, 12)
    //指定长度和空间
    s4 := make([]int, 10, 100)

    fmt.Println(s3, s4)

    array := [5]int{1, 2, 3, 4, 5}
    // 从数组切取
    s5 := array[0:2]
    // 从切片切取
    s6 := s5[0:1]
    fmt.Println(s5) // [1 2]
    fmt.Println(s6) // [1]

    // ===============================
    s := make([]int, 0)
    s = append(s, 1)              // 添加1个元素
    s = append(s, 2, 3, 4)        // 添加多个元素
    s = append(s, []int{5, 6}...) // 添加一个切片
    fmt.Println(s)

    fmt.Println(len(s))
    fmt.Println(cap(s))
}

// test 测试 list 结构
func testCrud() {
    crud()
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

func testRemove() {
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

// main
// go run go-string.go
func main() {
    fmt.Println("start ...")
    // testCrud()
    // testRemove()
    fmt.Println("end ...")
}
