// bubble sort

let arr = [3,2,9,6,5]
// should return 2,3,5,6,9 
function bubble(nums){
    // place holder array as result
    for(let i=0; i<nums.length; i++){
        console.log("this is i" + nums[i])
        for(let j=0; j<nums.length;j++){
            console.log("this is j" + nums[j])
            if(nums[j] > nums[j+1]){
                let temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                
            }
        }
    }
    return nums
}

console.log(bubble(arr))

// selection sort
let arr = [42,23,4,16,8,15]
function selection(nums){

    for(let i =0; i<nums.length-1; i++){
        let minIndex = i
        for(let j=i+1; j<nums.length; j++){
            if(nums[j] < nums[minIndex]){
                minIndex = j
            }

        }
        if(minIndex !== i){
            let temp = nums[i];
			nums[i] = nums[minIndex];
			nums[minIndex] = temp;
        }
    }

    return nums
}

console.log(selection(arr))

// insertion sort
let arr = [42,23,4,16,8,15]

function insertion(nums){
    
    let sorted = []
    for(let i=1; i <= nums.length-1;i++){
        element = nums[i]
        j = i
        while(j> 0 && nums[j-1] > element){
            nums[j] = nums[j-1]
            j = j - 1 

        }
        nums[j] = element
    }
    return nums
}
console.log(insertion(arr))