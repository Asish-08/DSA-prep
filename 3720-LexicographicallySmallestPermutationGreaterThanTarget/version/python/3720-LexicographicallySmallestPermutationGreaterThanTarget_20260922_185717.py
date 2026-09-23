# Last updated: 9/22/2026, 6:57:17 PM
1from string import ascii_lowercase
2class Solution:
3    def lexGreaterPermutation(self, s: str, target: str) -> str:
4        count=Counter(s)
5        prefix=[]
6
7        for c in target:
8            if count[c]==0:
9                break
10            count[c]-=1
11            prefix.append(c)
12        
13        for i in range(len(prefix),-1,-1):
14            if i<len(target):
15                for c in ascii_lowercase:
16                    if c > target[i] and count[c]>0:
17                        count[c]-=1
18
19                        suffix="".join(char*count[char] for char in ascii_lowercase)
20                        return "".join(prefix[:i])+c+suffix
21
22            if i>0:
23                count[prefix[i-1]]+=1
24        return ""
25
26