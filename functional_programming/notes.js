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