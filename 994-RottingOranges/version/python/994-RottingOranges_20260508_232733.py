# Last updated: 5/8/2026, 11:27:33 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        rows,cols=len(grid),len(grid[0])
4        fresh=0
5        q=deque()
6
7        for r in range(rows):
8            for c in range(cols):
9                if grid[r][c]==2:
10                    q.append((r,c))
11                elif grid[r][c]==1:
12                    fresh+=1
13        minutes=0
14
15        while q and fresh>0:
16            for i in range(len(q)):
17                r,c=q.popleft()
18                directions=[[1,0],[-1,0],[0,1],[0,-1]]
19
20                for dr,dc in directions:
21                    R,C=r+dr,c+dc
22                    if (R in range(rows) and C in range(cols) and grid[R][C]==1):
23                        q.append((R,C))
24                        fresh-=1
25                        grid[R][C]=2
26            minutes+=1
27        return minutes if fresh==0 else -1
28