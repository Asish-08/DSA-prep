# Last updated: 7/23/2026, 4:35:42 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        islands=0
4        visit=set()
5        rows,cols=len(grid),len(grid[0])
6
7        def bfs(r,c):
8            q=deque()
9            q.append((r,c))
10            visit.add((r,c))
11
12            while q:
13                directions=[(-1,0),(0,-1),(1,0),(0,1)]
14                r,c = q.popleft()
15                for dr,dc in directions:
16                    row,col=r+dr,c+dc
17                    if row in range(rows) and col in range(cols) and grid[row][col] =="1" and (row,col) not in visit :
18                        visit.add((row,col))
19                        q.append((row,col))
20        
21        
22        for r in range(rows):
23            for c in range(cols):
24                if grid[r][c]=="1" and (r,c) not in visit:
25                    bfs(r,c)
26                    islands+=1
27        return islands