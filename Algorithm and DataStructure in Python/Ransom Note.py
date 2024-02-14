# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        #put 2 string into 2 dictionaries to keep track of each letter
        data1 = {}
        data2 = {}
        #go thru ransomNote str and increament each letter by 1
        for i in ransomNote:
            if i in data1:
                data1[i] += 1
            else:
                data1[i] = 1
        #go thru magazine str and increament each letter by 1
        for j in magazine:
            if j in data2:
                data2[j] += 1
            else:
                data2[j] = 1
        # Compare Counts: For each letter in the ransomNote, 
        # check if the letter appears in the magazine with an equal or greater count. 
        
        for key, val in data1.items():
            if key not in data2:
                return False
            if val > data2[key]:
                return False
        return True
        
#this solution passes all test cases on leetcode
print(Solution().canConstruct("a","b")) #false
print(Solution().canConstruct("aa","ab")) #false
print(Solution().canConstruct("aa","aab")) #true