/**
 * LeetCode #121: Best Time to Buy and Sell Stock
 * Difficulty: Easy
 * Language: Python
 * Date: 2026-10-12T23:06:10.372Z
 */

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit