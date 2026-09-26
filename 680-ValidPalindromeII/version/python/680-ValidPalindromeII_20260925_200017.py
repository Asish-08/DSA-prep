# Last updated: 9/25/2026, 8:00:17 PM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        l,r=0,len(s)-1
4
5        def pal(i,j):
6            while i<j:
7                if s[i]!=s[j]:
8                    return False
9                i+=1
10                j-=1
11            return True
12
13        while l<r:
14            if s[l]!=s[r]:
15                return pal(l+1,r) or pal(l,r-1)
16            l+=1
17            r-=1
18        return True
19
20
21
22
23
24        # if len(s)<=1:
25        #     return True
26        # l,r=0,len(s)-1
27        # def pal(i,j):
28        #     while i<j:
29        #         if s[i]!=s[j]:
30        #             return False
31        #         i+=1
32        #         j-=1
33        #     return True
34        
35        # while l<r:
36        #     if s[l]!=s[r]:
37        #         return pal(l+1,r) or pal(l,r-1)
38        #     l+=1
39        #     r-=1
40        # return True
41        