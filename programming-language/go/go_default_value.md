# go 中的各种默认值

## 类型

Go 语言将数据类型分为四类：基础类型、复合类型、引用类型和接口类型

### 基础类型

- 整形

  有符号整形 int8 int16 int32 int64 默认值 0

  无符号整形 uint8 uint16 uint32 uint64 默认值 0

  特殊整形 int uint byte rune uintptr 默认值 0

- 浮点型

  浮点型数 float32 float64 默认值 0.0

  复数类型 complex64 complex128 默认值 0+0i

  布尔类型 true false 默认值 false

- 字符串类型 string 默认值 ""

- 复合类型

  数组类型 [SIZE]TYPE 默认值根据数组类型变化而变化 如 [3]int 为 [0,0,0]

  结构体类型 struct 默认值根据随结构体内部类型变化而变化，如下默认值为{ 0} 即 Name 为"" Age 为 0

  type Person struct { Name string Age int }

- 引用类型

  指针 \*TYPE 默认值 nil

  切片 []TYPE 默认值 nil

  字典 map[TYPE][type] 默认值 nil

  通道 chan 默认值 nil

  函数 func 默认值 nil

- 接口类型

  接口 interface 默认值 nil

  这里要特别注意 **nil 在 Go 中不同类型的 nil 是无法比较的，他们的大小也不一样**
  
  引用类型中的 slice map chan 要使用 make 函数初始化，如果常规 var NAME TYPE 的方式声明，将不能通过正常的赋值方法来修改默认值
