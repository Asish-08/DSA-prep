# Last updated: 9/7/2026, 12:47:39 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        # dp=[[1]*n for _ in range(m)]
4        # for i in range(1,m):
5        #     for j in range(1,n):
6        #         dp[i][j]=dp[i-1][j]+dp[i][j-1]
7        # return dp[m-1][n-1]
8        dp=[[1]*n for _ in range(m)]
9        for i in range(1,m):
10            for j in range(1,n):
11                dp[i][j]=dp[i-1][j]+dp[i][j-1]
12        return dp[m-1][n-1]