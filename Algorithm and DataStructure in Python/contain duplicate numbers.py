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

#this solution passes all leetcode test cases
print(Solution().containsDuplicate([1,2,3,1]))  #True
print(Solution().containsDuplicate([1,2,3,4]))  #False 
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  #True
