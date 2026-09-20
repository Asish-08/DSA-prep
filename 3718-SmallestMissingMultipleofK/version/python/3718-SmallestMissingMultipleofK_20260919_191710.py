# Last updated: 9/19/2026, 7:17:10 PM
1class Solution:
2    def missingMultiple(self, nums: List[int], k: int) -> int:
3        nums_set=set(nums)
4        multiple=1
5        while True:
6            var=k*multiple
7            if var not in nums:
8                return var
9            multiple+=1
10        
11