# Last updated: 6/2/2026, 6:27:01 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        h_map=Counter(nums)
4        n=len(nums)//3
5        res=[]
6        for key,val in h_map.items():
7            if val>n:
8                res.append(key)
9        return res
10