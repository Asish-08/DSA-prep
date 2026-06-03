# Last updated: 6/2/2026, 6:10:07 PM
1class NumMatrix:
2
3    def __init__(self, matrix: List[List[int]]):
4        self.dp=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
5
6        #prefix sum
7        for r in range(len(self.dp)-1):
8            for c in range(len(self.dp[0])-1):
9                self.dp[r+1][c+1]=matrix[r][c]+self.dp[r][c+1]+self.dp[r+1][c]-self.dp[r][c]
10
11    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
12        ans=0
13        ans=self.dp[row2+1][col2+1]-self.dp[row1][col2+1]-self.dp[row2+1][col1]+self.dp[row1][col1]
14        return ans
15        
16
17
18# Your NumMatrix object will be instantiated and called as such:
19# obj = NumMatrix(matrix)
20# param_1 = obj.sumRegion(row1,col1,row2,col2)