# Last updated: 7/12/2026, 10:42:49 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        islands=0
4        visit=set()
5        rows,cols=len(grid),len(grid[0])
6        def bfs(r,c):
7            q=collections.deque()
8            q.append((r,c))
9            visit.add((r,c))
10            
11            while q:
12                directions=[(-1,0),(0,-1),(1,0),(0,1)]
13                row,col=q.popleft()
14                for dr,dc in directions:
15                    R,C=row+dr,col+dc
16                    if R in range(rows) and C in range(cols) and grid[R][C]=="1" and (R,C) not in visit:
17                        q.append((R,C))
18                        visit.add((R,C))
19        
20        for r in range(rows):
21            for c in range(cols):
22                if grid[r][c]=="1" and (r,c) not in visit:
23                    bfs(r,c)
24                    islands+=1
25        return islands