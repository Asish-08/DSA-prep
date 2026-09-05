# Last updated: 9/5/2026, 3:58:52 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        word_set=set(wordDict)
4        dp=[False]*(len(s)+1)
5        dp[0]=True
6
7        for i in range(1,len(s)+1):
8            for j in range(i):
9                if dp[j] and s[j:i] in word_set:
10                    dp[i]=True
11                    break
12        return dp[len(s)]