# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:  # Existing mapping doesn't match current word
                    return False
            else:
                if word in word_to_char:  # Word already mapped to a different character
                    return False
                char_to_word[char] = word
                word_to_char[word] = char

        return True

#this solution passes all test cases on leet code