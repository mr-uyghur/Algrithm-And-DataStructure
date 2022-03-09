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

//  Shifting the values in the array
// Given an array x (e.g. [1,5, 10, 7, -2]), create an algorithm (sets of instructions) that shifts each number by one (to the front). 
//  For example when the program is done x (assuming it was [1,5,10,7,-2])
//  should become [5,10,7,-2, 0].  

let x = [1,5,10,7,-2]
// place holder var for my new array
let newArr = []
// loop through x from beginning to end and shify index
for(let i =0; i < x.length; i++){
    newArr.push(x[i+1])
}
newArr[x.length-1] = 0
console.log(newArr)

// Number to String
// Write a program that takes an array of numbers and replaces any number that's negative to a string called 'Dojo'.
//  For example if array = [-1, -3, 2] after your program is done
//   array should be ['Dojo', 'Dojo', 2].

let x = [-1, -3, 2]
console.log(x)
// loop through arr x and use if statement to change index value below 0
for(let i = 0; i < x.length; i++){
    if(x[i] < 0){
        x[i] = "Dojo"
    }
}
console.log(x)

// Random Array
// Create an array X and fill the array with 10 values, 
// each value being a random integer between 0 to 100. 
//  For example when your program is done, X could be something like this: [35, 15, 3, 39, 53, 93, 25, 39, 59, 21].

// need a place holder arr
let arr = []
// loop from 0 to 9, and generate random num and add it to my array
for(let i = 0; i <= 9; i++) {
    arr[i] = Math.floor(Math.random() *101)
}
console.log(arr)

// Swapping two values
// Write a program that takes an array of numbers and returns an array where the first and last numbers in the array have been switched.
// For example say x = [2, 3, 5, 7, 6]. By the end of the program x,
//  should be [6, 3, 5, 7, 2]. Do this without creating an empty array.
let x = [2, 3, 5, 7, 6]
console.log(x)
let first = x[0]
let last = x[x.length - 1]
x[0] = last
x[x.length - 1] = first
console.log(x)

// Reversing
// Given an array X of multiple values (e.g. [-3,5,1,3,2,10]),
//  write a program that reverses the values in the array.  
//  Once your program is done X should be in the reserved order. 
//   Do this without creating a temporary array.  
//   Also, do NOT use the reverse method but find a way to reverse the values in the array 
//   (HINT: swap the first value with the last; second with the second to last and so forth).


let x = [-3,5,1,3,2,10,11,8]
for(let i=0; i< Math.floor(x.length/2); i++){
let temp = x[i]
x[i] = x[x.length -1 -i ]
x[x.length -1 -i] = temp
}
console.log(x)

// Assignment: Insert X in Y
// Write a program that inserts a new number X at an index Y. 
// For example if array = [1, 3, 5, 7] and X = 10, and Y = 2, 
// by the end of your program array should be [1, 3, 10, 5, 7] 
// (in other words we added '10' on index 2). 
// Check the output of your array once your program is completed to make sure it's working correctly.
let arr = [1, 3, 5, 7]
console.log(arr)
let x = 10
let y = 2
arr.splice(y,0,x)
console.log(arr)

// Removing Negatives
let list = [0, -1, 2, -3, 4, -5, 6]
// loop through list of arrays and user if statement to find negative numbers
// replace those negative numbers with the same positive numbers
let data = list.filter((num) => {
    return num > 0
})
console.log(data)