# Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #2 pointer approach.
        #slow pointer keep track of the new length.
        #fast pointer scans the array
        #if scanned elment != val
        #place the current element in slow pointer position
        #slow pointer +1
        #after scanning thru the array return slow pointer
        i = 0
        for num in nums:
            #num is the fast pointer
            if num != val:
                nums[i] = num
                i +=1
        return i
    
    #this solition has 0ms runtime and beats 100% of python3 submissions    

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums = [3, 2, 2, 3]
    k = sol.removeElement(nums, 3)
    assert k == 2, f"Expected k=2, got {k}"
    assert sorted(nums[:k]) == [2, 2], f"Expected [2,2], got {nums[:k]}"
    print("✓ Test 1 Passed: example with val=3")

    # Example 2
    nums = [0,1,2,2,3,0,4,2]
    k = sol.removeElement(nums, 2)
    assert k == 5, f"Expected k=5, got {k}"
    assert sorted(nums[:k]) == sorted([0,1,4,0,3]), f"Expected elements [0,1,4,0,3], got {nums[:k]}"
    print("✓ Test 2 Passed: example with multiple 2s")

    # Test 3: empty array
    nums = []
    k = sol.removeElement(nums, 1)
    assert k == 0 and nums == [], f"Expected k=0 and nums=[], got {k}, {nums}"
    print("✓ Test 3 Passed: empty array")

    # Test 4: no occurrences (val not present)
    nums = [1,2,3]
    original = nums.copy()
    k = sol.removeElement(nums, 4)
    assert k == 3 and sorted(nums[:k]) == sorted(original), f"Expected unchanged array, got {nums[:k]}"
    print("✓ Test 4 Passed: val not present (no removals)")

    # Test 5: all elements removed
    nums = [5,5,5]
    k = sol.removeElement(nums, 5)
    assert k == 0, f"Expected k=0 when all removed, got {k}"
    print("✓ Test 5 Passed: all elements removed -> k=0")

    # Test 6: mixture and duplicates
    nums = [4,1,2,4,3,4,2]
    k = sol.removeElement(nums, 4)
    assert sorted(nums[:k]) == sorted([1,2,3,2]), f"Expected [1,2,3,2], got {nums[:k]}"
    print("✓ Test 6 Passed: mixture with duplicates")

    # Test 7: val is at the end
    nums = [1,2,3,4]
    k = sol.removeElement(nums, 4)
    assert k == 3 and sorted(nums[:k]) == [1,2,3], f"Expected [1,2,3], got {nums[:k]}"
    print("✓ Test 7 Passed: val at the end")

    print("\n✅ All Remove Element tests passed!")