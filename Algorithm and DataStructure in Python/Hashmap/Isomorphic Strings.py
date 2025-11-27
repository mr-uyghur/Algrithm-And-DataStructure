# 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #use bijection approach
        #create 2 hashmap
        #map each letter from one input to the other
        #when there's a mismatch return False,
        #otherwise continue with the loop and mapping.
        #return True when mapping is done without mismatch
        if len(s) != len(t):
            return False
        data1 = {}
        data2 = {}

        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]
            if letter_s in data1:
                if data1[letter_s] != letter_t:
                    return False
            else:
                data1[letter_s] = letter_t
            if letter_t in data2:
                if data2[letter_t] != letter_s:
                    return False
            else:
                data2[letter_t] = letter_s
        print(data1, data2)

        return True
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.isIsomorphic("egg", "add") == True, "Test 1 Failed"
    print("✓ Test 1 Passed: 'egg' -> 'add'")

    # Example 2
    assert sol.isIsomorphic("foo", "bar") == False, "Test 2 Failed"
    print("✓ Test 2 Passed: 'foo' -> 'bar' (not isomorphic)")

    # Example 3
    assert sol.isIsomorphic("paper", "title") == True, "Test 3 Failed"
    print("✓ Test 3 Passed: 'paper' -> 'title'")

    # Test 4: different lengths
    assert sol.isIsomorphic("a", "") == False, "Test 4 Failed"
    print("✓ Test 4 Passed: different lengths -> False")

    # Test 5: same single char
    assert sol.isIsomorphic("a", "a") == True, "Test 5 Failed"
    print("✓ Test 5 Passed: single char identical -> True")

    # Test 6: repeating chars mapping to same
    assert sol.isIsomorphic("abab", "cdcd") == True, "Test 6 Failed"
    print("✓ Test 6 Passed: 'abab' -> 'cdcd' -> True")

    # Test 7: two chars map to same char (invalid)
    assert sol.isIsomorphic("ab", "cc") == False, "Test 7 Failed"
    print("✓ Test 7 Passed: 'ab' -> 'cc' -> False")

    # Test 8: non-ascii / punctuation
    assert sol.isIsomorphic("!@!", "#$$") == False, "Test 8 Failed"
    print("✓ Test 8 Passed: punctuation mapping -> False")

    # Test 9: identity mapping allowed
    assert sol.isIsomorphic("abc", "abc") == True, "Test 9 Failed"
    print("✓ Test 9 Passed: identity mapping -> True")

    # Test 10: longer complex case (isomorphic)
    assert sol.isIsomorphic("turtle", "tletur") == True, "Test 10 Failed"
    print("✓ Test 10 Passed: complex isomorphic case -> True")

    print("\n✅ All Isomorphic Strings tests passed!")
