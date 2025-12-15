

# 80. Remove Duplicates from Sorted Array II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.





from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #keep track of dups appear more than twice
        k = 0
        #interate thru the array list.
        # for each num in nums
        #if k<2 or x!=nums[k-2]
        #nums[k] = num, k+=1
        #return k
        for i in range(0, len(nums)):
            if k<2 or nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
            

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums = [1,1,1,2,2,3]
    k = sol.removeDuplicates(nums)
    assert k == 5, f"Test 1 Failed: expected k=5, got {k}"
    assert nums[:k] == [1,1,2,2,3], f"Test 1 Failed: expected [1,1,2,2,3], got {nums[:k]}"
    print("✓ Test 1 Passed: [1,1,1,2,2,3] -> k=5")

    # Example 2
    nums = [0,0,1,1,1,1,2,3,3]
    k = sol.removeDuplicates(nums)
    assert k == 7, f"Test 2 Failed: expected k=7, got {k}"
    assert nums[:k] == [0,0,1,1,2,3,3], f"Test 2 Failed: expected [0,0,1,1,2,3,3], got {nums[:k]}"
    print("✓ Test 2 Passed: [0,0,1,1,1,1,2,3,3] -> k=7")

    # Test 3: single element
    nums = [5]
    k = sol.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [5], f"Test 3 Failed: got k={k}, nums={nums[:k]}"
    print("✓ Test 3 Passed: single element")

    # Test 4: already valid (no more than twice)
    nums = [1,1,2,2,3]
    k = sol.removeDuplicates(nums)
    assert k == 5 and nums[:k] == [1,1,2,2,3], f"Test 4 Failed: got {nums[:k]}"
    print("✓ Test 4 Passed: already valid array")

    # Test 5: all duplicates
    nums = [2,2,2,2,2]
    k = sol.removeDuplicates(nums)
    assert k == 2 and nums[:k] == [2,2], f"Test 5 Failed: got k={k}, nums={nums[:k]}"
    print("✓ Test 5 Passed: all duplicates collapsed to two")

    # Test 6: mixed pattern
    nums = [1,1,1,2,2,2,3,3]
    k = sol.removeDuplicates(nums)
    assert k == 6 and nums[:k] == [1,1,2,2,3,3], f"Test 6 Failed: got {nums[:k]}"
    print("✓ Test 6 Passed: mixed pattern")

    # Test 7: no duplicates
    nums = [1,2,3,4]
    k = sol.removeDuplicates(nums)
    assert k == 4 and nums[:k] == [1,2,3,4], f"Test 7 Failed: got {nums[:k]}"
    print("✓ Test 7 Passed: no duplicates")

    print("\n✅ All Remove Dup (<=2) tests passed!")
