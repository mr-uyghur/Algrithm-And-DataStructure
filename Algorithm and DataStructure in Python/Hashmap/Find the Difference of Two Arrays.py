# 2215. Find the Difference of Two Arrays
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
# Example 2:

# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #loop thru each number in given inputs.
        #check if the number exists in the other input.
        #if it doesn't exist, append that number into an array.
        #do the same for the second input.
        #return the 2 lists 
        #convert the given input into set to avoid duplicates
        data1 = set(nums1)
        data2 = set(nums2)
        ans1 = []
        ans2 = []
        for num in data1:
            if num not in data2:
                ans1.append(num)
        for num in data2:
            if num not in data1:
                ans2.append(num)
        return [ans1, ans2]


if __name__ == "__main__":
    sol = Solution()

    def _eq(a, b):
        return set(map(frozenset, a)) == set(map(frozenset, b))

    tests = [
        ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
        ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
        ([], [], [[], []]),
        ([0, -1, 2], [2, 3, -1], [[0], [3]]),
        # additional cases
        ([1, 2, 2, 3, 5], [2, 3, 4, 4, 5], [[1], [4]]),
        ([1, 1, 1], [1], [[], []]),
        (list(range(10)), list(range(5, 15)), [[0, 1, 2, 3, 4], [10, 11, 12, 13, 14]]),
        ([-1, -2, -2, -3], [-3, -4], [[-1, -2], [-4]]),
        ([0], [1], [[0], [1]]),
        ([1000] * 10, [1000], [[], []]),
    ]

    for i, (n1, n2, exp) in enumerate(tests, 1):
        res = sol.findDifference(n1, n2)
        assert _eq(res, exp), f"Test {i} failed: got {res}, expected {exp}"

    print("All tests passed")
