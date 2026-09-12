# Last updated: 9/12/2026, 1:15:37 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        fresh=0
4        q=deque()
5        rows,cols=len(grid),len(grid[0])
6        for i in range(rows):
7            for j in range(cols):
8                if grid[i][j]==1:
9                    fresh+=1
10                elif grid[i][j]==2:
11                    q.append((i,j))
12        minutes=0
13
14        while q and fresh>0:
15            for _ in range(len(q)):  #iterating though all the rotten oranges in q
16                r,c=q.popleft()
17                directions=[(-1,0),(1,0),(0,-1),(0,1)]
18                for dr,dc in directions:
19                    row,col=r+dr,c+dc
20                    if row in range(rows) and col in range(cols) and grid[row][col]==1:
21                        grid[row][col]=2
22                        fresh-=1
23                        q.append((row,col))
24            minutes+=1
25        return minutes if fresh==0 else -1
26
27
28
29
30        # fresh=0
31        # q=deque()
32        # rows,cols=len(grid),len(grid[0])
33
34        # for r in range(rows):
35        #     for c in range(cols):
36        #         if grid[r][c]==2:
37        #             q.append((r,c))
38        #         elif grid[r][c]==1:
39        #             fresh+=1
40        # minutes=0
41
42        # while q and fresh>0:
43        #     for _ in range(len(q)):
44        #         r,c=q.popleft()
45        #         directions=[[-1,0],[1,0],[0,1],[0,-1]]
46
47        #         for dr,dc in directions:
48        #             R,C=r+dr,c+dc
49        #             if (R in range(rows) and C in range(cols) and grid[R][C]==1):
50        #                 q.append((R,C))
51        #                 fresh-=1
52        #                 grid[R][C]=2
53        #     minutes+=1
54        # return minutes if fresh==0 else -1