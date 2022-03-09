// Falsy Bouncer
// Remove all falsy values from an array.
// Falsy values in JavaScript are false, null, 0, "", undefined, and NaN.

function bouncer(arr) {
    // place holder var for arr
    let newArr = []
    // loop through arr and replace the false 
    for(let i =0; i<arr.length; i++){
      // check if index of arr has value
      if (arr[i]){
        newArr.push(arr[i]);
      } 
    }
    return newArr
  }
  
  bouncer([7, "ate", "", false, 9]);


// Where do I Belong
// Return the lowest index at which a value (second argument) should be inserted into an array (first argument) once it has been sorted. 
// The returned value should be a number.
// For example, getIndexToIns([1,2,3,4], 1.5) should return 1 because it is greater than 1 (index 0), 
// but less than 2 (index 1).
// Likewise, getIndexToIns([20,3,5], 19) should return 2
//  because once the array has been sorted it will look like [3,5,20] and 19 is less than 20 (index 2) and greater than 5 (index 1).

function getIndexToIns(arr, num) {
    // first sort num of arrays from low to high
    arr.sort((a, b) => a - b);
    // loop through the sorted arr and compare it with num
    for(let i=0;i < arr.length; i++){
      // return that index if it is greater or equal to num
      if(num <= arr[i]){
        return i
      }
    }
    return arr.length
  }
  getIndexToIns([40, 60], 50);

// Mutations
// For example, ["hello", "Hello"], should return true
//  because all of the letters in the second string are present in the first, ignoring case.
// The arguments ["hello", "hey"] should return false
//  because the string "hello" does not contain a "y".
// Lastly, ["Alien", "line"], should return true 
// because all of the letters in "line" are present in "Alien".
function mutation(arr) {
    // turn the strings inside the arr to lower case
    let test = arr[1].toLowerCase();
    let target = arr[0].toLowerCase();
    // loop through testcharacters
    for(let i =0; i<test.length; i++){
      // if any of them is not found we return false.
      if(target.indexOf(test[i]) < 0){
        return false;
      }
    }
    return true;
  }
  mutation(["hello", "hey"]);

// Chunky Monkey
// chunkArrayInGroups(["a", "b", "c", "d"], 2) 
// should return [["a", "b"], ["c", "d"]]
// chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2) 
// should return [[0, 1], [2, 3], [4, 5]].
function chunkArrayInGroups(arr, size) {
    // a place holder var for arrays
    let newArr = []
    // loop through arr , increase index by size,I can use size to slice my newArr
    for(let i=0; i < arr.length ; i+=size){
      // push the arr to newArr till size by using slice
      // it loops from the size index again and push it into newArr
      newArr.push(arr.slice(i, i + size));
    }
    return newArr;
  }
  chunkArrayInGroups(["a", "b", "c", "d"], 2);