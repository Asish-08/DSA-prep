# Last updated: 5/1/2026, 7:16:27 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n1=len(s1)
4        n2=len(s2)
5        if n1>n2:
6            return False
7        s1_counts=[0]*26
8        s2_counts=[0]*26
9        for i in range(n1):
10            s1_counts[ord(s1[i])-ord('a')]+=1
11            s2_counts[ord(s2[i])-ord('a')]+=1
12        if s1_counts==s2_counts:
13            return True
14        for i in range(n1,n2):
15            s2_counts[ord(s2[i])-ord('a')]+=1
16            s2_counts[ord(s2[i-n1])-ord('a')] -=1
17            if s1_counts==s2_counts:
18                return True
19        return False
20