# Last updated: 5/9/2026, 8:32:56 AM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        rows,cols=len(board),len(board[0])
7        res=[]
8
9        def bfs(r,c):
10            q=collections.deque()
11            q.append([r,c])
12            board[r][c]= "T"
13            while q:
14                row,col=q.popleft()
15                directions=[[1,0],[-1,0],[0,1],[0,-1]]
16
17                for dr,dc in directions:
18                    R,C=row+dr,col+dc
19                    if (R in range(rows) and C in range(cols) and board[R][C]=="O"):
20                        board[R][C]="T"
21                        q.append([R,C])
22        
23        # traversing through the edges of the O's
24        for r in range(rows):
25            for c in range(cols):
26                if (r==0 or r==rows-1 or 
27                c==0 or c==cols-1) and board[r][c]=="O":
28                    bfs(r,c)
29        
30        # flipping the middle O's to X's
31        for r in range(rows):
32            for c in range(cols):
33                if (board[r][c]=='O'):
34                    board[r][c]='X'
35                elif (board[r][c]=='T'):
36                    board[r][c]='O'
37                    
38
39