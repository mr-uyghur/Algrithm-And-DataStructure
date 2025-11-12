#Three Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #2 pointer approach
        #sort the given array
        #first pointer = +1, 2nd pointer = len(nums) - 1
        #iterate thru each number when the target is 0 store the numbers in an array
        arr = []
        nums.sort()

        for i in range(len(nums) - 2):
            #skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    arr.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    # Then move both pointers
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return arr


        

def _normalize(result: List[List[int]]) -> List[tuple]:
    """Helper to convert result lists to sorted list of tuples for comparison."""
    return sorted(tuple(triplet) for triplet in result)


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Example 1
    res = sol.threeSum([-1, 0, 1, 2, -1, -4])
    assert _normalize(res) == _normalize([[-1, -1, 2], [-1, 0, 1]]), f"Failed Test 1, got {res}"
    print("✓ Test 1 Passed")

    # Test 2: Example 2 -> no triplets
    res = sol.threeSum([0, 1, 1])
    assert _normalize(res) == _normalize([]), f"Failed Test 2, got {res}"
    print("✓ Test 2 Passed")

    # Test 3: Example 3 -> all zeros
    res = sol.threeSum([0, 0, 0])
    assert _normalize(res) == _normalize([[0, 0, 0]]), f"Failed Test 3, got {res}"
    print("✓ Test 3 Passed")

    # Test 4: not enough elements
    res = sol.threeSum([])
    assert _normalize(res) == _normalize([]), f"Failed Test 4, got {res}"
    print("✓ Test 4 Passed")

    # Test 5: negative combinations
    res = sol.threeSum([-2, 0, 1, 1, 2])
    assert _normalize(res) == _normalize([[-2, 0, 2], [-2, 1, 1]]), f"Failed Test 5, got {res}"
    print("✓ Test 5 Passed")

    # Test 6: duplicates produce single triplet
    res = sol.threeSum([0, 0, 0, 0])
    assert _normalize(res) == _normalize([[0, 0, 0]]), f"Failed Test 6, got {res}"
    print("✓ Test 6 Passed")

    # Test 7: large but valid numbers
    res = sol.threeSum([100000, -100000, 0])
    assert _normalize(res) == _normalize([[-100000, 0, 100000]]), f"Failed Test 7, got {res}"
    print("✓ Test 7 Passed")

    print("\n✅ All ThreeSum tests passed!")


