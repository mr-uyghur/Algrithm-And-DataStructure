// Reverse String

function reverseString(str) {
    // new var with empty string
    let newWord = "";
    // loop through str in reverse
  for(let i = str.length-1; i>=0; i--){
    // add each letter to empty var in reverse
  newWord += str[i]
  }
    // return new var
    return newWord;
  }
  reverseString("hello");


// Factorialize a Number
// Factorials are often represented with the shorthand notation n!
// For example: 5! = 1 * 2 * 3 * 4 * 5 = 120
function factorialize(num) {
    // var for the sum 
    let sum = 1
    // for loop from 1-num
    for(let i=1; i<=num; i++){
   // sum multiply from 1 till num 
   sum *= i
    }
    // return the sum
   return sum;
  }
  console.log(factorialize(5)); //

//   Find the Longest Word in a StringPassed

function findLongestWordLength(str) {
    // break down str to arr with split 
    let words = str.split(' ')
    // var for number place holder
    let maxNum = words[0].length
    // loop through the str 
    // find the longest str with if condition
    for(let i =0; i< words.length; i++){
      if(maxNum < words[i].length){
        maxNum = words[i].length
      }
    }
    // return the maxNum var
    return maxNum;
  }
 console.log( findLongestWordLength("The quick brown fox jumped over the lazy dog"));

//  Return Largest Numbers in Arrays
// Example:  largestOfFour([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]) 
// should return [27, 5, 39, 1001].
function largestOfFour(arr) {
    // a var for arr holder
    let newArr = [];
    // loop through the arr
    for(let i =0; i < arr.length; i++){
        // var for maxNum placeholder
      let maxNum = arr[i][0]
      // inner loop for inner arrs
      for(let j=1; j < arr[i].length; j++){
    // find the max num inside the inner loop and push it to arr holder 
        if(maxNum < arr[i][j]){
          maxNum = arr[i][j];
        }
      }
     newArr[i] = maxNum;
    }
    // return arr holder
    return newArr;
  }
 console.log( largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));


//  Confirm the Ending
// Check if a string (first argument, str) ends with the given target string (second argument, target).
// confirmEnding("Congratulation", "on") should return true.
// confirmEnding("Connor", "n") should return false.

function confirmEnding(str, target) {
    return str.slice(str.length - target.length) === target;
    }
    
    confirmEnding("Bastian", "n");
    // Code Explanation
    // First we use the slice method copy the string.
    // In order to get the last characters in str equivalent to the target's length we use the slice method.
    // The first parameter inside the slice method is the starting index and the second parameter would be the ending index
    // In this case we only include one parameter which it will copy everything from the starting index.
    // We substract the length of str and the length of target, that way, we shall get the last remaining characters equivalent to the target's length.
    // Finally we compare the return result of slice to target and check if they have the same characters.