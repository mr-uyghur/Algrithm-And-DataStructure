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
# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

import unittest


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #check if the ransomNote is longer than magazine
        #return false if yes
        if len(ransomNote) > len(magazine):
            return False
        #store value of magazine in a dict
        #with the letters as key and value as counter int
        #loop thru ransomeNote,
        #decrease the value of each letter found.
        #return false if any int goes below 0
        #return true if the value for the letters found in ransomeNote is 0
        char_count = {}
        for char in magazine:
            char_count[char] = char_count.get(char, 0) +1
        print(char_count)

        for l in ransomNote:
            if l not in char_count:
                return False
            char_count[l] -= 1 #decrease the count for this char
            if char_count[l] < 0:
                return False
        return True

class TestRansomNote(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test case from example 1: different single characters"""
        self.assertFalse(self.solution.canConstruct("a", "b"))
    
    def test_example_2(self):
        """Test case from example 2: not enough characters"""
        self.assertFalse(self.solution.canConstruct("aa", "ab"))
    
    def test_example_3(self):
        """Test case from example 3: sufficient characters"""
        self.assertTrue(self.solution.canConstruct("aa", "aab"))
    
    def test_empty_strings(self):
        """Test with empty strings"""
        self.assertTrue(self.solution.canConstruct("", ""))
        self.assertTrue(self.solution.canConstruct("", "abc"))
    
    def test_longer_ransom_note(self):
        """Test when ransom note is longer than magazine"""
        self.assertFalse(self.solution.canConstruct("abc", "ab"))
    
    def test_different_frequencies(self):
        """Test with same characters but different frequencies"""
        self.assertTrue(self.solution.canConstruct("hello", "helloworld"))
        self.assertFalse(self.solution.canConstruct("hello", "world"))
    
    def test_case_sensitivity(self):
        """Test case sensitivity matters"""
        self.assertFalse(self.solution.canConstruct("a", "A"))
    
    def test_complex_string(self):
        """Test with more complex strings"""
        self.assertTrue(self.solution.canConstruct("paper", "paperplane"))
        self.assertFalse(self.solution.canConstruct("paper", "painter"))

if __name__ == '__main__':
    unittest.main()