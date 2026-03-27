# Last updated: 3/27/2026, 4:46:26 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        rows=collections.defaultdict(set)
4        cols=collections.defaultdict(set)
5        squares=collections.defaultdict(set)
6        for r in range(9):
7            for c in range(9):
8                if board[r][c]==".":
9                    continue
10                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3,c//3]:
11                    return False
12                rows[r].add(board[r][c])
13                cols[c].add(board[r][c])
14                squares[r//3,c//3].add(board[r][c])
15        return True