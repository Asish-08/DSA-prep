# Last updated: 4/30/2026, 12:54:47 PM
1from collections import Counter
2class Solution:
3    def lengthOfLongestSubstring(self, s: str) -> int:
4        chars=Counter()
5        
6        left,right=0,0
7        res=0
8
9        while right<len(s):
10            r=s[right]
11            chars[r]+=1
12            while chars[r]>1:
13                l=s[left]
14                chars[l] -=1
15                left+=1
16
17            res=max(res,right-left+1)
18            right+=1
19        return res
20