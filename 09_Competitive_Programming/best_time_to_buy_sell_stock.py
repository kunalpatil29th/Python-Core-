# best_time_to_buy_sell_stock.py

"""
Problem: Best Time to Buy and Sell Stock
You are given an array 'prices' where prices[i] is the price of a given stock on the ith day. 
Maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
"""

def max_profit(prices):
    l, r = 0, 1 # l=buy, r=sell
    max_p = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1
    return max_p

# Example
prices = [7, 1, 5, 3, 6, 4]
print(f"Maximum profit: {max_profit(prices)}")
