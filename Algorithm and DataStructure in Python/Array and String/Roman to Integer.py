# Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def romanToInt(self, s: str) -> int:
        #create a dict set with Roman to Number data 
        #create a result = 0
        #loop thru the given string
        #if the current index < next index subtract current from result
        #else add current
        #this condition covers cases like IV = 4

        result = 0
        values = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                    }
        for i in range(len(s) ):
            #make sure the current index is not the last index.
            current = values[s[i]] #this points to the current index in string -> Roman number
            if i != len(s) -1:
                next_value = values[s[i+1]]

                if current < next_value:
                    result = result - current
                else:
                    result = result + current
            else:
                result = result + current
        return result

        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.romanToInt("III") == 3, "Test 1 Failed"
    print("✓ Test 1 Passed: 'III' -> 3")

    # Example 2
    assert sol.romanToInt("LVIII") == 58, "Test 2 Failed"
    print("✓ Test 2 Passed: 'LVIII' -> 58")

    # Example 3
    assert sol.romanToInt("MCMXCIV") == 1994, "Test 3 Failed"
    print("✓ Test 3 Passed: 'MCMXCIV' -> 1994")

    # Additional edge cases
    assert sol.romanToInt("IV") == 4, "Test 4 Failed"
    print("✓ Test 4 Passed: 'IV' -> 4")

    assert sol.romanToInt("IX") == 9, "Test 5 Failed"
    print("✓ Test 5 Passed: 'IX' -> 9")

    assert sol.romanToInt("XL") == 40, "Test 6 Failed"
    print("✓ Test 6 Passed: 'XL' -> 40")

    assert sol.romanToInt("CD") == 400, "Test 7 Failed"
    print("✓ Test 7 Passed: 'CD' -> 400")

    assert sol.romanToInt("I") == 1, "Test 8 Failed"
    print("✓ Test 8 Passed: 'I' -> 1")

    assert sol.romanToInt("MMMCMXCIX") == 3999, "Test 9 Failed"
    print("✓ Test 9 Passed: 'MMMCMXCIX' -> 3999")

    print("\n✅ All Roman to Integer tests passed!")

