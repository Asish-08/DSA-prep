# Last updated: 5/1/2026, 7:23:05 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        n1=len(s1)
4        n2=len(s2)
5        if n1>n2:
6            return False
7        s1_counts=[0]*26
8        s2_counts=[0]*26
9
10        for i in range(n1):
11            s1_counts[ord(s1[i])-ord('a')]+=1
12            s2_counts[ord(s2[i])-ord('a')]+=1
13        if s1_counts==s2_counts:
14            return True
15        
16        for i in range(n1,n2):
17            s2_counts[ord(s2[i])-ord('a')] +=1
18            s2_counts[ord(s2[i-n1])-ord('a')] -=1
19            if s1_counts==s2_counts:
20                return True
21        return False
22
23        
24