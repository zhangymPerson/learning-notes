//执行 tsc index.ts 生成 index.js
//执行 node index.ts 可直接打印 Hello Word! 不生成 js文件
//简单的可以  复杂的 必须转 js执行
console.log("Hello Word!");

function f(shouldInitialize: Boolean) {
    if (shouldInitialize) {
        var x = 10;
    }

    return x;
}

// name属性在window对象上定义： 您需要为变量提供一个新名称：
// var name: string = "错误";

console.log(f(true));
console.log(f(false));
