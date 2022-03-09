// Implement map on a Prototype
var s = [23, 65, 98, 5];
// code bwlow is basically how .map works under the hood
Array.prototype.myMap = function(callback) {
  var newArray = [];
  
  this.forEach(item =>
  newArray.push(callback(item))
  )
 
  return newArray;
};
var new_s = s.myMap(function(item) {
  return item * 2;
});

// Implement the filter Method on a PrototypePassed
// code below shows how .filter method works under the hood
var s = [23, 65, 98, 5];
Array.prototype.myFilter = function(callback) {
//   Place holder var for array
  var newArray = [];
//   loop through each item assigned to this method
  this.forEach(function(item){
    //   if the call back item is true for the condition
    if(callback(item) == true){
        // push that item in the array
      newArray.push(item)
    }
  })
// return the arr
  return newArray;
};

var new_s = s.myFilter(function(item) {
  return item % 2 === 1;
});

// Combine Two Arrays Using the concat Method
// concat method overview 
function nonMutatingConcat(original, attach) {
 
return original.concat(attach);

}
var first = [1, 2, 3];
var second = [4, 5];
nonMutatingConcat(first, second);

// for the squareList function using any combination of map(), filter(), and reduce()
//  so that it returns a new array containing only the square of only the positive integers (decimal numbers are not integers) 
// squareList([4, 5.6, -9.8, 3.14, 42, 6, 8.34, -2]) should return [16, 1764, 36].

const squareList = arr => {
  // use filter method to find positive integers
  let nums = arr.filter(num => num > 0 && num % parseInt(num) === 0)
  // user map to store them in an array
  let data = nums.map(num => num*num)
  
  return data;
  // Only change code above this line
};
const squaredIntegers = squareList([-3, 4.8, 5, 3, -3.2]);
console.log(squaredIntegers);