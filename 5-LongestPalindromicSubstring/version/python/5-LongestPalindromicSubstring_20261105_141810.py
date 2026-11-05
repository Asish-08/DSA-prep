# Last updated: 11/5/2026, 2:18:10 PM
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
27        # reslen=0
28        # res=""
29
30        # #odd length
31        # for i in range(len(s)):
32        #     l,r=i,i
33        #     while l>=0 and r<len(s) and s[l]==s[r]:
34        #         if r-l+1 >reslen:
35        #             reslen=r-l+1
36        #             res=s[l:r+1]
37        #         l-=1
38        #         r+=1
39        
40        # #even length
41        # for i in range(len(s)):
42        #     l,r=i,i+1
43        #     while l>=0 and r<len(s) and s[l]==s[r]:
44        #         if r-l+1 > reslen:
45        #             reslen=r-l+1
46        #             res=s[l:r+1]
47        #         l-=1
48        #         r+=1
49        # return res
50
51
52        