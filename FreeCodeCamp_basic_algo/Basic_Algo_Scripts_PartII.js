// Repeat a String Repeat a String
// Repeat a given string str (first argument) for num times (second argument).
//  Return an empty string if num is not a positive number. For the purpose of this challenge, do not use the built-in .repeat() method.
function repeatStringNumTimes(str, num) {
    // if val of num is not a positive num
    // return empty str
    let newWord = ""
    if(num <= 0){
      return "";
    }
    // else repeat the str with num and return it
     else {
      // user for loop to repeat
      for(let i =1; i<=num;i++){
        // add str to newWord in num of times
        newWord += str
      }
    }
  return newWord;
  }
  console.log(repeatStringNumTimes("abc", 3));



  // Truncate a String
  // truncateString("A-tisket a-tasket A green and yellow basket", 8) should return "A-tisket...".
//   truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length) should return "A-tisket a-tasket A green and yellow basket".
// truncateString("A-tisket a-tasket A green and yellow basket", "A-tisket a-tasket A green and yellow basket".length + 2) should return "A-tisket a-tasket A green and yellow basket".
  function truncateString(str, num) {
    // edge case
    // incase the num used str.length and str.length + n
    if(str.length <= num){
      return str;
    }
    // need a place holder var
    let newStr = ""
    // loop through str till num
    for(let i =0; i < num; i++){
    // add str to place holder var
      newStr += str[i]
    }
    return newStr += "..." 
  }
  
  truncateString("A-tisket a-tasket A green and yellow basket", 8);


  // Finders Keepers
//   findElement([1, 3, 5, 8, 9, 10], function(num) { return num % 2 === 0; }) should return 8.
// findElement([1, 3, 5, 9], function(num) { return num % 2 === 0; }) should return undefined

function findElement(arr, func) {
  let num = 0;
  // loop through the arr from start to end
  // check if the index of arr is true for func
  // reaplce num with that index of arr
  for(let i =0; i <arr.length;i++){
    if(func(arr[i])){
      num = arr[i];
      return num;
    } 
  } 
  return undefined;
}

findElement([1, 2, 3, 4], num => num % 2 === 0);


// Check if a value is classified as a boolean primitive. Return true or false.
// Boolean primitives are true and false.
function booWho(bool) {
  // check if bool is a boolean, return true if it is
  if(bool === true || bool === false){
    return true;
  } else {
    return false;
  }
  
}

booWho(null);

// Capitilize letters in String
// first char of each word must be upper case, rest lower case
function titleCase(str) {
  // split str in to arrays
  str = str.toLowerCase().split(' ')
  // set every index of arr to lower case
  // loop through the arr and set the first char to upper case
  for(let i =0; i< str.length; i++){
  str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1);
  /* Here str.length = 5
    1st iteration: str[0] = str[0].charAt(0).toUpperCase() + str[0].slice(1);
                   str[0] = "i'm".charAt(0).toUpperCase()  + "i'm".slice(1);
                   str[0] = "I"                            + "'m";
                   str[0] = "I'm";
    2nd iteration: str[1] = str[1].charAt(0).toUpperCase() + str[1].slice(1);
                   str[1] = "a".charAt(0).toUpperCase()    + "a".slice(1);
                   str[1] = "A"                            + "";
                   str[1] = "A";
    3rd iteration: str[2] = str[2].charAt(0).toUpperCase()   + str[2].slice(1);
                   str[2] = "little".charAt(0).toUpperCase() + "little".slice(1);
                   str[2] = "L"                              + "ittle";
                   str[2] = "Little";
    4th iteration: str[3] = str[3].charAt(0).toUpperCase() + str[3].slice(1);
                   str[3] = "tea".charAt(0).toUpperCase()  + "tea".slice(1);
                   str[3] = "T"                            + "ea";
                   str[3] = "Tea";
    5th iteration: str[4] = str[4].charAt(0).toUpperCase() + str[4].slice(1);
                   str[4] = "pot".charAt(0).toUpperCase() + "pot".slice(1);
                   str[4] = "P"                           + "ot";
                   str[4] = "Pot";                                                         
    End of the FOR Loop*/
  }
  // return the arr as strings
  return str.join(' ');
}

titleCase("I'm a little tea pot");

// Slice and Splice
// You are given two arrays and an index.
// Copy each element of the first array into the second array, in order.
// Begin inserting elements at index n of the second array.
// Return the resulting array. The input arrays should remain the same after the function runs.
// frankenSplice([1, 2], ["a", "b"], 1) should return ["a", 1, 2, "b"]

function frankenSplice(arr1, arr2, n) {
  // place holder var for arr2
  let newArr = arr2.slice()
  // loop through arr 1 and use splice to add them into arr 2
  for(let i=0; i < arr1.length; i++){
    newArr.splice(n,0,arr1[i]);
    // make sure to increament n
    n++;
  }
  // return arr2 place holder var
  return newArr;
}

console.log(frankenSplice([1, 2, 3], [4, 5, 6], 1));



