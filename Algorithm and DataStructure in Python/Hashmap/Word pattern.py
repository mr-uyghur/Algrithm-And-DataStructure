# 290. Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false

from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #core logic
        #use bijection approach
        #create 2 hashmap
        #loop thru both inputs and store them into the hashmap
        #'a' maps to 'dog' 
        #'dog' maps to 'a'
        #check if the current index exists in the hashmap
        #if yes, check for mismatch.
        #if there's a mismatch return false.
        #otherwise  continue with the loop and return true at the end
        data1 = {}
        data2 = {}
        words = s.split(' ')
        # print(words)
        # print(len(pattern),len(words))
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            word = words[i]
            letter = pattern[i]
            #check if the word exists in data1
            #if its a mismatch return false, therwise continue
            if word in data1:
                if data1[word] != letter:
                    return False
            else:
                data1[word] = letter
            if letter in data2:
                if data2[letter] != word:
                    return False
            else:
                data2[letter] = word
        return True
            
            
           

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.wordPattern("abba", "dog cat cat dog") == True, "Test 1 Failed"
    print("✓ Test 1 Passed: pattern='abba', s='dog cat cat dog' -> True")

    # Example 2
    assert sol.wordPattern("abba", "dog cat cat fish") == False, "Test 2 Failed"
    print("✓ Test 2 Passed: pattern='abba', s='dog cat cat fish' -> False")

    # Example 3
    assert sol.wordPattern("aaaa", "dog cat cat dog") == False, "Test 3 Failed"
    print("✓ Test 3 Passed: pattern='aaaa', s='dog cat cat dog' -> False")

    # Test 4: Single character and word
    assert sol.wordPattern("a", "dog") == True, "Test 4 Failed"
    print("✓ Test 4 Passed: Single char and word")

    # Test 5: Pattern shorter than words
    assert sol.wordPattern("ab", "dog cat dog") == False, "Test 5 Failed"
    print("✓ Test 5 Passed: Pattern shorter than words -> False")

    # Test 6: Pattern longer than words
    assert sol.wordPattern("abc", "dog cat") == False, "Test 6 Failed"
    print("✓ Test 6 Passed: Pattern longer than words -> False")

    # Test 7: Duplicate letters, different words
    assert sol.wordPattern("aa", "dog cat") == False, "Test 7 Failed"
    print("✓ Test 7 Passed: Duplicate letters map to different words -> False")

    # Test 8: Different letters, same word
    assert sol.wordPattern("ab", "dog dog") == False, "Test 8 Failed"
    print("✓ Test 8 Passed: Different letters map to same word -> False")

    # Test 9: Valid bijection with 3 letters
    assert sol.wordPattern("abc", "dog cat bird") == True, "Test 9 Failed"
    print("✓ Test 9 Passed: Valid bijection with 3 letters -> True")

    # Test 10: All same letters and words
    assert sol.wordPattern("aaa", "dog dog dog") == True, "Test 10 Failed"
    print("✓ Test 10 Passed: All same letters and words -> True")

    # Test 11: Complex valid pattern
    assert sol.wordPattern("abab", "dog cat dog cat") == True, "Test 11 Failed"
    print("✓ Test 11 Passed: Complex valid pattern -> True")

    print("\n✅ All Word Pattern tests passed!")
