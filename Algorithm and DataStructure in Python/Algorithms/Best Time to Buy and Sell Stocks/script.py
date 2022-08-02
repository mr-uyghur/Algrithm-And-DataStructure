
def maxProfit(prices):
    min_profit, max_profit = float('inf'), 0

    for price in prices:
        profit_today = price - min_profit
        max_profit = max(max_profit, profit_today)
        min_profit = min(min_profit, price)
    return max_profit

print(maxProfit([7,1,5,3,6,4]))

print(maxProfit([7,6,4,3,1]))

