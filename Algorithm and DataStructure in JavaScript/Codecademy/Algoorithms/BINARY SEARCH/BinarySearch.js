//iterative
const binarySearch = (arr, target) => {
    //set 2 pointers, left and right pointers
    //pointer left points to the first index in the window 
    //pointer right points to the last index
    let left = 0;
    let right = arr.length

    //condition is as long the value of right pointer is larger than the left the loop continues
  while (right > left) {
      //grab the index index of the array, 
      //use that index to compare that value with target
      let indexToCheck = Math.floor((right + left) / 2)
      let midPoint = arr[indexToCheck]
      console.log(midPoint)

      if(midPoint === target) {
        return indexToCheck
      } else if(midPoint < target) {
        left = indexToCheck + 1
      } else {
        right = indexToCheck
      }
  }

  return null;
};

const searchable = [1, 2, 7, 8, 22, 28, 41, 58, 67, 71, 94];
const target = 94;

targetIndex = binarySearch(searchable, target);

console.log(`The target index is ${targetIndex}.`);

module.exports = binarySearch;