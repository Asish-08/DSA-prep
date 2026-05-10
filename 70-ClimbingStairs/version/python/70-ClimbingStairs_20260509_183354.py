# Last updated: 5/9/2026, 6:33:54 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        one,two=1,1
4
5        for i in range(n-1):
6            temp=one
7            one=one+two
8            two=temp
9        return one