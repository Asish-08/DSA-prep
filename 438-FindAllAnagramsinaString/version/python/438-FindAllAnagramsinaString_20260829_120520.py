# Last updated: 8/29/2026, 12:05:20 PM
1class Solution:
2    def findAnagrams(self, s: str, p: str) -> List[int]:
3        ns,np=len(s),len(p)
4        output=[]
5        p_count=Counter(p)
6        s_count=Counter()
7
8        for i in range(ns):
9            s_count[s[i]]+=1
10
11            if i>=np:
12                if s_count[s[i-np]]==1:
13                    del s_count[s[i-np]]
14                else:
15                    s_count[s[i-np]]-=1
16            if s_count==p_count:
17                output.append(i-np+1)
18        return output