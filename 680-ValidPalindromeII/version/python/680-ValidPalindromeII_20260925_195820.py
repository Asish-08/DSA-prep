# Last updated: 9/25/2026, 7:58:20 PM
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
12        while l<r:
13            if s[l]!=s[r]:
14                return pal(l+1,r) or pal(l,r-1)
15            l+=1
16            r-=1
17        return True
18
19
20
21
22
23        # if len(s)<=1:
24        #     return True
25        # l,r=0,len(s)-1
26        # def pal(i,j):
27        #     while i<j:
28        #         if s[i]!=s[j]:
29        #             return False
30        #         i+=1
31        #         j-=1
32        #     return True
33        
34        # while l<r:
35        #     if s[l]!=s[r]:
36        #         return pal(l+1,r) or pal(l,r-1)
37        #     l+=1
38        #     r-=1
39        # return True
40        