# 49. Group Anagrams
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

import unittest
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create and empty hashmap
        #loop thru each index in the given array list.
        #sort each index. amagrams will be the same after being sorted
        #if sorted index is not in the hashmap
        # sorted word = []
        #otherwise append the sorted word to hashmap as key and the original word as value 
        #return all value in the hashmap

        group = {
        
        }

        for word in strs:
            key = "".join(sorted(word))
            if key not in group:
                group[key] = []
            group[key].append(word)
        return list(group.values())


if __name__ == "__main__":
    sol = Solution()

    def _norm(groups):
        return sorted([sorted(g) for g in groups])

    # Test 1: Example 1
    assert _norm(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) == _norm([["bat"],["nat","tan"],["ate","eat","tea"]]), "Test 1 Failed"
    print("✓ Test 1 Passed: example grouping")

    # Test 2: Single empty string
    assert _norm(sol.groupAnagrams([""])) == _norm([[""]]), "Test 2 Failed"
    print("✓ Test 2 Passed: single empty string")

    # Test 3: Single character
    assert _norm(sol.groupAnagrams(["a"])) == _norm([["a"]]), "Test 3 Failed"
    print("✓ Test 3 Passed: single character")

    # Test 4: Two different single characters
    assert _norm(sol.groupAnagrams(["a","b"])) == _norm([["a"],["b"]]), "Test 4 Failed"
    print("✓ Test 4 Passed: two different single characters")

    # Test 5: Different lengths
    assert _norm(sol.groupAnagrams(["abc","abcd"])) == _norm([["abc"],["abcd"]]), "Test 5 Failed"
    print("✓ Test 5 Passed: different lengths")

    # Test 6: All same characters repeated
    assert _norm(sol.groupAnagrams(["aa","aa","aa"])) == _norm([["aa","aa","aa"]]), "Test 6 Failed"
    print("✓ Test 6 Passed: repeated identical strings")

    # Test 7: Same characters, different order
    assert _norm(sol.groupAnagrams(["listen","silent"])) == _norm([["listen","silent"]]), "Test 7 Failed"
    print("✓ Test 7 Passed: 'listen' and 'silent' are grouped")

    # Test 8: Different character counts but anagrams
    assert _norm(sol.groupAnagrams(["aab","baa"])) == _norm([["aab","baa"]]), "Test 8 Failed"
    print("✓ Test 8 Passed: 'aab' and 'baa' are grouped")

    # Test 9: Same chars but different counts
    assert _norm(sol.groupAnagrams(["aaab","aab"])) == _norm([["aaab"],["aab"]]), "Test 9 Failed"
    print("✓ Test 9 Passed: different counts are separated")

    # Test 10: Reverse string anagrams
    assert _norm(sol.groupAnagrams(["abc","cba"])) == _norm([["abc","cba"]]), "Test 10 Failed"
    print("✓ Test 10 Passed: reverse strings grouped")

    # Test 11: Two character anagrams
    assert _norm(sol.groupAnagrams(["ab","ba"])) == _norm([["ab","ba"]]), "Test 11 Failed"
    print("✓ Test 11 Passed: two-char anagrams")

    # Test 12: Long string anagrams
    assert _norm(sol.groupAnagrams(["abcdefghijklmnop","ponmlkjihgfedcba"])) == _norm([["abcdefghijklmnop","ponmlkjihgfedcba"]]), "Test 12 Failed"
    print("✓ Test 12 Passed: long string anagrams")

    print("\n✅ All Group Anagrams tests passed!")


