# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution(object):
    def strStr(self, haystack, needle):
        #check if the needle is included in the haystack, if not return -1
        if needle not in haystack:
            return -1
        #return the index of needle from haystack
        return haystack.index(needle)

#this solution passes all test cases on leet code
print(Solution().strStr("sadbutsad","sad")) 
print(Solution().strStr("leetcode","leeto")) 
# Assuming the Solution class and strStr function are defined correctly above
print(Solution().strStr("hello", "he"))  # Expected: 0
print(Solution().strStr("goodbye", "bye"))  # Expected: 4
print(Solution().strStr("middle", "dd"))  # Expected: 2
print(Solution().strStr("mississippi", "sing"))  # Expected: -1
print(Solution().strStr("haystack", ""))  # Expected: 0
print(Solution().strStr("", "needle"))  # Expected: -1
print(Solution().strStr("short", "longerSubstring"))  # Expected: -1
print(Solution().strStr("identical", "identical"))  # Expected: 0
