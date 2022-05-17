package main

import "fmt"

func getNum(num uint64) int64 {
	value := int64(num)
	// fmt.Printf("%d\n", value)
	return value
}

func getValue(num int64) {
	value := uint64(num)
	fmt.Printf("%d\n", value)
}

//main
func main() {
	fmt.Println("Hello world!")
	nums := []uint64{
		18446744069412284321,
	}
	for i := 0; i < len(nums); i++ {
		value := getNum(nums[i])
		fmt.Println(nums[i], value)
	}
	// getNum(18446744069412284321)
	// getValue(-4253024255)
}
