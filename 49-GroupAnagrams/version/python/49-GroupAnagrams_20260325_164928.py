# Last updated: 3/25/2026, 4:49:28 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        hashmap=defaultdict(list)
4        res=[]
5
6        for s in strs:
7            sorted_s=tuple(sorted(s))
8            hashmap[sorted_s].append(s)
9        
10        for val in hashmap.values():
11            res.append(val)
12        return res