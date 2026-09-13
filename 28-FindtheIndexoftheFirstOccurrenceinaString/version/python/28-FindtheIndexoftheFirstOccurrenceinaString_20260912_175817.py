# Last updated: 9/12/2026, 5:58:17 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        h=len(haystack)
4        n=len(needle)
5        for i in range(h):
6            if haystack[i:i+n]==needle:
7                return i
8        return -1