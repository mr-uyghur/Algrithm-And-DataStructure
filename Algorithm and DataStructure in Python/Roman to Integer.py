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

class Solution(object):
    def romanToInt(self, s):
        #create an Roman to Integer hashmap (dict)
        #create a var to keep track of the answer
        roman = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000}
        answer = 0
        #loop thru the Roman string, add the roman number to the answer
        #use roman hashmap to convert them to integers
        #check if there are cases CM = 900, XC = 90 and IV = 4 IX XL CD and subtract
        for i in s:
            answer += roman[i]
        if 'IV' in s or 'IX' in s:
            answer -= 2
        if 'XL' in s or 'XC' in s:
            answer -= 20
        if 'CD' in s or 'CM' in s:
            answer -= 200
        return answer

#this solution passes all leet code test cases
print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))