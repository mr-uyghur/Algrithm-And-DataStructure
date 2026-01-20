# 151. Reverse Words in a String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        #store the word as array, get rid of the space.
        #use 2 pointer, l = first index, r = last index
        #while left < right
        #loop thru the array, and swap the left index value with right index value.
        #this way we will have reverse the words wtih 2 pointers
        #return the new array as string with " " in between
        words = s.split()
        left = 0
        right = len(words) - 1

        while left < right:
            curr_word = words[left]
            words[left] = words[right]
            words[right] = curr_word

            left += 1
            right -= 1
        return " ".join(words)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic example
    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    print("✓ Test 1 passed: Basic example")
    
    # Test case 2: String with leading and trailing spaces
    assert solution.reverseWords("  hello world  ") == "world hello"
    print("✓ Test 2 passed: Leading and trailing spaces")
    
    # Test case 3: Multiple spaces between words
    assert solution.reverseWords("a good   example") == "example good a"
    print("✓ Test 3 passed: Multiple spaces between words")
    
    # Test case 4: Single word
    assert solution.reverseWords("hello") == "hello"
    print("✓ Test 4 passed: Single word")
    
    # Test case 5: Two words
    assert solution.reverseWords("hello world") == "world hello"
    print("✓ Test 5 passed: Two words")
    
    # Test case 6: Single character words
    assert solution.reverseWords("a b c") == "c b a"
    print("✓ Test 6 passed: Single character words")
    
    # Test case 7: Mixed length words with extra spaces
    assert solution.reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
    print("✓ Test 7 passed: Mixed length words with extra spaces")
    
    print("\nAll test cases passed!")
        