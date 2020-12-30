// Distribution
// uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]) 
// should return [1, 3, 2, 5, 4]
// uniteUnique([1, 2, 3], [5, 2, 1]) should return [1, 2, 3, 5].

function uniteUnique(arr1) {
    // need to convert 2d array to 1D array
    // place holder var for new array
    let newArr = []
    // loop through every arguement in outter loop
    for(let i=0; i<arguments.length; i++) {
        let arg = arguments[i];
        // loop through the current arr
        for(let j=0; j<arg.length; j++) {
            var idx = arg[j]
            // check if the value exists on the new array
            if(newArr.indexOf(idx) < 0){
                newArr.push(idx)
            }
        }
    }
    return newArr;
  }
  
console.log(uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]))

// Convert HTML Entities
// Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a string to their corresponding HTML entities.

function convertHTML(str) {
    // place holder var for new str
    let newStr = str.split("")
    // loop through str, and find html values
    // replace those values with relative HTML entities
    for (var i = 0; i < newStr.length; i++) {
        switch (newStr[i]) {
          case "<":
            newStr[i] = "&lt;";
            break;
          case "&":
            newStr[i] = "&amp;";
            break;
          case ">":
            newStr[i] = "&gt;";
            break;
          case '"':
            newStr[i] = "&quot;";
            break;
          case "'":
            newStr[i] = "&apos;";
            break;
        }
      }
    // return newStr
    return newStr.join("")
  }
  
 console.log( convertHTML("Dolce & Gabbana"))

//  Sum All Odd Fibonacci Numbers
// The first two numbers in the Fibonacci sequence are 1 and 1. Every additional number in the sequence is the sum of the two previous numbers.
//  The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.
// For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less than or equal to 10 are 1, 1, 3, and 5.

function sumFibs(num) {
    // create place holder var for current and prev number, also a var for the result 
    let prevNum = 0;
    let currentNum = 1;
    let result = 0;
    // loop till we reach the given num for out function
    while(currentNum <= num){
        // chech if the current number is Odd
        if(currentNum %2 !== 0){
            // add this odd number to the result
            result += currentNum;
        }
        // complete the fabonacci nums with the logic below
        currentNum += prevNum;
        prevNum = currentNum - prevNum
    }
    // return result
    return result
  }
  
 console.log( sumFibs(4))

// Sum All Primes
// A prime number is a whole number greater than 1 with exactly two divisors:
//  1 and itself. For example, 2 is a prime number because it is only divisible by 1 and 2.
//   In contrast, 4 is not prime since it is divisible by 1, 2 and 4.
// Rewrite sumPrimes so it returns the sum of all prime numbers that are less than or equal to num.

// Login for checking prime numbers
function isPrime(num) {
    if(num < 2) return false;
    for (var i = 2; i < num; i++) {
        if(num%i==0)
            return false;
    }
    return true;
}
function sumPrimes(num) {
//   a place holder var for the sum 
let sum = 0;
// loop till the given num and find prime numbers inside the loop 
// add only the prime numbers to our sum 
for(let i = 1; i<= num; i++){
    // helper function from above
    if (isPrime(i)){
        sum += i;
    }
}
// return the sum
return sum
}
console.log(sumPrimes(10))