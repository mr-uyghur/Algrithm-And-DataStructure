// iFibonacci
// iFibonacci(0) = 0           => 0
// iFibonacci(1) = 1           => 1
// iFibonacci(2) = 1           => 1
// iFibonacci(3) = 1 + 1       => 2
// iFibonacci(4) = 1 + 2       => 3
// iFibonacci(5) = 2 + 3       => 5
// iFibonacci(6) = 3 + 5       => 8

// iterative solution
function iFibonacci(n){
    let fibs = [0,1]
    for(let i =0; i < n; i++){
        fibs.push(fibs[0]+fibs[1])
        fibs.shift()
    }
    return fibs[0]
}
console.log(iFibonacci(3))

// recursive solution
function rFibonacci(n){
    if(n == 1 || n == 2){
        return 1
    }
    let num = 0
    num = rFibonacci(n-2) + rFibonacci(n-1)
    return num
}

console.log(rFibonacci(4))