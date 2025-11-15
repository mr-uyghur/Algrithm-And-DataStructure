# #Two Sum II - Input Array Is Sorted
# Medium
# Topics
# Companies
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Constraints:

# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Since the given array is sorted use 2 pointer approach.
        #left pointer = index 0, right pointer = last index
        #move 2 pointers inward till we find the sum == target
        #return the index with +1
        left = 0
        right = len(numbers) - 1

        while left < right:
            #pointers inward based on whether the current sum is too small or too large
            #if the sum is greater than target, move right pointer left
            #if the sum is less than target, move left pointer right
            #if the sum is equal to target, return the indexes +1
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] == target:
                return [left+1, right +1]
            
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2], "Test 1 Failed"
    print("✓ Test 1 Passed: [2,7,11,15], target=9 -> [1,2]")

    # Example 2
    assert sol.twoSum([2, 3, 4], 6) == [1, 3], "Test 2 Failed"
    print("✓ Test 2 Passed: [2,3,4], target=6 -> [1,3]")

    # Example 3
    assert sol.twoSum([-1, 0], -1) == [1, 2], "Test 3 Failed"
    print("✓ Test 3 Passed: [-1,0], target=-1 -> [1,2]")

    # Test 4: duplicates sum to target
    assert sol.twoSum([1, 2, 3, 4, 4, 9], 8) == [4, 5], "Test 4 Failed"
    print("✓ Test 4 Passed: [1,2,3,4,4,9], target=8 -> [4,5]")

    # Test 5: duplicate first two
    assert sol.twoSum([1, 1, 2, 3], 2) == [1, 2], "Test 5 Failed"
    print("✓ Test 5 Passed: [1,1,2,3], target=2 -> [1,2]")

    # Test 6: two elements only
    assert sol.twoSum([1, 2], 3) == [1, 2], "Test 6 Failed"
    print("✓ Test 6 Passed: [1,2], target=3 -> [1,2]")

    # Test 7: negative pair
    assert sol.twoSum([-4, -3, -2, -1], -5) == [1, 4], "Test 7 Failed"
    print("✓ Test 7 Passed: [-4,-3,-2,-1], target=-5 -> [1,4]")

    # Test 8: mid indices
    assert sol.twoSum([-3, -1, 0, 1, 2], 1) == [2, 5], "Test 8 Failed"
    print("✓ Test 8 Passed: [-3,-1,0,1,2], target=1 -> [2,5]")

    # Test 9: zeros
    assert sol.twoSum([0, 0, 1, 2], 0) == [1, 2], "Test 9 Failed"
    print("✓ Test 9 Passed: [0,0,1,2], target=0 -> [1,2]")

    print("\n✅ All 2Sum II tests passed!")
        
