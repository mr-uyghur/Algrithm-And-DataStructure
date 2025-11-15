# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #store inputs in 2 dict in this format
        # str:counter, to keep track of the letters from the input
        #returm true if 2 dict are the same, false otherwise
        #return false if the length of 2 input is not the same
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for char1, char2 in zip(s,t):
            dict1[char1] = dict1.get(char1, 0) + 1
            dict2[char2] = dict2.get(char2, 0) + 1
        if dict1 == dict2:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Example 1 - valid anagram
    assert sol.isAnagram("anagram", "nagaram") == True, "Test 1 Failed"
    print("✓ Test 1 Passed: 'anagram' and 'nagaram' are anagrams")

    # Test 2: Example 2 - not an anagram
    assert sol.isAnagram("rat", "car") == False, "Test 2 Failed"
    print("✓ Test 2 Passed: 'rat' and 'car' are not anagrams")

    # Test 3: Single character anagrams
    assert sol.isAnagram("a", "a") == True, "Test 3 Failed"
    print("✓ Test 3 Passed: Single same character is anagram")

    # Test 4: Single character non-anagrams
    assert sol.isAnagram("a", "b") == False, "Test 4 Failed"
    print("✓ Test 4 Passed: Single different characters are not anagrams")

    # Test 5: Different lengths
    assert sol.isAnagram("abc", "abcd") == False, "Test 5 Failed"
    print("✓ Test 5 Passed: Different length strings are not anagrams")

    # Test 6: All same characters
    assert sol.isAnagram("aaa", "aaa") == True, "Test 6 Failed"
    print("✓ Test 6 Passed: Identical strings with repeated chars are anagrams")

    # Test 7: Same characters, different order
    assert sol.isAnagram("listen", "silent") == True, "Test 7 Failed"
    print("✓ Test 7 Passed: 'listen' and 'silent' are anagrams")

    # Test 8: Different character counts
    assert sol.isAnagram("aab", "baa") == True, "Test 8 Failed"
    print("✓ Test 8 Passed: 'aab' and 'baa' are anagrams")

    # Test 9: Same chars but different counts
    assert sol.isAnagram("aaab", "aab") == False, "Test 9 Failed"
    print("✓ Test 9 Passed: Different character counts are not anagrams")

    # Test 10: Reverse string anagrams
    assert sol.isAnagram("abc", "cba") == True, "Test 10 Failed"
    print("✓ Test 10 Passed: 'abc' and 'cba' are anagrams")

    # Test 11: Two character anagrams
    assert sol.isAnagram("ab", "ba") == True, "Test 11 Failed"
    print("✓ Test 11 Passed: 'ab' and 'ba' are anagrams")

    # Test 12: Long string anagrams
    assert sol.isAnagram("abcdefghijklmnop", "ponmlkjihgfedcba") == True, "Test 12 Failed"
    print("✓ Test 12 Passed: Long string anagrams")

    print("\n✅ All Valid Anagram tests passed!")
