# Last updated: 9/26/2026, 7:03:51 PM
1class Solution:
2    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
3        A=img1
4        B=img2
5        N=len(A)
6
7
8        def helper(x_shift,y_shift):
9            num=0
10            for r in range(N):
11                for c in range(N):
12                    if 0<=r+y_shift<N and 0<=c+x_shift<N and A[r+y_shift][c+x_shift]==1 and B[r][c]==1:
13                        num+=1
14            return num
15        
16        return max([helper(x,y) for x in range(-N,N) for y in range(-N,N)])
17