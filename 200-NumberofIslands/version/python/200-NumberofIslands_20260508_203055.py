# Last updated: 5/8/2026, 8:30:55 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        islands=0
4        visit=set()
5        rows,cols=len(grid),len(grid[0])
6
7        def bfs(r,c):
8            q=collections.deque()
9            q.append((r,c))
10            visit.add((r,c))
11            while q:
12                row,col=q.popleft()
13                directions=[[1,0],[-1,0],[0,1],[0,-1]]
14                for dr,dc in directions:
15                    r,c=row+dr,col+dc
16                    if (r in range(rows) and 
17                    c in range(cols) and
18                    grid[r][c]=="1" and 
19                    (r,c) not in visit):
20                        q.append((r,c))
21                        visit.add((r,c))
22
23        for r in range(rows):
24            for c in range(cols):
25                if grid[r][c]=="1" and (r,c) not in visit:
26                    bfs(r,c)
27                    islands+=1
28        return islands
29            