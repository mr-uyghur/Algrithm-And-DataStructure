// Merging Sorted Array, the given arrays are sorted 
function mergeSortedArray(arr1,arr2){
    // check input
    if(!arr1 || !arr2 ){
        return "hmm inputs needs to be arrays"
    }
    if(arr1.length === 0){
        return arr2
    }
    if(arr2.length === 0){
        return arr1
    }
    // concat 2 given arrays and sorted them after
    return arr1.concat(arr2).sort((a, b) => a - b)
}
console.log(mergeSortedArray([0,3,4,31],[4,6,30]))

// Merge sorted arrays
function mergeSortedArray2(array1,array2){
    // check inputs first
    if(array1.length === 0){
        return array2
    }
    if(array2.length === 0){
        return array1
    }
    // place holders vars for new array
    let newArray = []
    let arrayItem1 = array1[0]
    let arrayItem2 = array2[0]
    let i = 1
    let j = 1
    // loop through both arrays
    // place the smaller value of num in front
    while(arrayItem1 || arrayItem2){
        if( arrayItem2 === undefined ||arrayItem1 < arrayItem2){
            newArray.push(arrayItem1);
            // update arrayItem's index
            arrayItem1 = array1[i]
            i++;
        }   else {
            newArray.push(arrayItem2);
            arrayItem2 = array2[j]
            j++
        }
    }
    return newArray
}
console.log(mergeSortedArray2([0,3,4,31], [3,4,6,30]))




