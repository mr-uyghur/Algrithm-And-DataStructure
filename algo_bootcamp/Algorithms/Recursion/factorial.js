// Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop


//5! = 5 * 4 * 3 *2 *1
function findFactorialRecursive(number) {
    //code here
    if(number === 1){
        return 1
    }
    //recursion 
    return findFactorialRecursive(number - 1) * number
}

function findFactorialIterative(number) {
    //code here
    let answer = 1
    for(let i = number; i >=1; i--){
        answer *= i
    }
    return answer;
}

// console.log(findFactorialIterative(5))

// console.log(findFactorialRecursive(5))