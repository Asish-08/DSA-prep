# Last updated: 3/3/2026, 3:26:24 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        # x=str(x)
4        # if x[::-1] == x : 
5        #     return True
6        # else:
7        #     return False
8        orig=x
9        rev=0
10        if x<0:
11            return False
12        while x:
13            x,d=divmod(x,10)
14            rev=rev*10+d
15        if orig==rev:
16            return True
17        else:
18            return False
19