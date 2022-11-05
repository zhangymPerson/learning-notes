//函数测试
function f(shouldInitialize) {
    if (shouldInitialize) {
        var x = 10;
    }

    return x;
}

console.log(f(true));
console.log(f(false));


function f() {
    var a = 1;

    a = 2;
    var b = g();
    a = 3;

    return b;

    function g() {
        return a;
    }
}

console.log(f());

//=========================================================================================================
//js中的let和var
var vararg = "var定义的参数";
let letarg = "letarg定义的参数";
console.log(vararg);
console.log(letarg);

//在ES6之前，我们都是用var来声明变量，而且JS只有函数作用域和全局作用域，没有块级作用域，所以{}限定不了var声明变量的访问范围。
{
    var vart = "var test";
}
console.log(vart);  // 9
//ES6新增的let，可以声明块级作用域的变量。
{
    let lett = "let test";     // i变量只在 花括号内有效！！！
}
// Uncaught ReferenceError: i is not defined
//console.log(lett);  


//let 配合for循环的独特应用
//let非常适合用于 for循环内部的块级作用域。
//JS中的for循环体比较特殊，每次执行都是一个全新的独立的块作用域，
//用let声明的变量传入到 for循环体的作用域后，不会发生改变，不受外界的影响。看一个常见的面试题目：

for (var i = 0; i < 10; i++) {
    setTimeout(function () {  // 同步注册回调函数到 异步的 宏任务队列。
        console.log(i);        // 执行此代码时，同步代码for循环已经执行完成
    }, 0);
}
// 输出结果
//10   共10个

// 这里面的知识点： JS的事件循环机制，setTimeout的机制等
//如果把 var改成 let声明：
// i虽然在全局作用域声明，但是在for循环体局部作用域中使用的时候，变量会被固定，不受外界干扰。
for (let i = 0; i < 10; i++) {
    setTimeout(function () {
        //  i 是循环体内局部作用域，不受外界影响。
        console.log(i);
    }, 0);
}
// 输出结果：
//0  1  2  3  4  5  6  7  8 9
//=========================================================================================================