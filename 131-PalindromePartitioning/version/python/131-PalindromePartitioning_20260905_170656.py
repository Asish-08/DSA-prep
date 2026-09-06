# Last updated: 9/5/2026, 5:06:56 PM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        res=[]
4        path=[]
5
6        def isPali(s,l,r):
7            while l<r:
8                if s[l]!=s[r]:
9                    return False
10                l+=1
11                r-=1
12            return True
13        
14        def dfs(i):
15            if i>=len(s):
16                res.append(path[:])
17                return
18            for j in range(i,len(s)):
19                if isPali(s,i,j):
20                    path.append(s[i:j+1])
21                    dfs(j+1)
22                    path.pop()
23        dfs(0)
24        return res