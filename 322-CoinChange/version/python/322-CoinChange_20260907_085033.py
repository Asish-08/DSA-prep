# Last updated: 9/7/2026, 8:50:33 AM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        dp=[float('inf')] * (amount+1)
4        dp[0]=0 #Base case: 0 coins to make amount 0
5
6        # for coin in coins:
7        #     for i in range(coin, amount+1):
8        #         dp[i]=min(dp[i],dp[i-coin]+1) # Use this coin
9        
10        # return dp[amount] if dp[amount]!=float('inf') else -1
11
12        for a in range(1,amount+1):
13            for coin in coins:
14                if a-coin>=0:
15                    dp[a]=min(dp[a],1+dp[a-coin])
16        return dp[amount] if dp[amount] !=float('inf') else -1
17
18