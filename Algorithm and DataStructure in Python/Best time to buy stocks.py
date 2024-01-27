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


class Solution(object):
    def maxProfit(self, prices):
     #create profit var and set it to 0
     #creat buy var set it as the first element of the prices arr
        profit = 0
        buy = prices[0]
        #loop thru the price array list starting from the second element
        #compare it with the first element = buy
        #if the selling price is higher than the buying price
        #calculate the profit
        #compare it to the profit var
        #take the maximum profit
        #if the buying price is lower than the selling price:
        #udpate the buying price to the cheaper option
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit
        

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
#this solution passes all leet code test cases