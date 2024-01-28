#242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution(object):
    def isAnagram(self, s, t):
        #check if 2 inputes are the same length
        #diff lenth str can't be anagram so return False
        if len(s) != len(t):
            return False
        #use hashmap to keep count of how many times each char occurs
        #if 2 inputs have the same key and value pair return True
        dataS = {}
        dataT={}
        
        for i in s:
            if i in dataS:
                dataS[i] += 1
            elif i not in dataS:
                dataS[i] = 1
        #print(dataS)

        for j in t:
            if j in dataT:
                dataT[j] += 1
            elif j not in dataT:
                dataT[j] = 1
       # print(dataT)
        #return True if 2 dictionary (hashmaps) have the same key and value pair
        if dataS == dataT:
            return True
        else:
            return False
        
#this solution has 25ms runtime, faster than 91% of python solutions on leetcode
print(Solution().isAnagram("anagram", "nagaram"))  # True
print(Solution().isAnagram("rat", "car"))          # False
print(Solution().isAnagram("listen", "silent"))    # True
print(Solution().isAnagram("triangle", "integral"))# True
print(Solution().isAnagram("hello", "olleh"))      # True
print(Solution().isAnagram("apple", "aple"))       # False