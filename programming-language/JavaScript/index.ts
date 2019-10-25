//执行 tsc index.ts 生成 index.js 
//执行 node index.ts 可直接打印 Hello Word! 不生成 js文件
//简单的可以  复杂的 必须转 js执行
console.log("Hello Word!");

function f(shouldInitialize : Boolean) {
    if (shouldInitialize) {
        var x = 10;
    }

    return x;
}

console.log(f(true));
console.log(f(false));