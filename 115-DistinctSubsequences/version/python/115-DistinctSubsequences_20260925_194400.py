# Last updated: 9/25/2026, 7:44:00 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        cache={}
4        def dfs(i,j):
5            if j==len(t):
6                return 1
7            if i==len(s):
8                return 0
9            if (i,j) in cache:
10                return cache[(i,j)]
11            if s[i]==t[j]:
12                cache[(i,j)]=dfs(i+1,j+1)+dfs(i+1,j)
13            else:
14                cache[(i,j)]=dfs(i+1,j)
15            return cache[(i,j)]
16        return dfs(0,0)
17
18
19