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