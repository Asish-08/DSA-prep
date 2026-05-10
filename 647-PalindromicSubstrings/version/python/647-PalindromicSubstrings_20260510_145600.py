# Last updated: 5/10/2026, 2:56:00 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        # reslen=0
4        count=0
5        #odd length
6        for i in range(len(s)):
7            l,r=i,i
8            while l>=0 and r<len(s) and s[l]==s[r]:
9                count+=1
10                l-=1
11                r+=1
12        #even length
13        for i in range(len(s)):
14            l,r=i,i+1
15            while l>=0 and r<len(s) and s[l]==s[r]:
16                count+=1
17                l-=1
18                r+=1
19        return count
20