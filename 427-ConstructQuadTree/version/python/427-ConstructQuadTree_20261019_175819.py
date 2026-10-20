# Last updated: 10/19/2026, 5:58:19 PM
1"""
2# Definition for a QuadTree node.
3class Node:
4    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
5        self.val = val
6        self.isLeaf = isLeaf
7        self.topLeft = topLeft
8        self.topRight = topRight
9        self.bottomLeft = bottomLeft
10        self.bottomRight = bottomRight
11"""
12
13class Solution:
14    def construct(self, grid: List[List[int]]) -> 'Node':
15        def dfs(n,r,c):
16            allSame=True
17            for i in range(n):
18                for j in range(n):
19                    if grid[r][c]!=grid[r+i][c+j]:
20                        allSame=False
21                        break
22            if allSame:
23                return Node(grid[r][c],True,None,None,None,None)
24            
25            n=n//2
26            topLeft=dfs(n,r,c)
27            topRight=dfs(n,r,c+n)
28            bottomLeft=dfs(n,r+n,c)
29            bottomRight=dfs(n,r+n,c+n)
30
31            return Node(0,False,topLeft,topRight,bottomLeft,bottomRight)
32        return dfs(len(grid),0,0)
33
34