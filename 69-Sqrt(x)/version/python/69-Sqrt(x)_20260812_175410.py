# Last updated: 8/12/2026, 5:54:10 PM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x<2:
4            return x
5        l,r=2,x//2
6
7        while l<=r:
8            mid=l+(r-l)//2
9            num=mid*mid
10            if num>x:
11                r=mid-1
12            elif num<x:
13                l=mid+1
14            else:
15                return mid
16        return r
17