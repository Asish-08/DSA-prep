# Last updated: 5/10/2026, 3:23:54 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        dp={len(s):1}
4
5        for i in range(len(s)-1,-1,-1):
6            if s[i]=='0':
7                dp[i]=0
8            else:
9                dp[i]=dp[i+1]
10            
11            if i+1<len(s) and 10<=int(s[i:i+2])<=26:
12                dp[i]+=dp[i+2]
13            
14        return dp[0]