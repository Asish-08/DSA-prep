# Last updated: 7/29/2026, 6:43:46 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        l,r=0,len(s)-1
7        while l< r:
8            s[l],s[r]=s[r],s[l]
9            l+=1
10            r-=1
11        
12            
13