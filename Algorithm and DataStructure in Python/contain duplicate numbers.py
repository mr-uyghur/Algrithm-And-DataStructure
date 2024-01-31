# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) <= 1:
            return False
        #this prob we can store the input in a dictionary (hashmap)
        #keep track of each occurance of the element
        #return true only if the value of all elements in hashmap is > 1
        #otherwise return false
        
        data = {}

        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        print(data)

        #this block of code checks if all the values in the hashmap is great than 1
        #that way we know there are duplicare elements
        for value in data.values():
            if value != 1:
                return True
        return False

# this solution passes all leetcode test cases
print(Solution().containsDuplicate([1,2,3,1]))  #True
print(Solution().containsDuplicate([1,2,3,4]))  #False 
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  #True

#solving the same question with different logic, here we're using sets

class Solution(object):
    def containsDuplicate2(self, nums):
        #store the input into sets
        #sets can't contain duplicate elements
        #if the length of the set and nums are not the same 
        #return True, bc it means there are duplicate items
        #otherwise False
        if len(nums) <= 1:
            return False
        my_set = set(nums)
        print(my_set)
        if len(nums) != len(my_set):
            return True
        return False
    
#this solution passes all leetcode test cases
print(Solution().containsDuplicate2([]))  # False (Empty list, no duplicates)
print(Solution().containsDuplicate2([5]))  # False (Single element, no duplicates)
print(Solution().containsDuplicate2([2, 2]))  # True (All elements are duplicates)
print(Solution().containsDuplicate2([1, 3, 5, 7, 9, 1]))  # True (1 is repeated)
print(Solution().containsDuplicate2([10, 20, 30, 40]))  # False (All elements are unique)
print(Solution().containsDuplicate2([1, 2, 2, 3, 4, 5]))  # True (2 is repeated)
print(Solution().containsDuplicate2([-1, -2, -3, -1]))  # True (Negative numbers, -1 is repeated)
print(Solution().containsDuplicate2([1, 1, 1, 1, 1, 1]))  # True (All elements are the same)