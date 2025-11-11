# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #2 pointer solution
        #1 pointer points to the first index of first input
        #2nd pointer points to the first index of second input/
        #2nd pointer moves thru the input,
        #when the pointers match, 1st pointer moves to the next index, 
        #repeat this process.
        #return False if not sequence is found.
        left = 0
        right = 0
        # print(left,right)
        if len(s) < 1:
            return True
        while right < len(t):
            if left < len(s) and s[left] == t[right]:
                left +=1
                right += 1
            else:
                right += 1
        if left == len(s):
            return True
        if right == len(t): #Return false if we loop thru the second input before the first input
            return False


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Basic example - true case
    assert solution.isSubsequence("abc", "ahbgdc") == True, "Test 1 Failed"
    print("✓ Test 1 Passed: 'abc' is a subsequence of 'ahbgdc'")
    
    # Test Case 2: Basic example - false case
    assert solution.isSubsequence("axc", "ahbgdc") == False, "Test 2 Failed"
    print("✓ Test 2 Passed: 'axc' is NOT a subsequence of 'ahbgdc'")
    
    # Test Case 3: Empty s (should return True)
    assert solution.isSubsequence("", "ahbgdc") == True, "Test 3 Failed"
    print("✓ Test 3 Passed: Empty string is a subsequence of any string")
    
    # Test Case 4: Empty t (non-empty s should return False)
    assert solution.isSubsequence("a", "") == False, "Test 4 Failed"
    print("✓ Test 4 Passed: Non-empty string is NOT a subsequence of empty string")
    
    # Test Case 5: Both empty (should return True)
    assert solution.isSubsequence("", "") == True, "Test 5 Failed"
    print("✓ Test 5 Passed: Empty string is a subsequence of empty string")
    
    # Test Case 6: Single character match
    assert solution.isSubsequence("a", "a") == True, "Test 6 Failed"
    print("✓ Test 6 Passed: Single character matches")
    
    # Test Case 7: Single character no match
    assert solution.isSubsequence("a", "b") == False, "Test 7 Failed"
    print("✓ Test 7 Passed: Single character doesn't match")
    
    # Test Case 8: Same strings
    assert solution.isSubsequence("abc", "abc") == True, "Test 8 Failed"
    print("✓ Test 8 Passed: Identical strings")
    
    # Test Case 9: s longer than t
    assert solution.isSubsequence("abcd", "abc") == False, "Test 9 Failed"
    print("✓ Test 9 Passed: s longer than t returns False")
    
    # Test Case 10: Characters out of order
    assert solution.isSubsequence("ba", "ab") == False, "Test 10 Failed"
    print("✓ Test 10 Passed: Characters in wrong order returns False")
    
    # Test Case 11: Multiple occurrences of same character
    assert solution.isSubsequence("aaa", "aaabbbccc") == True, "Test 11 Failed"
    print("✓ Test 11 Passed: Multiple same characters match correctly")
    
    # Test Case 12: Repeated characters, not enough in t
    assert solution.isSubsequence("aaaa", "aaa") == False, "Test 12 Failed"
    print("✓ Test 12 Passed: Not enough repeated characters returns False")
    
    # Test Case 13: Complex sequence at the end
    assert solution.isSubsequence("xyz", "aabbccxxyyzz") == True, "Test 13 Failed"
    print("✓ Test 13 Passed: Subsequence at the end of string")
    
    # Test Case 14: Alternating pattern
    assert solution.isSubsequence("ace", "abcde") == True, "Test 14 Failed"
    print("✓ Test 14 Passed: Alternating pattern matches")
    
    # Test Case 15: Non-consecutive matches
    assert solution.isSubsequence("bd", "abcd") == True, "Test 15 Failed"
    print("✓ Test 15 Passed: Non-consecutive characters match")
    
    print("\n✅ All test cases passed!")
        
