# Last updated: 8/28/2026, 7:39:59 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n1=len(s1)
4        n2=len(s2)
5        if n1>n2:
6            return False
7
8        s1_counts=[0]*26
9        s2_counts=[0]*26
10
11        for i in range(n1):
12            s1_counts[ord(s1[i])-ord('a')]+=1
13            s2_counts[ord(s2[i])-ord('a')]+=1
14        # Check the first complete window.
15        if s1_counts==s2_counts:
16            return True
17        
18        for i in range(n1,n2):
19            s2_counts[ord(s2[i])-ord('a')]+=1 #right pointer inc
20            s2_counts[ord(s2[i-n1])-ord('a')]-=1 #left pointer dec
21            if s1_counts==s2_counts:
22                return True
23        return False
24
25        
26        