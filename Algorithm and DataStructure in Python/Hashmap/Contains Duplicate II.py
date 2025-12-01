# 219. Contains Duplicate II
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

from typing import List

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #hashmap approach.
        #if we've seen a duplicate number
        #check how far apart the indexes are
        #if the reapet number is <= k return true
        #otherwise update the last index in the hashmap
        #loop thru the entire array unless a valid pair is found early.
        data = {}
        for i, num in enumerate(nums):
            #if the num is already in the dict, it means we've seen a duplicate
            #check the distance between the current index and the previous index
            if num in data:
                #capture the previous index and compare the current index with k
                prev = data[num] 
                if i - prev <= k:
                    return True
                
            data[num] = i
        return False


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: True - duplicates at indices 0 and 3, distance = 3 <= k
    assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
    print("✓ Test 1 passed: [1,2,3,1], k=3")
    
    # Example 2: True - duplicates at indices 2 and 3, distance = 1 <= k
    assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
    print("✓ Test 2 passed: [1,0,1,1], k=1")
    
    # Example 3: False - duplicates at indices 0 and 3, distance = 3 > k=2
    assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
    print("✓ Test 3 passed: [1,2,3,1,2,3], k=2")
    
    # Test 4: Single element - no duplicates
    assert sol.containsNearbyDuplicate([1], 1) == False
    print("✓ Test 4 passed: [1], k=1")
    
    # Test 5: Two same elements with k=1 (minimum distance)
    assert sol.containsNearbyDuplicate([1, 1], 1) == True
    print("✓ Test 5 passed: [1,1], k=1")
    
    # Test 6: Two same elements but distance > k
    assert sol.containsNearbyDuplicate([1, 2, 1], 1) == False
    print("✓ Test 6 passed: [1,2,1], k=1")
    
    # Test 7: k=0 (no duplicates allowed within distance 0)
    assert sol.containsNearbyDuplicate([1, 2, 3, 1], 0) == False
    print("✓ Test 7 passed: [1,2,3,1], k=0")
    
    # Test 8: Multiple duplicates, one valid pair
    assert sol.containsNearbyDuplicate([99, 99], 2) == True
    print("✓ Test 8 passed: [99,99], k=2")
    
    # Test 9: Negative numbers
    assert sol.containsNearbyDuplicate([-1, -1, -1], 2) == True
    print("✓ Test 9 passed: [-1,-1,-1], k=2")
    
    # Test 10: Large k value with duplicates far apart
    assert sol.containsNearbyDuplicate([1, 2, 3, 4, 5, 1], 5) == True
    print("✓ Test 10 passed: [1,2,3,4,5,1], k=5")
    
    # Test 11: No duplicates at all
    assert sol.containsNearbyDuplicate([1, 2, 3, 4, 5], 10) == False
    print("✓ Test 11 passed: [1,2,3,4,5], k=10")
    
    # Test 12: Duplicates but just outside k range
    assert sol.containsNearbyDuplicate([1, 2, 3, 4, 1], 3) == False
    print("✓ Test 12 passed: [1,2,3,4,1], k=3")
    
    print("\n✅ All 12 tests passed!")
        