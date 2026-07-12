# Last updated: 7/12/2026, 12:25:09 PM
1class Solution:
2    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
3        parent={}
4        rank={}
5        islands=0
6        grid=[[0]*n for _ in range(m)]
7        result=[]
8
9        def find(n1):
10            while parent[n1] != n1:
11                parent[n1]=parent[parent[n1]]
12                n1=parent[n1]
13            return n1
14
15        def union(n1,n2):
16            p1,p2= find(n1),find(n2)
17            if p1==p2:
18                return False
19            
20            if rank[p2]>rank[p1]:
21                parent[p1]=p2
22                rank[p2]+=rank[p1]
23            else:
24                parent[p2]=p1
25                rank[p1]+=rank[p2]
26            return True
27        
28        for r,c in positions:
29            if grid[r][c]==1:
30                result.append(islands)
31                continue
32            grid[r][c]=1
33            parent[(r,c)]=(r,c)
34            rank[(r,c)]=0
35            islands+=1
36
37            for dr,dc in [(-1,0),(0,-1),(1,0),(0,1)]:
38                row,col=r+dr,c+dc
39                if 0<=row<m and 0<=col<n and grid[row][col]==1:
40                    if union((r,c),(row,col)):
41                        islands-=1
42
43            result.append(islands)
44        return result
45