# Last updated: 3/24/2026, 11:13:45 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s=Counter(s)
4        t=Counter(t)
5        if s==t:
6            return True
7        else:
8            return False