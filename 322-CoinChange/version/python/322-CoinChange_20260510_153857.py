# Last updated: 5/10/2026, 3:38:57 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        dp=[float('inf')] * (amount+1)
4        dp[0]=0
5
6        for coin in coins:
7            for i in range(coin, amount+1):
8                dp[i]=min(dp[i],dp[i-coin]+1)
9        
10        return dp[amount] if dp[amount]!=float('inf') else -1
11
12