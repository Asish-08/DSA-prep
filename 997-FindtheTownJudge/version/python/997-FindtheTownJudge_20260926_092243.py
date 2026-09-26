# Last updated: 9/26/2026, 9:22:43 AM
1class Solution:
2    def findJudge(self, n: int, trust: list[list[int]]) -> int:
3        trusts={i:0 for i in range(1,n+1)}
4        trusted_by={i:0 for i in range(1,n+1)}
5
6        for a,b in trust:
7            trusts[a]+=1
8            trusted_by[b]+=1
9        
10        for person in range(1,n+1):
11            if trusts[person]==0 and trusted_by[person]==n-1:
12                return person
13        return -1