// bubble sort

let arr = [3, 2, 9, 6, 5]
// should return 2,3,5,6,9 
function bubble(nums) {
    // place holder array as result
    for (let i = 0; i < nums.length; i++) {
        console.log("this is i" + nums[i])
        for (let j = 0; j < nums.length; j++) {
            console.log("this is j" + nums[j])
            if (nums[j] > nums[j + 1]) {
                let temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

            }
        }
    }
    return nums
}

console.log(bubble(arr))

// selection sort
let arr = [42, 23, 4, 16, 8, 15]
function selection(nums) {

    for (let i = 0; i < nums.length - 1; i++) {
        let minIndex = i
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[j] < nums[minIndex]) {
                minIndex = j
            }

        }
        if (minIndex !== i) {
            let temp = nums[i];
            nums[i] = nums[minIndex];
            nums[minIndex] = temp;
        }
    }

    return nums
}

console.log(selection(arr))

// insertion sort
let arr = [42, 23, 4, 16, 8, 15]

function insertion(nums) {

    let sorted = []
    for (let i = 1; i <= nums.length - 1; i++) {
        element = nums[i]
        j = i
        while (j > 0 && nums[j - 1] > element) {
            nums[j] = nums[j - 1]
            j = j - 1

        }
        nums[j] = element
    }
    return nums
}
console.log(insertion(arr))

// merge sort
function merge(left, right) {
    let arr = []
    // Break out of loop if any one of the array gets empty
    while (left.length && right.length) {
        // Pick the smaller among the smallest element of left and right sub arrays 
        if (left[0] < right[0]) {
            arr.push(left.shift())
        } else {
            arr.push(right.shift())
        }
    }

    // Concatenating the leftover elements
    // (in case we didn't go through the entire left or right array)
    return [...arr, ...left, ...right]
}

function mergeSort(array) {
    const half = array.length / 2

    // Base case or terminating case
    if (array.length < 2) {
        return array
    }

    const left = array.splice(0, half)
    return merge(mergeSort(left), mergeSort(array))
}

array = [4, 8, 7, 2, 11, 1, 3];
console.log(mergeSort(array));