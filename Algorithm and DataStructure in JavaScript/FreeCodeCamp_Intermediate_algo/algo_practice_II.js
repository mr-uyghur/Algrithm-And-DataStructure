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


// Smallest Common Multiple
// Find the smallest common multiple of the provided parameters that can be evenly divided by both, 
// as well as by all sequential numbers in the range between these parameters.
// For example, if given 1 and 3,
//  find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. 
//  The answer here would be 6.

function smallestCommons(arr) {
  // Sort array from greater to lowest
  // This line of code was from Adam Doyle (http://github.com/Adoyle2014)
  arr.sort(function(a, b) {
    return b - a;
  });
  // Create new array and add all values from greater to smaller from the
  // original array.
  var newArr = [];
  for (var i = arr[0]; i >= arr[1]; i--) {
    newArr.push(i);
  }
  // Variables needed declared outside the loops.
  var quot = 0;
  var loop = 1;
  var n;
  // Run code while n is not the same as the array length.
  do {
    quot = newArr[0] * loop * newArr[1];
    for (n = 2; n < newArr.length; n++) {
      if (quot % newArr[n] !== 0) {
        break;
      }
    }
    loop++;
  } while (n !== newArr.length);

  return quot;
}
// test here
smallestCommons([1, 5]);

// Drop it
// Given the array arr, iterate through and remove each element starting from the first element (the 0 index)
//  until the function func returns true when the iterated element is passed through it.

function dropElements(arr, func) {
  for(let i =0; i < arr.length; i++){
    if(func(arr[0])){
      break
    } else{
      arr.shift()
    }
  }
  return arr;
}

dropElements([1, 2, 3], function(n) {return n < 3; });

// Steamroller
// Flatten a nested array. You must account for varying levels of nesting.
// steamrollArray([[["a"]], [["b"]]]) should return ["a", "b"].
// steamrollArray([1, [2], [3, [[4]]]]) should return [1, 2, 3, 4].

function steamrollArray(arr) {
  // place holder for array
  let newArr = []
  // loop through arr and put each value to the new array
  for(let i=0; i < arr.length; i++) {
    if(Array.isArray(arr[i])){
      let subArr = steamrollArray(arr[i]);
      newArr = newArr.concat(subArr);
    } else {
      newArr.push(arr[i])
    }
   
  }
  // return new array
  return newArr
}
console.log(steamrollArray([1, [2], [3, [[4]]]]));

// Binary Agents
// Return an English translated sentence of the passed binary string.
function binaryAgent(str) {
  var biString = str.split(" ");
  var uniString = [];

  /*using the radix (or base) parameter in parseInt, we can convert the binary
      number to a decimal number while simultaneously converting to a char*/

  for (var i = 0; i < biString.length; i++) {
    uniString.push(String.fromCharCode(parseInt(biString[i], 2)));
  }

  // we then simply join the string
  return uniString.join("");
}

binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111");

// Everything Be True
function truthCheck(collection, pre) {
  
  // loop through collection data and check if pre exists within that data
  // return true 
  // else return false
  return collection.every(item => item[pre])
}

truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy", "sex": "male"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex");

