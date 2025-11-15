#  Contains Duplicate II
#  Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #find indexes of duplicate numbers.
        #if abs(index1 - index2) <= k-(second input) true
        #false otherwise
        #loop thru the array, add the int to a dict to keep track of idex
        #when the 2 indexes are found, compare the abs value with k
        #if it matches return true, otherwise keep looping thru the array and update the idex
        #repeat this operation
        data = {}
        for i, num in enumerate(nums):
            if num in data:
                if abs(i - data[num]) <= k:
                    return True
            data[num] = i
        return False
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) == True, "Test 1 Failed"
    print("✓ Test 1 Passed: [1,2,3,1], k=3 -> True")

    # Example 2
    assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) == True, "Test 2 Failed"
    print("✓ Test 2 Passed: [1,0,1,1], k=1 -> True")

    # Example 3
    assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False, "Test 3 Failed"
    print("✓ Test 3 Passed: [1,2,3,1,2,3], k=2 -> False")

    # Edge: empty array
    assert sol.containsNearbyDuplicate([], 5) == False, "Test 4 Failed"
    print("✓ Test 4 Passed: [] is False")

    # Edge: single element
    assert sol.containsNearbyDuplicate([1], 1) == False, "Test 5 Failed"
    print("✓ Test 5 Passed: Single element is False")

    # k = 0 (no two distinct indices can be within 0 distance)
    assert sol.containsNearbyDuplicate([1, 1], 0) == False, "Test 6 Failed"
    print("✓ Test 6 Passed: k=0 returns False")

    # Adjacent duplicate
    assert sol.containsNearbyDuplicate([1, 1], 1) == True, "Test 7 Failed"
    print("✓ Test 7 Passed: Adjacent duplicates return True")

    # Non-adjacent but within k
    assert sol.containsNearbyDuplicate([1, 2, 1], 2) == True, "Test 8 Failed"
    print("✓ Test 8 Passed: [1,2,1], k=2 -> True")

    # Non-adjacent and outside k
    assert sol.containsNearbyDuplicate([1, 2, 1], 1) == False, "Test 9 Failed"
    print("✓ Test 9 Passed: [1,2,1], k=1 -> False")

    # Negative numbers
    assert sol.containsNearbyDuplicate([-1, -1], 1) == True, "Test 10 Failed"
    print("✓ Test 10 Passed: Negative duplicate")

    # Duplicates further apart
    assert sol.containsNearbyDuplicate([1, 2, 3, 4, 2], 3) == True, "Test 11 Failed"
    print("✓ Test 11 Passed: duplicate found within k")

    # Long repeating values with k limit
    arr = [99] * 100 + [99]
    assert sol.containsNearbyDuplicate(arr, 100) == True, "Test 12 Failed"
    print("✓ Test 12 Passed: repeating values with k cover last duplicate")

    print("\n✅ All ContainDupII tests passed!")


        
