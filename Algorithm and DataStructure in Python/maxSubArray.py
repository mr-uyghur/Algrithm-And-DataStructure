# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #create place holder for current sum and the max sum
        currentSum = nums[0]
        maxSum = nums[0]
        #iterate thru the list
        #keep track of the maximum current sum 
        #and keep track of max sum over all
        #iteration starts from the 2nd index bc the currentSum and maxSum are set equal to the first index
        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)
        #return the max sum we get after the loop
        return maxSum

#this solution passes all leet code test cases
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6
print(Solution().maxSubArray([1])) #1
print(Solution().maxSubArray([5,4,-1,7,8])) #23

print(Solution().maxSubArray([-1, -2, -3, -4])) # -1
print(Solution().maxSubArray([0, -1, 2, -3, 4])) # 4
print(Solution().maxSubArray([2, -1, 2, 3, -9, 4, -2, -3, 5, 1])) # 6
print(Solution().maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3])) # 7
print(Solution().maxSubArray([8, -19, 5, -4, 20])) # 21
