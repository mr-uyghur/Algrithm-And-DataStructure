# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution(object):
    def productExceptSelf(self, nums):
        #from the current index
        #calculate its left product ie prefix
        #calculate its right product ie postfix
        #return the product output

        ans=[1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        postfix = 1
        #start from the back to the beginning of the arr list
        for i in range(len(nums) - 1,-1,-1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
    
#this solution passes all test cases on leet code
#beat 91% of python solutions
print(Solution().productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(Solution().productExceptSelf([-1,1,0,-3,3])) #[0,0,9,0,0]
print(Solution().productExceptSelf([1,2,3,4])) # [24, 12, 8, 6]
print(Solution().productExceptSelf([-1,1,0,-3,3])) # [0, 0, 9, 0, 0]
print(Solution().productExceptSelf([5])) # [1]
print(Solution().productExceptSelf([2,2,3,4])) # [24, 24, 16, 12]
print(Solution().productExceptSelf([0, 0])) # [0, 0]
print(Solution().productExceptSelf([-2, -1, -3])) # [3, 6, 2]
print(Solution().productExceptSelf([1, -1, 1, -1])) # [-1, 1, -1, 1]
