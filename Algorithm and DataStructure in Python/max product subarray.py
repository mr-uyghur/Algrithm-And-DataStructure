# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.
# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution(object):
    def maxProduct(self, nums):
        #use dyinamic programming approach
        #use tracking vars to keep track of min and max products
        #since a very small number could turn into a large one if multiplied by another negative number
        minNum = nums[0]
        maxNum = nums[0]
        finalProduct = nums[0]

        for num in nums[1:]:
            #use temp values to store the oridinal max and min product value
            tempMax = maxNum
            tempMin = minNum

            maxNum = max(num, num*tempMax, num*tempMin )
            minNum = min(num, num*tempMax, num*tempMin  ) 
            
            #the following one line of code can replace the 4 lines of code above and it'll still work
            #-------------------------------------------------------------

            # maxNum, minNum = max(num, num*maxNum, num*minNum),min(num, num*maxNum, num*minNum )

            #--------------------------------------------------------------

            finalProduct = max(finalProduct, maxNum)

        return finalProduct
    
print(Solution().maxProduct([2,3,-2,4])) # 6
print(Solution().maxProduct([-2,0,-1])) # 0
print(Solution().maxProduct([-1])) # -1 (Single element)
print(Solution().maxProduct([0,2])) # 2 (Array with a zero)
print(Solution().maxProduct([-2,-3,-4])) # 12 (All negative numbers)
print(Solution().maxProduct([1,2,3,4])) # 24 (All positive numbers)
print(Solution().maxProduct([-1, -2, -3, 0, 1])) # 6 (Mix of positive, negative, and zero)
print(Solution().maxProduct([0, 0, 0, 0])) # 0 (All zeros)
print(Solution().maxProduct([2,-5,-2,-4,3])) # 24 (Complex case)