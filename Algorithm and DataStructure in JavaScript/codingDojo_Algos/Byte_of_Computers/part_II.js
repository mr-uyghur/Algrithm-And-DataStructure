// iFibonacci
// iFibonacci(0) = 0           => 0
// iFibonacci(1) = 1           => 1
// iFibonacci(2) = 1           => 1
// iFibonacci(3) = 1 + 1       => 2
// iFibonacci(4) = 1 + 2       => 3
// iFibonacci(5) = 2 + 3       => 5
// iFibonacci(6) = 3 + 5       => 8

// iterative solution
function iFibonacci(n) {
    let fibs = [0, 1]
    for (let i = 0; i < n; i++) {
        fibs.push(fibs[0] + fibs[1])
        fibs.shift()
    }
    return fibs[0]
}
console.log(iFibonacci(5))

// recursive solution
function rFibonacci(n) {
    if (n == 1 || n == 2) {
        return 1
    }
    let num = 0
    num = rFibonacci(n - 2) + rFibonacci(n - 1)
    return num
}

console.log(rFibonacci(89))

// iterative Binary search. For example
// Pseudocode
// 1. Set lower bound to first position of array

// 2. Set upper bound to last position of array

// 3. While lower bound is less than or equal to the upper bound do the following steps:

// Set midpoint as upper bound plus lower bound divided by 2
// If midpoint element is less than the data being searched for, set new lower bound to midpoint + 1
// If midpoint element is greater than the data being searched for, set new upper bound to the midpoint - 1
// else midpoint is the found element

function binarySearch(arr,target,min = 0,max = arr.length-1){
    while(min<=max){
        let mid = Math.floor((min+max) /2)
        if(arr[mid] < target){
            min = mid +1
        }
        else if(arr[mid] > target){
            max = mid -1
        }
        else{
            return mid
        }
        
    }
}
var arr = [-90,-19,0,2,12,29,33,190,320];
console.log( binarySearch(arr,0))


