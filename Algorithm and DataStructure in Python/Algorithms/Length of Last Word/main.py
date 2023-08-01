#Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal 
# substring
#  consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split the string into a list with spaces in between
        words = s.split(" ")
        list = []
        # this logic will traverse thru the initial list
        # and checks for eadge cases
        for i in range(0,len(words)):
           # print(words[i])
           #only add the index with value that's higher than 0 bc we don't want any empty spaces in the list
            if len(words[i]) > 0:
                list.append(words[i])
        print(list)
        last_word = list[-1]
        return len(last_word)
    
print(Solution().lengthOfLastWord("Hello World"))
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
print(Solution().lengthOfLastWord("luffy is still joyboy"))