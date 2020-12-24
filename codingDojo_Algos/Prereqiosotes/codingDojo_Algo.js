// Print 1-255

for(let i = 1; i <= 255; i++){
console.log(i);
}

// Write a program that would print all the odd numbers from 1 to 1000
for(let i = 1; i <=1000; i++){
if(i % 2 !=0){
console.log(i);
}
}

// Write a program that would print the sum of all the odd numbers from 1 to 5000
let sum = 0;
for(let i =1; i<=5000; i++){
    sum += i;
}
console.log(sum);

// Iterating Through the Array
let arr = [1,3,5,7,9,13];
for(num in arr){
    console.log(num);
}

// Find Max
let arr = [-3, 3, 5, 7];
let max = arr[0]

for(let i = 0; i<=arr.length; i++){
if(arr[i] > max){
max = arr[i]
}
}
console.log(max)

// Find Average
let arr = [1,2,3]
let sum = 0;
let avg = 0;
for(let i=0; i < arr.length; i++){
    // add each num in arr 
    sum += arr[i]
}
avg = (sum / arr.length)
console.log(avg)

// Array With Odd Numbers
let arr = [];
for(let i =1; i<=255;i++){
if(i % 2 !=0){
    arr.push(i)
}
}
console.log(arr)

//  Greater Than Y
let array = [1,3, 5, 7];
let y = 3;
let count = 0
for(let i=0; i<=array.length; i++){
if(array[i] > y){
count++;
}
}
console.log(count)