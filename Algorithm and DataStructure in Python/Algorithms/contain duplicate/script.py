# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false


def containsDuplicate( nums):
    return len(nums) != len(set(nums))

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

#hashing approach

def containsDuplicate2( nums):
    container = {}
    
    for num in nums:
        if num not in container:
            container[num] = 0
        container[num] += 1
    
    for num, data in container.items():
        if data > 1:
            return True
        return False
    
print(containsDuplicate2([1,2,3,4]))

print(containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))
