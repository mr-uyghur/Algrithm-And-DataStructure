let array1 = ['a', 'b', 'c','x']
let array2 = ['z','y', 'a']

function containsCommonItem(arr1, arr2){
    // use for loop to add values
    // place holder var
    let map = {};
    for(let i = 0; i < arr1.length ; i++){
        // check if property exists
        if(!map[array1[i]]){
            const item = array1[i];
            map[item] = true
        }
    }
    // loop through the second array and chekc if item in arr2 already exist in object
    for(let j =0; j < arr2.length; j++){
        if(map[array2[j]]){
            return true
        }
    }
    return false
}
console.log(containsCommonItem(array1, array2))
// o(a+b) better than nested loop in terms of time complexity

// same function with built in method
function containsCommonItem2(arr1, arr2){
    return arr1.some(item => arr2.includes(item))
}
console.log(containsCommonItem2(array1,array2))

