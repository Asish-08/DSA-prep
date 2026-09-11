# Last updated: 9/10/2026, 8:16:11 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        reslen=0
4        res=""
5
6        #odd length with same position of 2 pointers
7        for i in range(len(s)):
8            l,r=i,i
9            while l>=0 and r<len(s) and s[l]==s[r]:
10                if r-l+1>reslen:
11                    reslen=r-l+1
12                    res=s[l:r+1]
13                l-=1
14                r+=1
15        
16        #even length where 2 pointers will be adjacent to eachother
17        for i in range(len(s)):
18            l,r=i,i+1
19            while l>=0 and r<len(s) and s[l]==s[r]:
20                if r-l+1>reslen:
21                    reslen=r-l+1
22                    res=s[l:r+1]
23                l-=1
24                r+=1
25
26        return res
27
28
29
30
31
32
33
34
35
36        # reslen=0
37        # res=""
38
39        # #odd length
40        # for i in range(len(s)):
41        #     l,r=i,i
42        #     while l>=0 and r<len(s) and s[l]==s[r]:
43        #         if r-l+1 >reslen:
44        #             reslen=r-l+1
45        #             res=s[l:r+1]
46        #         l-=1
47        #         r+=1
48        
49        # #even length
50        # for i in range(len(s)):
51        #     l,r=i,i+1
52        #     while l>=0 and r<len(s) and s[l]==s[r]:
53        #         if r-l+1 > reslen:
54        #             reslen=r-l+1
55        #             res=s[l:r+1]
56        #         l-=1
57        #         r+=1
58        # return res
59
60
61        