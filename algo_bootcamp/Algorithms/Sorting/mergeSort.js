// Merge Sort 
//take a list and take them in half
//take each sub list and divide them in half again till we have 1 item 
// once we have them divided up then compare those values and sort them out into sublists 

const numbers = [99,44,6,2,1,5,63,87,283,4,0];

function mergeSort(array) {
    if(array.length === 1) {
        return array
    }
    // Split Array in into right and left
    const half = Math.floor(array.length /2)
    const left = array.slice(0, half)
    const right = array.slice(half)
    
    return merge(
        mergeSort(left),
        mergeSort(right)
    )
}

function merge(left,right) {
    let arr = []
    while(left.length && right.length){
        if(left[0] < right[0]){
            arr.push(left.shift())
        } else {
            arr.push(right.shift())
        }
    }

    return [...arr, ...left, ...right]
}

console.log(mergeSort(numbers))

