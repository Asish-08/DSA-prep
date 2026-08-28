# Last updated: 8/27/2026, 10:38:39 PM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x<2:
4            return x
5        l=1
6        r=x//2
7
8        while l<=r:
9            mid=l+(r-l)//2
10            if mid*mid==x:
11                return mid
12            elif mid*mid < x:
13                l=mid+1
14            else:
15                r=mid-1
16        return r