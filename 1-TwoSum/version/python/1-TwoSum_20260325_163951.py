# Last updated: 3/25/2026, 4:39:51 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hashmap={}
4        for i,val in enumerate(nums):
5            diff=target-val
6            if diff in hashmap:
7                return [hashmap[diff],i]
8            hashmap[val]=i