fn main() {
    test_println();
}

fn test_println() {
    // 单个占位符
    println!("{}", 1);
    // 多个占位符
    println!("{} {}", 1, 3);
    // 位置参数
    println!(
        "{0} 是 {1} {2}，{0} 也是 {3} 编程语言",
        "Rust", "cool", "language", "safe"
    );
    // 命名参数
    println!("{country} 是一个团结的国家", country = "China");
    // 占位符特征 :b 表示二进制， :0x 表示十六进制， :o 表示八进制
    println!(
        "让我们打印 76 是二进制的 {:b} ，十六进制等价物是 {:0x} 八进制等价物是 {:o}",
        76, 76, 76
    );
    // 调试特征
    println!(
        "使用调试特征 {:?} 在此处打印我们想要的任何内容",
        (76, 'A', 90)
    );

    // 1.58 中的新格式字符串
    let x = "world";
    println!("Hello {x}!");
}
