# Last updated: 5/7/2026, 11:47:20 PM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        res=[]
4        part=[]
5
6        def dfs(i):
7            if i>=len(s):
8                res.append(part[:])
9                return
10            for j in range(i,len(s)):
11                if self.ispali(s,i,j):
12                    part.append(s[i:j+1])
13                    dfs(j+1)
14                    part.pop()
15
16        dfs(0)
17        return res
18
19    def ispali(self,s,l,r):
20        while l<r:
21            if s[l] != s[r]:
22                return False
23            l,r=l+1,r-1
24        return True
25