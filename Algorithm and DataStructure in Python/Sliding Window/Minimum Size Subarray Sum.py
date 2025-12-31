# 209. Minimum Size Subarray Sum
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #use sliding window approach
        #while sum >= target shrink the wirodw from the left
        #make the window as small as possible to keep the best length
        #return the min length of the window
        #return 0 if we can't reach the target from the given input

        left = 0
        curr_sum = 0
        best_len = len(nums) + 1

        #for loop logic
        #expand the window by moving right pointer
        #whenever curr_sum >= target shrink the window from the left
        for right in range(len(nums)):
            curr_sum += nums[right] #expand the window

            while curr_sum >= target:
                best_len = min(best_len, right - left+1)
                curr_sum -= nums[left]
                left += 1
        if best_len == len(nums) +1:
            return 0
        return best_len

        


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.minSubArrayLen(7, [2,3,1,2,4,3]) == 2, "Test 1 Failed"
    print("✓ Test 1 Passed: target=7, nums=[2,3,1,2,4,3] -> 2")

    # Example 2
    assert sol.minSubArrayLen(4, [1,4,4]) == 1, "Test 2 Failed"
    print("✓ Test 2 Passed: target=4, nums=[1,4,4] -> 1")

    # Example 3
    assert sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0, "Test 3 Failed"
    print("✓ Test 3 Passed: target=11, nums=[1,1,1,1,1,1,1,1] -> 0")

    # Additional tests
    assert sol.minSubArrayLen(15, [1,2,3,4,5]) == 5, "Test 4 Failed"
    print("✓ Test 4 Passed: target=15, nums=[1,2,3,4,5] -> 5")

    assert sol.minSubArrayLen(100, [1,2,3]) == 0, "Test 5 Failed"
    print("✓ Test 5 Passed: target=100, nums=[1,2,3] -> 0")

    assert sol.minSubArrayLen(3, [3]) == 1, "Test 6 Failed"
    print("✓ Test 6 Passed: target=3, nums=[3] -> 1")

    assert sol.minSubArrayLen(1, [1]) == 1, "Test 7 Failed"
    print("✓ Test 7 Passed: target=1, nums=[1] -> 1")

    print("\n✅ All Minimum Size Subarray Sum tests passed!")





