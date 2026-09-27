# Last updated: 9/26/2026, 7:30:40 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price=float('inf')
4        max_price=0
5        
6        for i in prices:
7            if i<min_price:
8                min_price=i
9            else:
10                profit=i-min_price
11                max_price=max(max_price,profit)
12        return max_price
13
14
15
16
17
18
19
20        # min_price=float("inf")
21        # max_profit=0
22        # for i in prices:
23        #     if i<min_price:
24        #         min_price=i
25        #     else:
26        #         profit=i-min_price
27        #         max_profit=max(profit,max_profit)
28        # return max_profit
29       