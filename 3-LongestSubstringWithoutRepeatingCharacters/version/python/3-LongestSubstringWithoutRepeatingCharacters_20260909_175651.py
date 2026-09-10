# Last updated: 9/9/2026, 5:56:51 PM
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
14            right+=1
15            res=max(res,right-left)
16        return res