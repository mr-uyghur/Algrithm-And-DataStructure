// Bubble Sort

let list = [6,5,3,1,8,7,2,4]

function bubbleSort(nums){
    let counter = 0
    for(let i=0; i < nums.length; i++){ //
        //compare values inside the nested forloop
        for(let j=0; j < nums.length; j++){ //
            if(nums[j] > nums[j+1]){
                //swap values 
                let temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                counter++
            }
        }
    }
    console.log(counter)
    return nums
}
console.log(bubbleSort(list))