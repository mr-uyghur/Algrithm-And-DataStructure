# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1


class Solution(object):
    def search(self, nums, target):
        #use binary search to find the target from nums list
        #we need O(log n) runtime complexity
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]

            if mid_val == target:
               # print(mid_val)
                return mid 

            elif nums[left] <= mid_val:
                if nums[left] <= target and mid_val >= target:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target and mid_val <= target:
                    left = mid + 1
                else:
                    right = mid -1

        return -1


print(Solution().search([4,5,6,7,0,1,2],0))
print(Solution().search([4,5,6,7,0,1,2],3))
print(Solution().search([1],0))
print(Solution().search([9,12,17,2,4,5], 17))  # Test case with target present in a larger rotated array
print(Solution().search([9,12,17,2,4,5], 6))   # Test case with target not present in a larger rotated array
print(Solution().search([1,2,3,4,5,6,7], 5))   # Test case with target present in a non-rotated sorted array
print(Solution().search([1,2,3,4,5,6,7], 0))   # Test case with target not present in a non-rotated sorted array
            # Test case with a single-element array where the target does not match the element

    
