# Last updated: 7/29/2026, 6:53:46 PM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        if len(s)<=1:
4            return True
5        l,r=0,len(s)-1
6         # delete=1
7        def pal(i,j):
8            while i<j:
9                if s[i]!=s[j]:
10                    return False
11                i+=1
12                j-=1
13            return True
14        
15        while l<r:
16            if s[l]!=s[r]:
17                return pal(l+1,r) or pal(l,r-1)
18            l+=1
19            r-=1
20        return True
21        