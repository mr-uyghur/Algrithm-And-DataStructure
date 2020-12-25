// Square the Values
// [1,5, 10, -2] should return  [1, 25, 100, 4]

let arr = [1,5, 10, -2]
// loop through each index of arr and multiply by itself
for(let i=0; i<arr.length; i++){
console.log(arr[i] * arr[i])
}
// return place holder var

// Negative Numbers
// Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that replaces any negative number with the value of 0.
//   When the program is done x should have no negative values (e.g. [1, 5, 10, 0]).

let arr = [1,5, 10, -2];
// loop through the array and look for number less than 0
// replace that index of arr with 0 inside the loop
for(var i=0;i<arr.length; i++){
    if(arr[i] < 0){
        arr[i] = 0;
    }
}
console.log(arr) 

// Max, Min, and Average
// Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that prints the maximum number in the array,
//  minimum value in the array as well as the average values in the array. 
let x = [1,5, 10, -2]
// place holder var for the data 
let sum = 0
let data = {
    max:x[0],
    min:x[0],
}
// loop through x and use if and else if to find Max min and avg
for(let i=0; i<x.length; i++){
    sum += x[i]
    if(x[i] > data.max){
        data.max = x[i]
    } else if(x[i] < data.min){
        data.min = x[i]
    }
   
}
let avg  = sum / x.length
console.log("the max is: " + data.max,
 "the min num is: " + data.min, 
 "the average is " + avg)
