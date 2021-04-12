//selection sort 
//this algo works by targetting the smallest item in the list and putting them in order of min to max.
const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function selectionSort(items){
    for(let i=0; i<items.length;i++){ //
        // set current index as min 
        let minIndex = i 
        for(let j=i+1; j < items.length; j++){ //
            if(items[j] < items[minIndex]){
                minIndex = j
            }
            if(minIndex !== i){
                let temp = items[i]
                items[i] = items[minIndex]
                items[minIndex] = temp
            }
        }
    }
    return items
}

console.log(selectionSort(numbers))