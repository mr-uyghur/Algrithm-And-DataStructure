// Insertion Sort

const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function insertionSort(array) {
    const length = array.length
    for(let i =0; i < length; i++){
        // if the item we're looping is less than first item 
        if(arr[i] < arr[0]){
            //move that item(use unshift mathod) in the first index of that array with unshift
            array.unshift(array.splice(i,1)[0])
        }
        //otherwise if the item we're looping is not less than the first item'
        else {
            //findout where the number should go
            for(let j=1; j < i; j++){
                if(arr[i] > arr[j-1] && arr[i] < arr[j]){
                    //move number to the right index with splice
                    array.splice(j,0,array.splice(i,1)[0])
                }
            }
        }
    }
}