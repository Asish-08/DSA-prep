# Last updated: 4/30/2026, 12:42:03 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price=float("inf")
4        max_profit=0
5        for i in prices:
6            if i<min_price:
7                min_price=i
8            else:
9                profit=i-min_price
10                max_profit=max(profit,max_profit)
11        return max_profit