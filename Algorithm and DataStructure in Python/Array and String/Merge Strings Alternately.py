# 1768. Merge Strings Alternately
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #use 2 pointer approach.
        #each pointer points to the first index of given words
        #obtain the highest length from the given input
        #loop thru the given input, loop ends with the highest length input.
        #add first index of word 1, then word 2 and increase the pointers by 1
        arr = []
        i = 0
        j = 0

        while i < len(word1) or j < len(word2):
            if i < len(word1):
                arr.append(word1[i])
                i += 1
            if j < len(word2):
                arr.append(word2[j])
                j += 1

        return "".join(arr)


if __name__ == '__main__':
    import unittest

    class TestMergeAlternately(unittest.TestCase):
        def setUp(self):
            self.sol = Solution()

        def test_equal_length(self):
            self.assertEqual(self.sol.mergeAlternately("abc", "pqr"), "apbqcr")

        def test_word2_longer(self):
            self.assertEqual(self.sol.mergeAlternately("ab", "pqrs"), "apbqrs")

        def test_word1_longer(self):
            self.assertEqual(self.sol.mergeAlternately("abcd", "pq"), "apbqcd")

        def test_empty_first(self):
            self.assertEqual(self.sol.mergeAlternately("", "xyz"), "xyz")

        def test_empty_second(self):
            self.assertEqual(self.sol.mergeAlternately("abc", ""), "abc")

        def test_both_empty(self):
            self.assertEqual(self.sol.mergeAlternately("", ""), "")

    unittest.main()
