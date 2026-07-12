# Last updated: 7/12/2026, 11:45:14 AM
1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        par=[i for i in range(n)]
4        rank=[1]*n
5
6        def find(n1):
7            res=n1
8            while res!=par[res]:
9                par[res]=par[par[res]]
10                res=par[res]
11            return res
12        
13        def union(n1,n2):
14            p1,p2=find(n1),find(n2)
15            if p1==p2:
16                return 0
17            
18            if rank[p2]>rank[p1]:
19                par[p1]=p2
20                rank[p2]+=rank[p1]
21            else:
22                par[p2]=p1
23                rank[p1]+=rank[p2]
24            return 1
25        
26        res=n
27        for n1,n2 in edges:
28            res-=union(n1,n2)
29        return res
30
31