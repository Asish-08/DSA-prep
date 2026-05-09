# Last updated: 5/9/2026, 12:19:29 AM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        Rows,Cols=len(heights),len(heights[0])
4        pac,atl=set(),set()
5
6        def dfs(r,c,visit,prevHeight):
7            if((r,c) in visit or 
8            r<0 or c<0 or r==Rows or c==Cols or heights[r][c]<prevHeight):
9                return
10            visit.add((r,c))
11            dfs(r+1,c,visit,heights[r][c])
12            dfs(r-1,c,visit,heights[r][c])
13            dfs(r,c+1,visit,heights[r][c])
14            dfs(r,c-1,visit,heights[r][c])
15
16        for c in range(Cols):
17            dfs(0,c,pac,heights[0][c])
18            dfs(Rows-1,c,atl,heights[Rows-1][c])
19        
20        for r in range(Rows):
21            dfs(r,0,pac,heights[r][0])
22            dfs(r,Cols-1,atl,heights[r][Cols-1])
23
24        res=[]
25        for r in range(Rows):
26            for c in range(Cols):
27                if (r,c) in pac and (r,c) in atl:
28                    res.append([r,c])
29        return res