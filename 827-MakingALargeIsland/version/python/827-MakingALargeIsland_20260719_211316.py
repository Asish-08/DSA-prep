# Last updated: 7/19/2026, 9:13:16 PM
1class Solution:
2    def largestIsland(self, grid: List[List[int]]) -> int:
3        n=len(grid)
4        island_size={}
5        label=2
6        #dfs to traverse the grid and see for any potential cells
7        def dfs(r,c,label):
8            if not (0<=r<n and 0<=c<n) or grid[r][c]!=1:
9                return 0
10            
11            grid[r][c]=label
12            size=1
13            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
14                size+=dfs(r+dr,c+dc,label)
15            return size
16        
17        #pre-computing island sizes
18        for r in range(n):
19            for c in range(n):
20                if grid[r][c]==1:
21                    island_size[label]=dfs(r,c,label)
22                    label+=1
23        
24        # Phase 2: Try flipping each 0
25        res= max(island_size.values()) if island_size else 0
26        for r in range(n):
27            for c in range(n):
28                if grid[r][c]==0:
29                    visited=set()
30                    curr=1
31                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
32                        nr, nc = r + dr, c + dc
33
34                        if (
35                            0 <= nr < n
36                            and 0 <= nc < n
37                            and grid[nr][nc] > 1
38                            and grid[nr][nc] not in visited
39                        ):
40                            curr += island_size[grid[nr][nc]]
41                            visited.add(grid[nr][nc])
42
43                    res = max(res, curr)
44
45        return res