# 35. Search Insert Position
# Easy
# 14.4K
# 619
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right= 0, len(nums)-1
        while left <= right:
            mid = (left + right)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left

print(Solution().searchInsert([1,3,5,6],5))
print(Solution().searchInsert([1,3,5,6],2))
print(Solution().searchInsert([1,3,5,6],7))
