# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #use brute force to find the indexes
        for i in range(0,len(nums)):
            #use i + 1, always point j next to i's index
            for j in range(i+1,len(nums)):
                if target - nums[i] == nums[j]:
                    return [i,j]
        


print(Solution().twoSum([3,2,4],6))
print(Solution().twoSum([2,7,11,15],9))
print(Solution().twoSum([3,3],6))
print(Solution().twoSum([1, 5, 3, 7], 8))  # Test with a pair that adds up to 8
print(Solution().twoSum([10, 22, 5, 75, 65, 80], 90))  # Test with larger numbers and a pair that adds up to 90
print(Solution().twoSum([-1, -2, -3, -4, -5], -8))  # Test with negative numbers
print(Solution().twoSum([5, 25, 75], 100))  # Test with exact match at the end
print(Solution().twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19))  # Test with a sequence of numbers
