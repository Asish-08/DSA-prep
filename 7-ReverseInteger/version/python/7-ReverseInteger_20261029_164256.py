# Last updated: 10/29/2026, 4:42:56 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        int_min,int_max=-2**31, 2**31-1
4        rev=0
5        sign=-1 if x<0 else 1
6        x=abs(x)
7        while x:
8            x,r=divmod(x,10)
9            if rev>int_max//10 or (x==int_max//10 and r>7):
10                return 0
11            rev=rev*10+r
12        return rev*sign
13
14
15#Have to check if th existing rev is greater than int_max//10 or check 
16#if rev is at 214748364, the last digit cannot exceed 7