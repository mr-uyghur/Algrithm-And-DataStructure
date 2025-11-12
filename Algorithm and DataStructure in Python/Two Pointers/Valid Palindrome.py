# Valid Palindrome
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

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean the string
        #2 pointer apprach
        #move pointers inward while comparing characters
        #return false if there's mismatch between the pointer, otherwise return true
        newStr = ''.join(ch.lower() for ch in s if ch.isalnum())
        print(newStr)
        left = 0
        right = len(newStr) - 1
        while left < right:
            if newStr[left] != newStr[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sol = Solution()

    # Example tests
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True, "Test 1 Failed"
    print("✓ Test 1 Passed: Example palindrome")

    assert sol.isPalindrome("race a car") == False, "Test 2 Failed"
    print("✓ Test 2 Passed: Example non-palindrome")

    # Edge cases
    assert sol.isPalindrome(" ") == True, "Test 3 Failed"
    print("✓ Test 3 Passed: Single space (empty after cleanup) is palindrome")

    # Mixed casing and punctuation
    assert sol.isPalindrome("Able was I, ere I saw Elba") == True, "Test 4 Failed"
    print("✓ Test 4 Passed: Mixed case and punctuation")

    # Numbers and letters
    assert sol.isPalindrome("0P") == False, "Test 5 Failed"
    print("✓ Test 5 Passed: '0P' is not a palindrome after cleanup")

    # Simple palindromes and non-palindromes
    assert sol.isPalindrome("racecar") == True, "Test 6 Failed"
    print("✓ Test 6 Passed: 'racecar'")

    assert sol.isPalindrome("12321") == True, "Test 7 Failed"
    print("✓ Test 7 Passed: numeric palindrome")

    assert sol.isPalindrome("1231") == False, "Test 8 Failed"
    print("✓ Test 8 Passed: numeric non-palindrome")

    print("\n✅ All Valid Palindrome tests passed!")