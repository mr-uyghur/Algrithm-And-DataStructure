# Given an array nums containing n distinct numbers in the range [0, n], 
#return the only number in the range that is missing from the array.
# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # calculate the length of the array list
        # calculate the sum of the array length from 0 to n.
        # calculate the sum of 0 to n ( actual length of the arr)
        # subtract sum of the 0 to n from the length of the array list
        n = len(nums)
        nSum = n* (n +1)/2
        arraySum = sum(nums)
        result = int(nSum - arraySum)
        #print(abs(result))
        return abs(result)

print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
        
# Test case 1: Testing with a sequence that includes negative numbers, which is a bit of a trick since the problem usually assumes non-negative integers.
print(Solution().missingNumber([-1, 0, 1, 2]))  # Expected output: The missing number is not well-defined in the context of non-negative integers sequence.

# Test case 2: Testing with a longer sequence that is missing the last number.
print(Solution().missingNumber([0, 1, 2, 3, 4, 5, 6, 7, 8]))  # Expected output: 9

# Test case 3: Testing with a single-element array, which is the smallest non-trivial case.
print(Solution().missingNumber([1]))  # Expected output: 0, since 0 is missing and it's the smallest non-negative integer.

# Test case 4: Testing with a sequence that misses the first number (0 in this case).
print(Solution().missingNumber([1, 2, 3, 4, 5]))  # Expected output: 0

# Test case 5: Testing with a sequence that has all the numbers but in a jumbled order.
print(Solution().missingNumber([4, 2, 3, 1, 0, 6]))  # Expected output: 5

# Test case 6: Testing with an empty array, assuming the sequence starts with 0.
print(Solution().missingNumber([]))  # Expected output: 0, since the array is empty and 0 is considered missing.

# Note: The first test case is a bit of a trick and might not align with the expected problem constraints of non-negative integers only. It's there to challenge the assumption and see how the method handles unexpected inputs.

