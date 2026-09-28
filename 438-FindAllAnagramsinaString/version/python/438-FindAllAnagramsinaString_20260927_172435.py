# Last updated: 9/27/2026, 5:24:35 PM
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
19
20        # for i in range(ns):
21        #     s_count[s[i]]+=1
22
23        #     if i>=np:
24        #         if s_count[s[i-np]]==1:
25        #             del s_count[s[i-np]]
26        #         else:
27        #             s_count[s[i-np]]-=1
28        #     if s_count==p_count:
29        #         output.append(i-np+1)
30        # return output