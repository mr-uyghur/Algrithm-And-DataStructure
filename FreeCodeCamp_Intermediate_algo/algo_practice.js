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