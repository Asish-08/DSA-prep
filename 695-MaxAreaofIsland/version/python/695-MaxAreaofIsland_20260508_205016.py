# Last updated: 5/8/2026, 8:50:16 PM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        if not grid:
4            return 0
5        rows,cols=len(grid),len(grid[0])
6        max_area=0
7        cur_area=0
8        visit=set()
9
10        def bfs(r,c):
11            q=collections.deque()
12            q.append((r,c))
13            visit.add((r,c))
14            area=0
15
16            while q:
17                row,col=q.popleft()
18                directions=[[1,0],[-1,0],[0,1],[0,-1]]
19                for dr,dc in directions:
20                    R,C=row+dr,col+dc
21                    if (R in range(rows) and 
22                    C in range(cols) and 
23                    (R,C) not in visit and 
24                    grid[R][C]==1):
25                        q.append((R,C))
26                        visit.add((R,C))
27                area+=1
28            return area
29                        
30
31        for r in range(rows):
32            for c in range(cols):
33                if grid[r][c]==1 and (r,c) not in visit :
34                    cur_area= bfs(r,c)
35                max_area=max(max_area,cur_area)
36        return max_area
37
38