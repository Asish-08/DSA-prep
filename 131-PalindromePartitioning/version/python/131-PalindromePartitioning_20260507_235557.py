# Last updated: 5/7/2026, 11:55:57 PM
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
11                if self.isPali(s,i,j):
12                    part.append(s[i:j+1])
13                    dfs(j+1)
14                    part.pop()
15        dfs(0)
16        return res
17    def isPali(self,s,l,r):
18        while l<r:
19            if s[l]!=s[r]:
20                return False
21            l+=1
22            r-=1
23        return True