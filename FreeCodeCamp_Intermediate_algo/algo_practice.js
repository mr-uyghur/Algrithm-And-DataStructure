// Sum All Numbers in a Range
// For example, sumAll([4,1]) should return 10 because sum of all the numbers between 1 and 4 (both inclusive) is 10.
function sumAll(arr) {
    // find max and min number from the arr
    let min = Math.min(...arr)
    let max = Math.max(...arr)
    // a place holder var for sum of all
    let sum = 0
    // loop from min to max and add every num in between
    for(let i = min; i <= max; i++){
      sum += i;
    }
    // return placeholder var
    return sum;
  }
  
  console.log(sumAll([1, 4]));


//   Diff Two Arrays
// Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both.
//  In other words, return the symmetric difference of the two arrays.
// [1, 2, 3, 5], [1, 2, 3, 4, 5] should return [4].
  function diffArray(arr1, arr2) {
    //   placeholder var
    var newArr = []; 
    // merge 2 arrays and sort them from low to high
       var ordArr = arr1.concat(arr2).sort(); 
       console.log(ordArr)
    //loop through the ordered array and push to the empty newArr only the items that have not a twin in the ordered arr (only items that are not equal to the previous nor to the next item)
       for(var i=0; i<ordArr.length; i++) {
    //    check if the item in ordArr does not have the same value 
           if(ordArr[i] !== ordArr[i+1] && ordArr[i] !== ordArr[i-1]){
           newArr.push(ordArr[i]);
           }
       }
       return newArr;
    }
    
   console.log(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5])) ;

  //  Seek and Destroy
  // destroyer([1, 2, 3, 1, 2, 3], 2, 3) should return [1, 1].
  // destroyer([3, 5, 1, 2, 2], 2, 3, 5) should return [1].
  function destroyer(arr) {
    //  convert arguments into an array
    var args = Array.prototype.slice.call(arguments);
    
    // user nested for loop to loop through arr and then arguements
    for(let i =0; i< arr.length; i++){
      for(let j=0; j<args.length; j++){
        if(arr[i] === args[j]){
          delete arr[i]
        }
      }
    }
    return arr.filter(Boolean)
    }
    
    destroyer([1, 2, 3, 1, 2, 3], 2, 3);

    // Wherefore art thou
    function whatIsInAName(collection, source) {
      // save source keys in a var
      var srcKeys = Object.keys(source);
      // use filter to loop through each item in collection
      return collection.filter(function(obj) {
        // then loop through each item in the object
        for (var i = 0; i < srcKeys.length; i++) {
          // use a if statement to check if the object in the collection doesn’t have the key and the property value doesn’t match the value in source.
          if (
            !obj.hasOwnProperty(srcKeys[i]) ||
            obj[srcKeys[i]] !== source[srcKeys[i]]
          ) {
            return false;
          }
        }
        return true;
      });
    }
    
    whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });


    // Spinal Tap Case
    // spinalCase("This Is Spinal Tap") should return "this-is-spinal-tap".
    // spinalCase("The_Andy_Griffith_Show") should return "the-andy-griffith-show".
    // spinalCase("Teletubbies say Eh-oh") should return "teletubbies-say-eh-oh".
    function spinalCase(str) {
      // split the str with following conditions
  // a whitespace character [\s] is encountered
  // underscore character [_] is encountered
  // or is followed by an uppercase letter [(?=[A-Z])]
   let newWords = str.split(/\s|_|(?=[A-Z])/)
  //  convert the splitted arr in to str
    let words = newWords.join('-')
    // return the str with all lower cases
    return words.toLowerCase()
  }
  
  spinalCase('This Is Spinal Tap');


//  Pig Latin
// translatePigLatin("california") should return "aliforniacay".
//Should handle words where the first vowel comes in the middle of the word. 
// translatePigLatin("schwartz") should return "artzschway".
function translatePigLatin(str) {
  // create var for vowels
  let vowels = ['a', 'e', 'i', 'o', 'u'];
  // place holder var for new string
  let newStr = "";
    // check in the first char of str is a vowel
    // use the indexOf() method to check if the first character exists in our vowels array.
    if (vowels.indexOf(str[0]) > -1) {
        newStr = str + "way";
        return newStr;
    } else {
        let firstMatch = str.match(/[aeiou]/g) || 0;
        // The vowel variable will give us the index of the first vowel found in the string using indexOf().
        let vowel = str.indexOf(firstMatch[0]);
        newStr = str.substring(vowel) + str.substring(0, vowel) + "ay";
        return newStr;
    }
}
translatePigLatin("consonant");

// Search and Replace
// myReplace("Let us go to the store", "store", "mall")
//  should return "Let us go to the mall"
// myReplace("His name is Tom", "Tom", "john") should return "His name is John"
function myReplace(str, before, after) {
  //  find index whwere before is on str
  var index = str.indexOf(before)
  // verify if the first index is upper case
  if(str[index] === str[index].toUpperCase()){
  // if true change capitilize the after paramiter
   after = after.charAt(0).toUpperCase() + after.slice(1)
  } else{
    after = after.charAt(0).toLowerCase() + after.slice(1)
  }
  // replace the before arguement with after
  str = str.replace(before, after)
  return str
  }
  
  myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped");