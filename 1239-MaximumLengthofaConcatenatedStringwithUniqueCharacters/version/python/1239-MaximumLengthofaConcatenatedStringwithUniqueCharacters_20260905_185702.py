# Last updated: 9/5/2026, 6:57:02 PM
1class Solution:
2    def maxLength(self, arr: List[str]) -> int:
3        charSet=set()
4
5        def overlap(charSet,s):
6            seen=set()
7            for c in s:
8                #c already exists
9                if c in charSet:
10                    return True
11                #same character appears twice
12                if c in seen:
13                    return True
14                seen.add(c)
15            return False
16
17
18        def backtrack(i):
19            if i==len(arr):
20                return len(charSet)
21            #inlcude the option
22            res=0
23            if not overlap(charSet,arr[i]):
24                for c in arr[i]:
25                    charSet.add(c)
26                res=backtrack(i+1)
27
28                for c in arr[i]:
29                    charSet.remove(c)
30            #exclude the option
31            skip=backtrack(i+1)
32            return max(res,skip)
33        return backtrack(0)
34