# Last updated: 9/26/2026, 7:21:23 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        chars=Counter()
4        left,right=0,0
5        res=0
6
7        while right<len(s):
8            r=s[right]
9            chars[r]+=1
10            while chars[r]>1:
11                l=s[left]
12                chars[l]-=1
13                left+=1
14            res=max(res,right-left+1)
15            right+=1
16        return res
17            
18
19
20
21
22
23
24
25
26
27
28
29
30        # chars=Counter()
31        # left,right=0,0
32        # res=0
33
34        # while right<len(s):
35        #     r=s[right]
36        #     chars[r]+=1
37        #     while chars[r]>1:
38        #         l=s[left]
39        #         chars[l]-=1
40        #         left+=1
41
42        #     res=max(res,right-left+1)
43        #     right+=1
44        # return res
45            