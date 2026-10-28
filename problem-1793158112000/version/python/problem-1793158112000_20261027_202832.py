# Last updated: 10/27/2026, 8:28:32 PM
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        # for i in range(n):
7        #     if (isBadVersion(i)):
8        #         return i
9        # return n
10        left,right=0,n
11        while left<right:
12            mid=(left+right)//2
13            if (isBadVersion(mid)):
14                right=mid
15            else:
16                left=mid+1
17        return left
18
19
20            
21