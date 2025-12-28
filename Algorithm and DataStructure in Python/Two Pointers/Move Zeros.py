# 283. Move Zeroes
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
      # write points to the index where the next non-zero value should be placed
        # iterate through the array
        # if the current value is non-zero:
        #   copy it to the position indicated by write
        #   move write forward so the next non-zero goes after it
        # after all non-zero values are moved to the front,
        # fill the remaining positions in the array with zeros
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0
        

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic example
    arr = [0,1,0,3,12]
    solution.moveZeroes(arr)
    assert arr == [1,3,12,0,0], "Test 1 Failed"
    print("✓ Test 1 Passed: [0,1,0,3,12] -> [1,3,12,0,0]")

    # Test Case 2: Single zero
    arr = [0]
    solution.moveZeroes(arr)
    assert arr == [0], "Test 2 Failed"
    print("✓ Test 2 Passed: [0] -> [0]")

    # Test Case 3: Mixed zeros and non-zeros
    arr = [1,0,2,0,3]
    solution.moveZeroes(arr)
    assert arr == [1,2,3,0,0], "Test 3 Failed"
    print("✓ Test 3 Passed: [1,0,2,0,3] -> [1,2,3,0,0]")

    # Test Case 4: All zeros
    arr = [0,0,0]
    solution.moveZeroes(arr)
    assert arr == [0,0,0], "Test 4 Failed"
    print("✓ Test 4 Passed: [0,0,0] -> [0,0,0]")

    # Test Case 5: No zeros
    arr = [1,2,3]
    solution.moveZeroes(arr)
    assert arr == [1,2,3], "Test 5 Failed"
    print("✓ Test 5 Passed: [1,2,3] unchanged")

    # Test Case 6: Leading zero
    arr = [0,1]
    solution.moveZeroes(arr)
    assert arr == [1,0], "Test 6 Failed"
    print("✓ Test 6 Passed: [0,1] -> [1,0]")

    # Test Case 7: Complex mix
    arr = [4,2,4,0,0,3,0,5]
    solution.moveZeroes(arr)
    assert arr == [4,2,4,3,5,0,0,0], "Test 7 Failed"
    print("✓ Test 7 Passed: complex mix moved correctly")

    # Test Case 8: Not enough nonzeros
    arr = [0,1,0,0,2]
    solution.moveZeroes(arr)
    assert arr == [1,2,0,0,0], "Test 8 Failed"
    print("✓ Test 8 Passed: [0,1,0,0,2] -> [1,2,0,0,0]")

    # Test Case 9: Negative numbers preserved
    arr = [0,-1,0,2]
    solution.moveZeroes(arr)
    assert arr == [-1,2,0,0], "Test 9 Failed"
    print("✓ Test 9 Passed: negatives handled correctly")

    # Test Case 10: Empty array (edge)
    arr = []
    solution.moveZeroes(arr)
    assert arr == [], "Test 10 Failed"
    print("✓ Test 10 Passed: empty array handled")

    print("\n✅ All Move Zeroes tests passed!")
        