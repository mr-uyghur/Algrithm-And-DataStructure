# 121. Best Time to Buy and Sell Stock
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for sell in prices[1:]:
            profit = max(profit, sell - buy)
            if sell < buy:
                buy = sell
        return profit
        

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    assert sol.maxProfit([7,1,5,3,6,4]) == 5, "Test 1 Failed"
    print("✓ Test 1 Passed: [7,1,5,3,6,4] -> 5")

    # Example 2
    assert sol.maxProfit([7,6,4,3,1]) == 0, "Test 2 Failed"
    print("✓ Test 2 Passed: [7,6,4,3,1] -> 0")

    # Test 3: Single day
    assert sol.maxProfit([5]) == 0, "Test 3 Failed"
    print("✓ Test 3 Passed: single day -> 0")

    # Test 4: Two days increasing
    assert sol.maxProfit([1, 10]) == 9, "Test 4 Failed"
    print("✓ Test 4 Passed: [1,10] -> 9")

    # Test 5: All equal prices
    assert sol.maxProfit([3,3,3,3]) == 0, "Test 5 Failed"
    print("✓ Test 5 Passed: equal prices -> 0")

    # Test 6: Increasing sequence
    assert sol.maxProfit([1,2,3,4,5]) == 4, "Test 6 Failed"
    print("✓ Test 6 Passed: increasing sequence -> 4")

    # Test 7: Profit at the end
    assert sol.maxProfit([5,4,3,2,10]) == 8, "Test 7 Failed"
    print("✓ Test 7 Passed: profit at end -> 8")

    # Test 8: Large values
    assert sol.maxProfit([10000, 0, 10000]) == 10000, "Test 8 Failed"
    print("✓ Test 8 Passed: large values -> 10000")

    # Test 9: Random-like pattern
    assert sol.maxProfit([2,1,4,1,3]) == 3, "Test 9 Failed"
    print("✓ Test 9 Passed: [2,1,4,1,3] -> 3")

    print("\n✅ All Best Time to Buy and Sell Stock tests passed!")
