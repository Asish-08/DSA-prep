# Last updated: 7/29/2026, 6:58:09 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        n=max(len(word1),len(word2))
4        res=[]
5        for i in range(n):
6            if i <len(word1):
7                res.append(word1[i])
8            if i<len(word2):
9                res.append(word2[i])
10        return ''.join(res)
11    
12