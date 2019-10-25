
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