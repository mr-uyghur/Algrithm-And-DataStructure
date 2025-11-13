# Two Sum
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
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #store the given intergers into a dict
        # int : index
        #loop thru the given integers.
        #find currentNum - target value from the hashmap
        #store the index of 2 numbers into an array, 
        #return the array
        numsDict = {}
        for i, num in enumerate(nums):
            current = target - num
            if current in numsDict:
                return [numsDict[current], i]
            numsDict[num] = i


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Example 1
    result = sol.twoSum([2, 7, 11, 15], 9)
    assert set(result) == {0, 1}, f"Test 1 Failed, got {result}"
    print("✓ Test 1 Passed: [2,7,11,15] target=9 -> indices [0,1]")

    # Test 2: Example 2
    result = sol.twoSum([3, 2, 4], 6)
    assert set(result) == {1, 2}, f"Test 2 Failed, got {result}"
    print("✓ Test 2 Passed: [3,2,4] target=6 -> indices [1,2]")

    # Test 3: Example 3 - duplicate values
    result = sol.twoSum([3, 3], 6)
    assert set(result) == {0, 1}, f"Test 3 Failed, got {result}"
    print("✓ Test 3 Passed: [3,3] target=6 -> indices [0,1]")

    # Test 4: Negative numbers
    result = sol.twoSum([-1, -2, -3, 5, 10], 7)
    assert set(result) == {2, 4}, f"Test 4 Failed, got {result}"
    print("✓ Test 4 Passed: Negative numbers with positive target")

    # Test 5: Mix of positive and negative
    result = sol.twoSum([0, -1, 2, -2], 0)
    assert set(result) == {2, 3}, f"Test 5 Failed, got {result}"
    print("✓ Test 5 Passed: [0,-1,2,-2] target=0 -> sum of -2 and 2")

    # Test 6: Large numbers
    result = sol.twoSum([1000000000, 500000000, 200000000], 1500000000)
    assert set(result) == {0, 1}, f"Test 6 Failed, got {result}"
    print("✓ Test 6 Passed: Large positive numbers")

    # Test 7: Minimum array size (2 elements)
    result = sol.twoSum([5, 1], 6)
    assert set(result) == {0, 1}, f"Test 7 Failed, got {result}"
    print("✓ Test 7 Passed: Minimum size array (2 elements)")

    # Test 8: Zero target with positive/negative pair
    result = sol.twoSum([5, -5], 0)
    assert set(result) == {0, 1}, f"Test 8 Failed, got {result}"
    print("✓ Test 8 Passed: Zero target")

    # Test 9: Target at beginning and end
    result = sol.twoSum([1, 2, 3, 4, 5], 9)
    assert set(result) == {3, 4}, f"Test 9 Failed, got {result}"
    print("✓ Test 9 Passed: [1,2,3,4,5] target=9 -> 4+5")

    # Test 10: Single digit numbers
    result = sol.twoSum([1, 1, 1, 2], 3)
    assert set(result) == {2, 3}, f"Test 10 Failed, got {result}"
    print("✓ Test 10 Passed: Multiple 1s with target=3")

    print("\n✅ All 2Sum tests passed!")
