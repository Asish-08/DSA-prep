# Last updated: 9/27/2026, 7:12:45 AM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        res=""
4        for i in range(len(strs[0])):
5            for s in strs:
6                if i==len(s) or strs[0][i]!=s[i]:
7                    return res
8            res+=strs[0][i]
9        return res
10
11
12
13        # res=""
14        # for i in range(len(strs[0])):
15        #     for s in strs:
16        #         if i==len(s) or strs[0][i]!=s[i]:
17        #             return res
18        #     res+=strs[0][i]
19        # return res