# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #keep track of char and its index with hasmap (dict)
        data = {}
        lowest = 0
        length = 0

        for r in range(len(s)):
            char = s[r]
            if char in data and data[char] >= lowest:
                lowest = data[char] + 1
            else:
                length = max(length,r - lowest + 1)
            data[char] = r
        return length

#this solution passes all leetcode test cases