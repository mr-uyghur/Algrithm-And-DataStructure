// Linear Search
// find the target from a givin array
function linearSearch(target, value) {
    for (let i = 0; i < value.length; i++) {
        if (target === value[i]) {
            return i
        }
    }
    return false
}
var arr = [24, 8, 23, 3];
console.log(linearSearch(8, arr))

// using ideration to find sums
function rSum(num) {
    // place holder var for sums  
    let sum = 0;
    // use reverse for loop to interate till the given num
    for (let i = num; i >= 1; i--) {
        sum += i
    }
    // return sum 
    return sum
}

console.log(rSum(4))
// alternate method with recursion formula

// rSum(1) = 1                  => 1  **BASE CASE**
// rSum(2) = rSum(1) + 2        => 3
// rSum(3) = rSum(2) + 3        => 6
// rSum(4) = rSum(3) + 4        => 10
// rSum(5) = rSum(4) + 5        => 15

function rSum2(n) {
    if (n === 1) {
        return 1;
    } else {
        // function will be called again in this condition
        // examnlpe :rSum(5) -> 5 + rSum(4) -> 4 + rSunm(3) etc
        return rSum2(n - 1) + n;
    }
}

console.log(rSum2(4))

//   iFactorial with ideration

// iFactorial(1) = 1                  => 1
// iFactorial(2) = 2 * 1              => 2
// iFactorial(3) = 3 * 2 * 1          => 6
// iFactorial(4) = 4 * 3 * 2 * 1      => 24
// iFactorial(5) = 5 * 4 * 3 * 2 * 1  => 120

function iFactorial(num) {
    // place holder var for the total numbers
    let total = 1
    // use reverse for loop to multiply each number to the total
    for (let i = num; i >= 1; i--) {
        total *= i
    }
    return total
}

console.log(iFactorial(4))

// iFactorial with recursion
function iFactorial2(num) {
    if (num === 1) {
        return 1
    }
    return iFactorial2(num - 1) * num
}
console.log(iFactorial2(5))
