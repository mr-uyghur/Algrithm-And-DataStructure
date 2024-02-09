# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


class Solution(object):
    def isPalindrome(self, s):
        #store the string into an array list by removing all the non-alphanumeric character
        letters = s.lower()
        arr = []

        for letter in letters:
            if letter.isalnum():
                arr.append(letter)
        #check if the arr list is the same as the revesed version of itself
        palindrome = list(reversed(arr))
        # print(arr)
        #print(palindrome)
        if arr == palindrome:
            return True
        else:
            return False

#this solution passes all test cases on leet code
print(Solution().isPalindrome("A man, a plan, a canal: Panama")) #True
print(Solution().isPalindrome("race a car")) #False
print(Solution().isPalindrome(" ")) #True

print(Solution().isPalindrome("No lemon, no melon")) # True
print(Solution().isPalindrome("Was it a car or a cat I saw?")) # True
print(Solution().isPalindrome("No 'x' in Nixon")) # True
print(Solution().isPalindrome("Madam, in Eden, I'm Adam")) # True
print(Solution().isPalindrome("Red roses run no risk, sir, on Nurse's order.")) # False
print(Solution().isPalindrome("12321")) # True
print(Solution().isPalindrome("123a321")) # True
print(Solution().isPalindrome("123abc")) # False
print(Solution().isPalindrome("1a2")) # False
