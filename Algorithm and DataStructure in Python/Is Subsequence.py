# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution(object):
    def isSubsequence(self, s, t):
# Initialize Pointers: Start by initializing two pointers, 
#one for each string s and t. Let's call them i and j
#both i and j are set to 0. These pointers will help us traverse both strings.

# Traverse the Strings:  iterate through string t using pointer j while checking if the current character in t matches the current character in s pointed by i.
#If they match, we move the pointer i forward (i.e., i += 1) to check the next character in s in the next iterations.

# Checking for Subsequence: Each time a character in s matches a character in t (according to the pointers),
# 23 move the pointer i forward. If we reach the end of s (i == len(s)), it means all characters of s have been found in t in the correct order, 
#so s is a subsequence of t. In this case, we should return true.

# End Condition: If we finish traversing t (the outer loop over j completes) and haven't found all characters of s (i.e., i doesn't reach len(s)), 
#then s is not a subsequence of t, and we should return false.
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1
            j +=1
        if i == len(s):
            return True
        return False
#this solution passes all test cases on leet code
print(Solution().isSubsequence("abc", "ahbgdc"))  # Expected: true
print(Solution().isSubsequence("axc", "ahbgdc"))  # Expected: false
print(Solution().isSubsequence("", "ahbgdc"))  # Expected: true (an empty string is a subsequence of any string)
print(Solution().isSubsequence("abc", ""))  # Expected: false (a non-empty string cannot be a subsequence of an empty string)
print(Solution().isSubsequence("abc", "abc"))  # Expected: true (the string is a subsequence of itself)
print(Solution().isSubsequence("abcd", "abdc"))  # Expected: false (order matters)
print(Solution().isSubsequence("a", "a"))  # Expected: true (single character is a subsequence of itself)
print(Solution().isSubsequence("xyz", "xzyabcd"))  # Expected: false (not in order)
print(Solution().isSubsequence("ace", "abcde"))  # Expected: true (example of characters spaced out)
print(Solution().isSubsequence("aec", "abcde"))  # Expected: false (incorrect order)

 
        