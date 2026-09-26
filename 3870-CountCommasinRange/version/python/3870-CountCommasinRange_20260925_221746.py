# Last updated: 9/25/2026, 10:17:46 PM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        n_len=len(str(n))
4
5        if n_len<=3:
6            return 0
7        else:
8            q,r=divmod(n,1000)
9            return (q-1)*1000+(r+1)