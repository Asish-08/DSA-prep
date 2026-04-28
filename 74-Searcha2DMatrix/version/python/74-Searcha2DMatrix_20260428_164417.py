# Last updated: 4/28/2026, 4:44:17 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        for row in matrix:
4            l,r=0,len(row)-1
5            while l<=r:
6                mid=(l+r)//2
7                if row[mid]==target:
8                    return True
9                    break
10                elif row[mid]>target:
11                    r=mid-1
12                else:
13                    l=mid+1
14        return False
15                
16                