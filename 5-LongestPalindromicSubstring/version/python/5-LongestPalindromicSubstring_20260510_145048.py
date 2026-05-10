# Last updated: 5/10/2026, 2:50:48 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        reslen=0
4        res=""
5
6        #odd length
7        for i in range(len(s)):
8            l,r=i,i
9            while l>=0 and r<len(s) and s[l]==s[r]:
10                if r-l+1 >reslen:
11                    reslen=r-l+1
12                    res=s[l:r+1]
13                l-=1
14                r+=1
15        
16        #even length
17        for i in range(len(s)):
18            l,r=i,i+1
19            while l>=0 and r<len(s) and s[l]==s[r]:
20                if r-l+1 > reslen:
21                    reslen=r-l+1
22                    res=s[l:r+1]
23                l-=1
24                r+=1
25        return res
26
27
28        