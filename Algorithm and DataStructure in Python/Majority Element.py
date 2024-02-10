# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    def majorityElement(self, nums):
        #store the nums in dict as key and val pair
        #key being the actual num, value being the times it occured
        data = {}
        #store the num and set the key equal to 1
        #if the num already is in the dict then icrease the key by 1
        for num in nums:
            if num in data:
                data[num] += 1
            elif num not in data:
                data[num] = 1
        print(data)
        #tracker var for max value from data hashmap (dictionary)
        majority = 0
        max_val = 0
        for key, val in data.items():
            #if the val is bigger than the current val
            #update the max val and update the majority 
            if val > max_val:
                max_val = val
                majority = key
        return majority

#this solution passes all test cases on leetcode
print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))
print(Solution().majorityElement([1]))  # Expected: 1
print(Solution().majorityElement([4, 4, 4, 4]))  # Expected: 4
# No test case for no majority element since the problem statement assumes one always exists
print(Solution().majorityElement([5, 5, 5, 2, 2, 1]))  # Expected: 5
print(Solution().majorityElement([1, 1, 1, 2, 3, 4, 5]))  # Expected: 1
print(Solution().majorityElement([1, 2, 3, 4, 5, 6, 6, 6, 6, 6]))  # Expected: 6
print(Solution().majorityElement([-3, -3, -3, -3, 2, 2, 1]))  # Expected: -3
print(Solution().majorityElement([1000000000, 1000000000, 2, 1000000000, 1000000000]))  # Expected: 1000000000
