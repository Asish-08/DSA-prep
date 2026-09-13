# Last updated: 9/12/2026, 5:59:49 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        h=len(haystack)
4        n=len(needle)
5
6        for i in range(h-n+1):
7            if haystack[i:i+n]==needle:
8                return i
9        return -1