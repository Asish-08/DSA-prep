# Last updated: 5/7/2026, 11:08:22 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        rows,cols=len(board),len(board[0])
4        path=set()
5        res=[]
6        def dfs(r,c,i):
7            if i==len(word):
8                return True
9            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in path or word[i]!=board[r][c]:
10                return False
11            
12            path.add((r,c))
13            res=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
14            path.remove((r,c))
15            return res
16        for r in range(rows):
17            for c in range(cols):
18                if dfs(r,c,0):
19                    return True
20        return False