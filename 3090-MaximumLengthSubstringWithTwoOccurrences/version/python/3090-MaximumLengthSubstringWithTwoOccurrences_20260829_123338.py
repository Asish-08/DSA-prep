# Last updated: 8/29/2026, 12:33:38 PM
1class Solution:
2    def maximumLengthSubstring(self, s: str) -> int:
3        left=0
4        ans=0
5        freq=defaultdict(int)
6
7        for right in range(len(s)):
8            freq[s[right]]+=1
9
10            while freq[s[right]]>2:
11                freq[s[left]]-=1
12                left+=1
13            ans=max(ans,right-left+1)
14        return ans